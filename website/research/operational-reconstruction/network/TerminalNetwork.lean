import PortQuotient
set_option autoImplicit false
namespace OperationalNetwork
variable {X : Type}

/-- Travel from a retained port to the next retained port with no observation
    in between. Waiting loops and repeated hidden sites are allowed. -/
inductive Excursion (e : Passage X) (keep : X → Bool) : X → X → Nat → Prop where
  | one {x y t} : e x y t → Excursion e keep x y t
  | add {x y z t c} : e x y t → keep y=false → Excursion e keep y z c →
      Excursion e keep x z (t+c)

abbrev Terminal (keep : X → Bool) := {x : X // keep x=true}

def terminalEdge (e : Passage X) (keep : X → Bool) : Passage (Terminal keep) :=
  fun x y t => Excursion e keep x.val y.val t

theorem excursionRuns {e : Passage X} {keep : X → Bool} {x y : X} {t : Nat}
    (exc : Excursion e keep x y t) : ∃ n, Itinerary e x y t n := by
  induction exc with
  | one edge => exact ⟨1,by simpa using Itinerary.step edge (.stay _)⟩
  | add edge _ _ ih =>
    obtain ⟨n,h⟩ := ih
    exact ⟨n+1,.step edge h⟩

theorem expandTerminalTrip {e : Passage X} {keep : X → Bool} {i j : Terminal keep} {c n : Nat}
    (trip : Itinerary (terminalEdge e keep) i j c n) : ∃ m, Itinerary e i.val j.val c m := by
  induction trip with
  | stay => exact ⟨0,.stay _⟩
  | step exc _ ih =>
    obtain ⟨_,first⟩ := excursionRuns exc
    obtain ⟨_,tail⟩ := ih
    exact ⟨_,joinTrips first tail⟩

/-- Split just before the first observed station reached after departure. -/
private theorem splitTerminalTrip {e : Passage X} {keep : X → Bool} {x z : X} {c n : Nat}
    (trip : Itinerary e x z c n) (last : keep z=true) :
    (x=z ∧ c=0) ∨ ∃ (v : Terminal keep) (a b m : Nat), a+b=c ∧ Excursion e keep x v.val a ∧
      Itinerary (terminalEdge e keep) v ⟨z,last⟩ b m := by
  induction trip with
  | stay => exact Or.inl ⟨rfl,rfl⟩
  | @step x y z t c n edge _ ih =>
    right
    rcases ih last with ⟨rfl,rfl⟩ | ⟨v,a,b,m,rfl,first,tail⟩
    · exact ⟨⟨y,last⟩,t,0,0,rfl,.one edge,.stay _⟩
    · cases mid : keep y with
      | false => exact ⟨v,t+a,b,m,Nat.add_assoc _ _ _,.add edge mid first,tail⟩
      | true =>
        exact ⟨⟨y,mid⟩,t,a+b,m+1,rfl,.one edge,.step first tail⟩

theorem terminalRunsExactly {e : Passage X} {keep : X → Bool} (x y : Terminal keep) (t : Nat) :
    (∃ n, Itinerary (terminalEdge e keep) x y t n) ↔ ∃ m, Itinerary e x.val y.val t m := by
  constructor
  · rintro ⟨_,h⟩; exact expandTerminalTrip h
  · rintro ⟨_,h⟩
    rcases splitTerminalTrip h y.property with ⟨eq,rfl⟩ | ⟨_,a,b,m,rfl,first,tail⟩
    · obtain rfl := Subtype.ext eq
      exact ⟨0,.stay _⟩
    · exact ⟨m+1,.step first tail⟩

theorem terminalReachExactly {e : Passage X} {keep : X → Bool} (x y : Terminal keep) (b : Nat) :
    CanReach (terminalEdge e keep) x y b ↔ CanReach e x.val y.val b := by
  constructor
  · rintro ⟨c,_,le,h⟩
    obtain ⟨m,k⟩ := expandTerminalTrip h
    exact ⟨c,m,le,k⟩
  · rintro ⟨c,n,le,h⟩
    obtain ⟨m,k⟩ := (terminalRunsExactly x y c).2 ⟨n,h⟩
    exact ⟨c,m,le,k⟩

end OperationalNetwork
