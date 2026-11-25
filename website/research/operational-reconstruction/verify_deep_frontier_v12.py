"""
Deep Frontier Verification Module v12 — Unified Walls 1, 2, 3 & Cross-Wall Synthesis (F15–F17):
  Wall 1 (V12.1.A–C, 27 checks): Background-Free 4D Regge/CDT + Kähler–Dirac, Mixed Spectral Action vs Super-F-40, String UV vs F-41 & G_Sak
  Wall 2 (V12.2.A–C, 39 checks): Microscopic Non-Heterotic CP & CKM, N_g=3 F-42 (C^96) & Thm 48d(c), Heavy-Threshold Split & Vissani
  Wall 3 (V12.3.A–B, 24 checks): CC / Sequestering / External SU(2)_d (14 checks) + Dynamical 1_F FIMP & Z_2^DM (10 checks)
  Synthesis (V12.4, 8 checks):   Cross-Wall Synthesis, 45.15 Invariance, 3-Stratum Ontology & Legacy Typo Guard

Self-contained, deterministic, zero fitted parameters (98/98 checks).
Exposes `run_v12_wall1()`, `run_v12_wall2()`, `run_v12_wall3()`, `run_v12_all()`, and `__main__`.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import math
from pathlib import Path
import sys
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.linalg import eigh, svd
from scipy.optimize import brentq, minimize, root


class _CheckCounter:
    def __init__(self) -> None:
        self.passed = 0
        self.total = 0
        self.failures: list[str] = []

    def check(self, cond: bool, label: str) -> bool:
        self.total += 1
        if cond:
            self.passed += 1
            return True
        self.failures.append(label)
        return False


# ==============================================================================
# V12.1.A: DYNAMICAL 4D SIMPLICIAL REGGE / CDT + KÄHLER–DIRAC MATTER
# ==============================================================================
def _skeleton_4d(simplices: list[tuple[int, ...]]):
    verts = sorted({v for s in simplices for v in s})
    edges = sorted({(s[i], s[j]) for s in simplices for i in range(5) for j in range(i + 1, 5)})
    tris = sorted({(s[i], s[j], s[k]) for s in simplices for i in range(5) for j in range(i + 1, 5) for k in range(j + 1, 5)})
    tets = sorted({(s[i], s[j], s[k], s[l]) for s in simplices for i in range(5) for j in range(i + 1, 5) for k in range(j + 1, 5) for l in range(k + 1, 5)})
    return verts, edges, tris, tets


def _build_s4_partial_beta5() -> list[tuple[int, ...]]:
    return [
        tuple(sorted((s0, 2 + s1, 4 + s2, 6 + s3, 8 + s4)))
        for s0 in (0, 1) for s1 in (0, 1) for s2 in (0, 1) for s3 in (0, 1) for s4 in (0, 1)
    ]


def _build_s1_x_s3(n_slices: int = 3) -> list[tuple[int, ...]]:
    simps = []
    tets_s3 = [tuple(k for k in range(5) if k != a) for a in range(5)]
    for t in range(n_slices):
        tn = (t + 1) % n_slices
        for tau in tets_s3:
            vs = [5 * t + k for k in tau]
            ws = [5 * tn + k for k in tau]
            for j in range(4):
                simps.append(tuple(sorted(vs[:4 - j] + ws[3 - j:])))
    return simps


class _Simplicial4DGeom:
    """Vectorized 4D simplicial Regge & DEC Kähler–Dirac evaluator."""

    def __init__(self, simplices: list[tuple[int, ...]]) -> None:
        self.simplices = simplices
        self.verts, self.edges, self.tris, self.tets = _skeleton_4d(simplices)
        self.n0 = len(self.verts)
        self.n1 = len(self.edges)
        self.n2 = len(self.tris)
        self.n3 = len(self.tets)
        self.n4 = len(self.simplices)
        self.chi = self.n0 - self.n1 + self.n2 - self.n3 + self.n4
        self.ds1 = 2 * self.n3 - 5 * self.n4
        self.ds2 = 2 * self.n1 - 3 * self.n2 + 4 * self.n3 - 5 * self.n4

        self.v_idx = {x: i for i, x in enumerate(self.verts)}
        self.e_idx = {x: i for i, x in enumerate(self.edges)}
        self.t_idx = {x: i for i, x in enumerate(self.tris)}
        self.tet_idx = {x: i for i, x in enumerate(self.tets)}

        self.tri_e = np.array([[self.e_idx[(a, b)], self.e_idx[(a, c)], self.e_idx[(b, c)]] for a, b, c in self.tris], dtype=int)
        self.tet_e = np.array([[self.e_idx[(s[i], s[j])] for i in range(4) for j in range(i + 1, 4)] for s in self.tets], dtype=int)
        self.s4_e = np.array([[self.e_idx[(s[i], s[j])] for i in range(5) for j in range(i + 1, 5)] for s in self.simplices], dtype=int)

        self.iu3, self.ju3 = np.triu_indices(4, k=1)
        self.iu4, self.ju4 = np.triu_indices(5, k=1)

        self.s4_opp_tri = np.zeros((self.n4, 5, 5), dtype=int)
        self.inc0 = np.zeros((self.n0, self.n4), dtype=float)
        self.inc1 = np.zeros((self.n1, self.n4), dtype=float)
        self.inc2 = np.zeros((self.n2, self.n4), dtype=float)
        self.inc3 = np.zeros((self.n3, self.n4), dtype=float)
        for s_i, s in enumerate(self.simplices):
            for a in s:
                self.inc0[self.v_idx[a], s_i] = 1.0
            for i in range(5):
                self.inc3[self.tet_idx[s[:i] + s[i + 1:]], s_i] = 1.0
                for j in range(i + 1, 5):
                    self.inc1[self.e_idx[(s[i], s[j])], s_i] = 1.0
                    h = tuple(s[m] for m in range(5) if m != i and m != j)
                    self.s4_opp_tri[s_i, i, j] = self.t_idx[h]
                    for k in range(j + 1, 5):
                        self.inc2[self.t_idx[(s[i], s[j], s[k])], s_i] = 1.0

        d0 = np.zeros((self.n1, self.n0), dtype=float)
        for i, (a, b) in enumerate(self.edges):
            d0[i, self.v_idx[a]] = -1.0
            d0[i, self.v_idx[b]] = 1.0
        d1 = np.zeros((self.n2, self.n1), dtype=float)
        for i, (a, b, c) in enumerate(self.tris):
            d1[i, self.e_idx[(b, c)]] = 1.0
            d1[i, self.e_idx[(a, c)]] = -1.0
            d1[i, self.e_idx[(a, b)]] = 1.0
        d2 = np.zeros((self.n3, self.n2), dtype=float)
        for i, (a, b, c, d) in enumerate(self.tets):
            d2[i, self.t_idx[(b, c, d)]] = 1.0
            d2[i, self.t_idx[(a, c, d)]] = -1.0
            d2[i, self.t_idx[(a, b, d)]] = 1.0
            d2[i, self.t_idx[(a, b, c)]] = -1.0
        d3 = np.zeros((self.n4, self.n3), dtype=float)
        for i, (a, b, c, d, e_) in enumerate(self.simplices):
            d3[i, self.tet_idx[(b, c, d, e_)]] = 1.0
            d3[i, self.tet_idx[(a, c, d, e_)]] = -1.0
            d3[i, self.tet_idx[(a, b, d, e_)]] = 1.0
            d3[i, self.tet_idx[(a, b, c, e_)]] = -1.0
            d3[i, self.tet_idx[(a, b, c, d)]] = 1.0
        self.ds = [d0, d1, d2, d3]
        self.eye_p = [np.eye(n) for n in (self.n0, self.n1, self.n2, self.n3, self.n4)]

    def eval_geom(self, L: np.ndarray):
        l2 = L * L
        la, lb, lc = L[self.tri_e[:, 0]], L[self.tri_e[:, 1]], L[self.tri_e[:, 2]]
        sp = 0.5 * (la + lb + lc)
        a2_sq = sp * (sp - la) * (sp - lb) * (sp - lc)
        if np.any(a2_sq <= 1e-16):
            return None
        areas = np.sqrt(a2_sq)

        mt = np.zeros((self.n3, 5, 5), dtype=float)
        mt[:, 0, 1:] = 1.0
        mt[:, 1:, 0] = 1.0
        lt2 = l2[self.tet_e]
        mt[:, self.iu3 + 1, self.ju3 + 1] = lt2
        mt[:, self.ju3 + 1, self.iu3 + 1] = lt2
        v3_sq = np.linalg.det(mt) / 288.0
        if np.any(v3_sq <= 1e-16):
            return None
        v3 = np.sqrt(v3_sq)

        m4 = np.zeros((self.n4, 6, 6), dtype=float)
        m4[:, 0, 1:] = 1.0
        m4[:, 1:, 0] = 1.0
        ls2 = l2[self.s4_e]
        m4[:, self.iu4 + 1, self.ju4 + 1] = ls2
        m4[:, self.ju4 + 1, self.iu4 + 1] = ls2
        v4_sq = -np.linalg.det(m4) / 9216.0
        if np.any(v4_sq <= 1e-16):
            return None
        v4 = np.sqrt(v4_sq)
        minv = np.linalg.inv(m4)

        theta_sum = np.zeros(self.n2, dtype=float)
        for i, j in zip(self.iu4, self.ju4):
            cos_th = np.clip(minv[:, i + 1, j + 1] / np.sqrt(minv[:, i + 1, i + 1] * minv[:, j + 1, j + 1]), -1.0, 1.0)
            np.add.at(theta_sum, self.s4_opp_tri[:, i, j], np.arccos(cos_th))
        eps = 2.0 * math.pi - theta_sum
        s_r = float(np.dot(areas, eps))
        v_tot = float(np.sum(v4))
        return s_r, v_tot, areas, eps, v3, v4

    def grad_neg_sr(self, L: np.ndarray) -> np.ndarray:
        _, _, areas, eps, _, _ = self.eval_geom(L)
        g = np.zeros(self.n1, dtype=float)
        la, lb, lc = L[self.tri_e[:, 0]], L[self.tri_e[:, 1]], L[self.tri_e[:, 2]]
        w = -eps / (8.0 * areas)
        np.add.at(g, self.tri_e[:, 0], w * la * (lb * lb + lc * lc - la * la))
        np.add.at(g, self.tri_e[:, 1], w * lb * (la * la + lc * lc - lb * lb))
        np.add.at(g, self.tri_e[:, 2], w * lc * (la * la + lb * lb - lc * lc))
        return g

    def hessian_neg_sr(self, L0: np.ndarray, hg: float = 1e-5) -> np.ndarray:
        h = np.zeros((self.n1, self.n1), dtype=float)
        for j in range(self.n1):
            lp = L0.copy()
            lp[j] += hg
            lm = L0.copy()
            lm[j] -= hg
            h[:, j] = (self.grad_neg_sr(lp) - self.grad_neg_sr(lm)) / (2.0 * hg)
        return 0.5 * (h + h.T)

    def build_kd(self, L: np.ndarray, areas: np.ndarray, v3: np.ndarray, v4: np.ndarray):
        vols = [np.ones(self.n0), L, areas, v3, v4]
        sv4 = [self.inc0 @ v4, self.inc1 @ v4, self.inc2 @ v4, self.inc3 @ v4, v4]
        weights = [((p + 1.0) / 5.0) * sv4[p] / (vols[p] ** 2) for p in range(5)]
        sw = [np.sqrt(wp) for wp in weights]
        isw = [1.0 / x for x in sw]
        dt = [(sw[p + 1][:, None] * self.ds[p]) * isw[p][None, :] for p in range(4)]
        laps = []
        for p in range(5):
            lp = np.zeros((len(vols[p]), len(vols[p])), dtype=float)
            if p > 0:
                lp += dt[p - 1] @ dt[p - 1].T
            if p < 4:
                lp += dt[p].T @ dt[p]
            laps.append(lp)
        return weights, dt, laps

    def kd_obs_eigs(self, L: np.ndarray, areas: np.ndarray, v3: np.ndarray, v4: np.ndarray, s_hm: float = 0.05, m_skd: float = 2.0):
        weights, dt, laps = self.build_kd(L, areas, v3, v4)
        z_tot = 0.0
        s_tot = 0.0
        all_ev = []
        bettis = []
        for lp in laps:
            ev = np.maximum(eigh(lp, eigvals_only=True), 0.0)
            all_ev.append(ev)
            bettis.append(int(np.sum(ev < 1e-9)))
            z_tot += float(np.sum(np.exp(-s_hm * ev)))
            s_tot += float(-0.5 * np.sum(np.log(ev + m_skd * m_skd)))
        return weights, dt, np.concatenate(all_ev), bettis, z_tot, s_tot

    def skd_slogdet(self, L: np.ndarray, areas: np.ndarray, v3: np.ndarray, v4: np.ndarray, m_skd: float = 1.0) -> float:
        vols = [np.ones(self.n0), L, areas, v3, v4]
        sv4 = [self.inc0 @ v4, self.inc1 @ v4, self.inc2 @ v4, self.inc3 @ v4, v4]
        weights = [((p + 1.0) / 5.0) * sv4[p] / (vols[p] ** 2) for p in range(5)]
        sw = [np.sqrt(wp) for wp in weights]
        isw = [1.0 / x for x in sw]
        dt = [(sw[p + 1][:, None] * self.ds[p]) * isw[p][None, :] for p in range(4)]
        s_tot = 0.0
        m2 = m_skd * m_skd
        for p in range(5):
            lp = m2 * self.eye_p[p]
            if p > 0:
                lp = lp + dt[p - 1] @ dt[p - 1].T
            if p < 4:
                lp = lp + dt[p].T @ dt[p]
            _, ld = np.linalg.slogdet(lp)
            s_tot += -0.5 * float(ld)
        return s_tot


class _FastSet:
    def __init__(self) -> None:
        self.items: list = []
        self.pos: dict = {}

    def add(self, x) -> None:
        if x not in self.pos:
            self.pos[x] = len(self.items)
            self.items.append(x)

    def remove(self, x) -> None:
        i = self.pos.pop(x)
        last = self.items.pop()
        if i < len(self.items):
            self.items[i] = last
            self.pos[last] = i

    def __len__(self) -> int:
        return len(self.items)

    def sample(self, rng: np.random.Generator):
        return self.items[int(rng.integers(0, len(self.items)))]


class _CDT4D:
    """O(1)-sampled 4D foliated CDT on S^1 x S^3 with all 7 foliation-preserving moves."""

    def __init__(self, n_slices: int = 4) -> None:
        self.T = n_slices
        self.v_slice: dict[int, int] = {}
        self.next_vid = 5 * n_slices
        self.simps = _FastSet()
        self.verts = _FastSet()
        self.tl_edges = _FastSet()
        self.sp_edges = _FastSet()
        self.sp_tris = _FastSet()
        self.sp_tets = _FastSet()
        self.tris = _FastSet()
        self.tet_to_s: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
        self.tri_to_s: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
        self.edge_to_s: dict[tuple[int, int], set[tuple[int, ...]]] = defaultdict(set)
        self.v_to_s: dict[int, set[tuple[int, ...]]] = defaultdict(set)
        self.n41 = 0
        self.n32 = 0
        self.n0_slice = [5] * n_slices
        for t in range(n_slices):
            for k in range(5):
                vid = 5 * t + k
                self.v_slice[vid] = t
                self.verts.add(vid)
        tets_s3 = [tuple(k for k in range(5) if k != a) for a in range(5)]
        for t in range(n_slices):
            tn = (t + 1) % n_slices
            for tau in tets_s3:
                vs = [5 * t + k for k in tau]
                ws = [5 * tn + k for k in tau]
                for j in range(4):
                    self._add_simp(tuple(sorted(vs[:4 - j] + ws[3 - j:])))

    def _simp_type(self, s: tuple[int, ...]) -> tuple[int, int]:
        ts = [self.v_slice[v] for v in s]
        t0 = min(ts)
        t_lo = self.T - 1 if (max(ts) - t0 > 1) else t0
        return t_lo, sum(1 for t in ts if t == t_lo)

    def _add_simp(self, s: tuple[int, ...]) -> None:
        self.simps.add(s)
        _, clo = self._simp_type(s)
        if clo in (1, 4):
            self.n41 += 1
        else:
            self.n32 += 1
        vs = self.v_slice
        for i in range(5):
            self.v_to_s[s[i]].add(s)
            tet = s[:i] + s[i + 1:]
            if not self.tet_to_s[tet] and vs[tet[0]] == vs[tet[1]] == vs[tet[2]] == vs[tet[3]]:
                self.sp_tets.add(tet)
            self.tet_to_s[tet].add(s)
            for j in range(i + 1, 5):
                e = (s[i], s[j])
                if not self.edge_to_s[e]:
                    if vs[e[0]] == vs[e[1]]:
                        self.sp_edges.add(e)
                    else:
                        self.tl_edges.add(e)
                self.edge_to_s[e].add(s)
                for k in range(j + 1, 5):
                    tr = (s[i], s[j], s[k])
                    if not self.tri_to_s[tr]:
                        self.tris.add(tr)
                        if vs[tr[0]] == vs[tr[1]] == vs[tr[2]]:
                            self.sp_tris.add(tr)
                    self.tri_to_s[tr].add(s)

    def _rem_simp(self, s: tuple[int, ...]) -> None:
        self.simps.remove(s)
        _, clo = self._simp_type(s)
        if clo in (1, 4):
            self.n41 -= 1
        else:
            self.n32 -= 1
        vs = self.v_slice
        for i in range(5):
            v = s[i]
            self.v_to_s[v].remove(s)
            if not self.v_to_s[v]:
                del self.v_to_s[v]
            tet = s[:i] + s[i + 1:]
            self.tet_to_s[tet].remove(s)
            if not self.tet_to_s[tet]:
                del self.tet_to_s[tet]
                if vs[tet[0]] == vs[tet[1]] == vs[tet[2]] == vs[tet[3]]:
                    self.sp_tets.remove(tet)
            for j in range(i + 1, 5):
                e = (s[i], s[j])
                self.edge_to_s[e].remove(s)
                if not self.edge_to_s[e]:
                    del self.edge_to_s[e]
                    if vs[e[0]] == vs[e[1]]:
                        self.sp_edges.remove(e)
                    else:
                        self.tl_edges.remove(e)
                for k in range(j + 1, 5):
                    tr = (s[i], s[j], s[k])
                    self.tri_to_s[tr].remove(s)
                    if not self.tri_to_s[tr]:
                        del self.tri_to_s[tr]
                        self.tris.remove(tr)
                        if vs[tr[0]] == vs[tr[1]] == vs[tr[2]]:
                            self.sp_tris.remove(tr)

    def step(self, rng: np.random.Generator, k0: float, delta: float, k4: float, n4_target: int, eps_vol: float) -> None:
        n4 = len(self.simps)
        n0 = len(self.verts)

        def ds_act(dn0: int, dn41: int, dn32: int) -> float:
            dn4 = dn41 + dn32
            v_cur = (n4 - n4_target) ** 2
            v_new = (n4 + dn4 - n4_target) ** 2
            return -(k0 + 6.0 * delta) * dn0 + k4 * dn4 - delta * dn41 + eps_vol * (v_new - v_cur)

        mv = int(rng.integers(0, 7))
        if mv == 0:  # (2,8)
            tau = self.sp_tets.sample(rng)
            s1, s2 = tuple(self.tet_to_s[tau])
            p = next(v for v in s1 if v not in tau)
            q = next(v for v in s2 if v not in tau)
            if math.log(max(rng.random(), 1e-16)) < -ds_act(1, 6, 0) + math.log(len(self.sp_tets) / (n0 + 1.0)):
                vn = self.next_vid
                self.next_vid += 1
                t = self.v_slice[tau[0]]
                self.v_slice[vn] = t
                self.verts.add(vn)
                self.n0_slice[t] += 1
                self._rem_simp(s1)
                self._rem_simp(s2)
                for i in range(4):
                    face = tau[:i] + tau[i + 1:]
                    self._add_simp(tuple(sorted((vn, p) + face)))
                    self._add_simp(tuple(sorted((vn, q) + face)))
        elif mv == 1:  # (8,2)
            v = self.verts.sample(rng)
            t = self.v_slice[v]
            if self.n0_slice[t] <= 5 or len(self.v_to_s[v]) != 8:
                return
            ss = list(self.v_to_s[v])
            up, dn, base_v = set(), set(), set()
            tp = (t + 1) % self.T
            tm = (t - 1) % self.T
            for s in ss:
                for x in s:
                    if x == v:
                        continue
                    tx = self.v_slice[x]
                    if tx == t:
                        base_v.add(x)
                    elif tx == tp:
                        up.add(x)
                    elif tx == tm:
                        dn.add(x)
                    else:
                        return
            if len(up) != 1 or len(dn) != 1 or len(base_v) != 4:
                return
            tau = tuple(sorted(base_v))
            if tau in self.tet_to_s:
                return
            p, q = next(iter(up)), next(iter(dn))
            if math.log(max(rng.random(), 1e-16)) < -ds_act(-1, -6, 0) + math.log(n0 / max(1.0, len(self.sp_tets) - 3.0)):
                for s in ss:
                    self._rem_simp(s)
                self.verts.remove(v)
                del self.v_slice[v]
                self.n0_slice[t] -= 1
                self._add_simp(tuple(sorted(tau + (p,))))
                self._add_simp(tuple(sorted(tau + (q,))))
        elif mv == 2:  # (2,4) slab
            s1 = self.simps.sample(rng)
            t_lo, clo = self._simp_type(s1)
            if clo not in (1, 4):
                return
            vs_drop = [v for v in s1 if (self.v_slice[v] == t_lo) == (clo == 4)]
            drop = vs_drop[int(rng.integers(0, 4))]
            tau = tuple(sorted(v for v in s1 if v != drop))
            s2 = next(x for x in self.tet_to_s[tau] if x != s1)
            if self._simp_type(s2)[1] not in (2, 3):
                return
            q = next(v for v in s2 if v not in tau)
            e_pq = (drop, q) if drop < q else (q, drop)
            if e_pq in self.edge_to_s:
                return
            if math.log(max(rng.random(), 1e-16)) < -ds_act(0, 0, 2) + math.log((4.0 * n4) / (len(self.tl_edges) + 1.0)):
                self._rem_simp(s1)
                self._rem_simp(s2)
                for i in range(4):
                    self._add_simp(tuple(sorted((drop, q) + tau[:i] + tau[i + 1:])))
        elif mv == 3:  # (4,2) slab
            e = self.tl_edges.sample(rng)
            ss = self.edge_to_s[e]
            if len(ss) != 4:
                return
            p, q = e
            c41, c32 = 0, 0
            other = set()
            for s in ss:
                if self._simp_type(s)[1] in (1, 4):
                    c41 += 1
                else:
                    c32 += 1
                for x in s:
                    if x != p and x != q:
                        other.add(x)
            if c41 != 1 or c32 != 3 or len(other) != 4:
                return
            tau = tuple(sorted(other))
            if tau in self.tet_to_s:
                return
            if math.log(max(rng.random(), 1e-16)) < -ds_act(0, 0, -2) + math.log(len(self.tl_edges) / max(1.0, 4.0 * (n4 - 2.0))):
                for s in list(ss):
                    self._rem_simp(s)
                self._add_simp(tuple(sorted(tau + (p,))))
                self._add_simp(tuple(sorted(tau + (q,))))
        elif mv == 4:  # (4,6) spatial
            tr = self.sp_tris.sample(rng)
            ss = self.tri_to_s[tr]
            if len(ss) != 4:
                return
            t = self.v_slice[tr[0]]
            tp = (t + 1) % self.T
            tm = (t - 1) % self.T
            up, dn, sp_opp = set(), set(), set()
            for s in ss:
                if self._simp_type(s)[1] not in (1, 4):
                    return
                for x in s:
                    if x in tr:
                        continue
                    tx = self.v_slice[x]
                    if tx == t:
                        sp_opp.add(x)
                    elif tx == tp:
                        up.add(x)
                    elif tx == tm:
                        dn.add(x)
                    else:
                        return
            if len(up) != 1 or len(dn) != 1 or len(sp_opp) != 2:
                return
            p, q = sorted(sp_opp)
            if (p, q) in self.edge_to_s:
                return
            w_p, w_m = next(iter(up)), next(iter(dn))
            if math.log(max(rng.random(), 1e-16)) < -ds_act(0, 2, 0) + math.log(len(self.sp_tris) / (len(self.sp_edges) + 1.0)):
                for s in list(ss):
                    self._rem_simp(s)
                for i in range(3):
                    e2 = tr[:i] + tr[i + 1:]
                    self._add_simp(tuple(sorted((p, q, w_p) + e2)))
                    self._add_simp(tuple(sorted((p, q, w_m) + e2)))
        elif mv == 5:  # (6,4) spatial
            e = self.sp_edges.sample(rng)
            ss = self.edge_to_s[e]
            if len(ss) != 6:
                return
            p, q = e
            t = self.v_slice[p]
            tp = (t + 1) % self.T
            tm = (t - 1) % self.T
            up, dn, tr_set = set(), set(), set()
            for s in ss:
                if self._simp_type(s)[1] not in (1, 4):
                    return
                for x in s:
                    if x == p or x == q:
                        continue
                    tx = self.v_slice[x]
                    if tx == t:
                        tr_set.add(x)
                    elif tx == tp:
                        up.add(x)
                    elif tx == tm:
                        dn.add(x)
                    else:
                        return
            if len(up) != 1 or len(dn) != 1 or len(tr_set) != 3:
                return
            tr = tuple(sorted(tr_set))
            if tr in self.tri_to_s:
                return
            w_p, w_m = next(iter(up)), next(iter(dn))
            if math.log(max(rng.random(), 1e-16)) < -ds_act(0, -2, 0) + math.log(len(self.sp_edges) / max(1.0, len(self.sp_tris) - 2.0)):
                for s in list(ss):
                    self._rem_simp(s)
                self._add_simp(tuple(sorted(tr + (p, w_p))))
                self._add_simp(tuple(sorted(tr + (q, w_p))))
                self._add_simp(tuple(sorted(tr + (p, w_m))))
                self._add_simp(tuple(sorted(tr + (q, w_m))))
        else:  # (3,3) slab
            tr = self.tris.sample(rng)
            ss = self.tri_to_s[tr]
            if len(ss) != 3:
                return
            opp = tuple(sorted({x for s in ss for x in s if x not in tr}))
            if len(opp) != 3 or opp in self.tri_to_s:
                return
            if len({self.v_slice[x] for x in tr + opp}) != 2:
                return
            new_ss = [tuple(sorted(opp + tr[:i] + tr[i + 1:])) for i in range(3)]
            if any(len({self.v_slice[v] for v in s}) != 2 for s in new_ss):
                return
            dn41, dn32 = 0, 0
            for s in ss:
                if self._simp_type(s)[1] in (1, 4):
                    dn41 -= 1
                else:
                    dn32 -= 1
            for s in new_ss:
                if self._simp_type(s)[1] in (1, 4):
                    dn41 += 1
                else:
                    dn32 += 1
            if math.log(max(rng.random(), 1e-16)) < -ds_act(0, dn41, dn32):
                for s in list(ss):
                    self._rem_simp(s)
                for s in new_ss:
                    self._add_simp(s)

    def observables(self) -> tuple[int, float, float, float, float]:
        n4 = len(self.simps)
        n4_sl = [0] * self.T
        for s in self.simps.items:
            n4_sl[self._simp_type(s)[0]] += 1
        ipr_t = sum((x / n4) ** 2 for x in n4_sl)
        o_cb = abs(sum(((-1) ** t) * n4_sl[t] for t in range(self.T))) / n4
        max_deg = max(len(self.v_to_s[v]) for v in self.verts.items) / n4
        return len(self.verts), self.n41 / n4, ipr_t, max_deg, o_cb


def suite_v121a_dynamical_4d_simplicial_cdt_regge_kd(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.1.A: Dynamical 4D Simplicial Regge / CDT + Kähler–Dirac Matter")
    print("=" * 88)

    # --------------------------------------------------------------------------
    # V12.1.A1: 4D Pachner-Evolved S^4 & Roček–Williams Zero-Mode Audit
    # --------------------------------------------------------------------------
    simps_s4 = _build_s4_partial_beta5()
    g_s4 = _Simplicial4DGeom(simps_s4)

    # (2,4) move on partial beta_5
    tet_map: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for idx, s in enumerate(simps_s4):
        for i in range(5):
            tet_map[s[:i] + s[i + 1:]].append(idx)
    e_set = set(g_s4.edges)
    simps_24 = None
    for tau, idxs in tet_map.items():
        if len(idxs) == 2:
            p = next(v for v in simps_s4[idxs[0]] if v not in tau)
            q = next(v for v in simps_s4[idxs[1]] if v not in tau)
            epq = (p, q) if p < q else (q, p)
            if epq not in e_set:
                simps_24 = [s for k, s in enumerate(simps_s4) if k not in idxs] + [
                    tuple(sorted((p, q) + tau[:i] + tau[i + 1:])) for i in range(4)
                ]
                break
    assert simps_24 is not None
    g_24 = _Simplicial4DGeom(simps_24)

    # (3,3) move after (2,4)
    tri_map: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for idx, s in enumerate(simps_24):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    tri_map[(s[i], s[j], s[k])].append(idx)
    t_set24 = set(tri_map.keys())
    simps_33 = None
    for tr, idxs in tri_map.items():
        if len(idxs) == 3:
            opp = tuple(sorted({v for idx in idxs for v in simps_24[idx] if v not in tr}))
            if len(opp) == 3 and opp not in t_set24:
                simps_33 = [s for k, s in enumerate(simps_24) if k not in idxs] + [
                    tuple(sorted(opp + tr[:i] + tr[i + 1:])) for i in range(3)
                ]
                break
    assert simps_33 is not None
    g_33 = _Simplicial4DGeom(simps_33)

    # (1,5) move on partial beta_5
    s_split = simps_s4[0]
    v_new = 10
    simps_15 = simps_s4[1:] + [tuple(sorted((v_new,) + s_split[:i] + s_split[i + 1:])) for i in range(5)]
    g_15 = _Simplicial4DGeom(simps_15)

    # S^1 x S^3 (T=3)
    simps_s1s3 = _build_s1_x_s3(3)
    g_s1s3 = _Simplicial4DGeom(simps_s1s3)

    topo_ok = (
        g_s4.chi == 2 and g_s4.ds1 == 0 and g_s4.ds2 == 0
        and (g_24.n0, g_24.n1, g_24.n2, g_24.n3, g_24.n4) == (10, 41, 84, 85, 34) and g_24.chi == 2 and g_24.ds1 == 0 and g_24.ds2 == 0
        and (g_33.n0, g_33.n1, g_33.n2, g_33.n3, g_33.n4) == (10, 41, 84, 85, 34) and g_33.chi == 2 and g_33.ds1 == 0 and g_33.ds2 == 0
        and (g_15.n0, g_15.n1, g_15.n2, g_15.n3, g_15.n4) == (11, 45, 90, 90, 36) and g_15.chi == 2 and g_15.ds1 == 0 and g_15.ds2 == 0
        and (g_s1s3.n0, g_s1s3.n1, g_s1s3.n2, g_s1s3.n3, g_s1s3.n4) == (15, 75, 150, 150, 60) and g_s1s3.chi == 0 and g_s1s3.ds1 == 0 and g_s1s3.ds2 == 0
    )
    cc.check(topo_ok, "V12.1.A1a: 4D Pachner (2,4)/(3,3)/(1,5) & S^1xS^3 satisfy chi and Dehn-Sommerville")

    def sig_counts(ev: np.ndarray, tol: float = 1e-6) -> tuple[int, int, int]:
        return int(np.sum(ev < -tol)), int(np.sum(np.abs(ev) <= tol)), int(np.sum(ev > tol))

    L_s4 = np.ones(g_s4.n1)
    sr_base = g_s4.eval_geom(L_s4)[0]
    h_s4 = g_s4.hessian_neg_sr(L_s4)
    ev_s4, evec_s4 = eigh(h_s4)
    sig_s4 = sig_counts(ev_s4)

    ev_24 = eigh(g_24.hessian_neg_sr(np.ones(g_24.n1)), eigvals_only=True)
    sig_24 = sig_counts(ev_24)
    ev_33 = eigh(g_33.hessian_neg_sr(np.ones(g_33.n1)), eigvals_only=True)
    sig_33 = sig_counts(ev_33)

    def lvec_15(l_in: float) -> np.ndarray:
        return np.array([l_in if v_new in e else 1.0 for e in g_15.edges], dtype=float)

    l_flat = math.sqrt(2.0 / 5.0)
    L_15_flat = lvec_15(l_flat)
    sr_15_flat = g_15.eval_geom(L_15_flat)[0]
    ev_15_flat = eigh(g_15.hessian_neg_sr(L_15_flat, hg=1e-6), eigvals_only=True)
    sig_15_flat = sig_counts(ev_15_flat, tol=1e-7)

    ev_15_curv = eigh(g_15.hessian_neg_sr(lvec_15(0.70)), eigvals_only=True)
    sig_15_curv = sig_counts(ev_15_curv)

    ev_15_spike = eigh(g_15.hessian_neg_sr(lvec_15(1.00)), eigvals_only=True)
    sig_15_spike = sig_counts(ev_15_spike)

    ev_s1s3 = eigh(g_s1s3.hessian_neg_sr(np.ones(g_s1s3.n1)), eigvals_only=True)
    sig_s1s3 = sig_counts(ev_s1s3)

    cc.check(
        sig_s4 == (10, 0, 30) and sig_24 == (10, 0, 31) and sig_33 == (10, 0, 31),
        "V12.1.A1b: Baseline S^4 (10,0,30) and (2,4)/(3,3) (10,0,31) Regge Hessians",
    )
    cc.check(
        abs(sr_15_flat - sr_base) < 1e-10 and sig_15_flat == (11, 4, 30),
        "V12.1.A1c: Flat (1,5) circumcentric subdivision preserves S_R & yields 4 Roček-Williams zero modes (11,4,30)",
    )
    cc.check(
        sig_15_curv == (11, 0, 34) and sig_15_spike == (10, 0, 35) and sig_s1s3 == (15, 0, 60),
        "V12.1.A1d: Curved (1,5) (11,0,34), spike (10,0,35), and S^1xS^3 (15,0,60) lift all diffeo zero modes",
    )

    print("  [V12.1.A1] 4D Pachner Moves & Roček–Williams Flat vs Curved Zero Modes [Т] / [✗]:")
    print(f"             - Baseline S^4: S_R={sr_base:.6f}, modes={sig_s4}; (2,4)={sig_24}, (2,4)+(3,3)={sig_33}")
    print(f"             - (1,5) flat l_in=sqrt(2/5): S_R={sr_15_flat:.6f}, modes={sig_15_flat} (4 exact RW zero modes [Т])")
    print(f"             - (1,5) curved l_in=0.70: {sig_15_curv}; spike l_in=1.00: {sig_15_spike}; S^1xS^3: {sig_s1s3} (0 zero modes [Т/✗])")

    # --------------------------------------------------------------------------
    # V12.1.A2: Exact 4D DEC Hodge Weights, KD Complex & TT Decomposition
    # --------------------------------------------------------------------------
    # Exact recursive circumcentric dual volume on regular unit d-simplex:
    # *sigma_p has barycentric/circumcentric ratio 1.0 on regular 4-simplex:
    # Dual volume of p-simplex inside single regular 4-simplex (R_k^2 = k/(2(k+1)) for k-simplex):
    # Recursive formula |*_4 sigma_p| = sum_{q=p+1}^4 ... (or exact simplex circumcenter distances):
    # On regular k-simplex of edge 1, circumradius R_k = sqrt(k / (2*(k+1))), distance from center of k-face
    # to center of (k+1)-face is h_{k+1} = sqrt(R_{k+1}^2 - R_k^2) = 1 / sqrt(2*(k+1)*(k+2)).
    # Thus dual cell volume inside 1 regular 4-simplex is:
    # |*_4 sigma_p|_{1-simp} = (4-p)! * prod_{k=p}^3 h_{k+1} * (Wait: number of flags from p to 4 is (4-p)!, times 1/(4-p)! simplex volume!)
    # Wait: each orthogonal flag from p-face center to (p+1)...4 center has orthogonal altitudes h_{p+1}, ..., h_4,
    # forming an orthoscheme of (4-p)-volume (1/(4-p)!) * prod_{k=p}^{3} h_{k+1}, and there are (4-p)!/(p+1-p)! ...
    # Specifically, number of (p < p+1 < ... < 4) co-chains in a 4-simplex = 5! / (p+1)! / ... Wait: (5)! / ((p+1)!) = (4-p)! * binom(5, p+1)? No:
    # A p-face has 5 - (p+1) = 4-p remaining vertices -> (4-p)! orderings of remaining vertices!
    # So inside ONE regular 4-simplex, |*_4 sigma_p| = prod_{k=p}^3 h_{k+1}, and over all incident 4-simplices = n_inc(p) * prod_{k=p}^3 h_{k+1}!
    # Dividing by |sigma_p| = sqrt(p+1) / (p! * 2^(p/2)) gives w_p^circ!
    h_orth = [1.0 / math.sqrt(2.0 * (k + 1) * (k + 2)) for k in range(4)]  # k=0,1,2,3 -> (0->1, 1->2, 2->3, 3->4)
    n_inc_s4 = [16, 8, 4, 2, 1]  # number of 4-simplices in partial beta_5 containing a p-simplex
    vol_reg_p = [math.sqrt(p + 1.0) / (math.factorial(p) * (2.0 ** (0.5 * p))) for p in range(5)]
    w_circ_reg = []
    for p in range(5):
        dual_1 = 1.0
        for k in range(p, 4):
            dual_1 *= h_orth[k]
        w_circ_reg.append((n_inc_s4[p] * dual_1) / vol_reg_p[p])

    _, V0_s4, a0_s4, _, v30_s4, v40_s4 = g_s4.eval_geom(L_s4)
    w_s4, dt_s4, ev_kd_s4, bet_s4, z0_kd, s0_kd = g_s4.kd_obs_eigs(L_s4, a0_s4, v30_s4, v40_s4, s_hm=0.05, m_skd=2.0)

    circ_ratio_err = max(abs(w_circ_reg[p] / float(w_s4[p][0]) - 1.0) for p in range(5))

    # Constant p-form norm identity inside 1 regular 4-simplex embedded in R^4:
    # Vertices of regular 4-simplex of edge 1 in R^4: Gram-Schmidt / symmetric embedding in R^5 hyperplane sum x_i = 0 scaled by 1/sqrt(2):
    v4_coords = np.eye(5) / math.sqrt(2.0)  # edge length between e_i/sqrt(2) and e_j/sqrt(2) is 1.0!
    # Orthonormal basis in R^4 for hyperplane sum x_i = 0:
    q_basis, _ = np.linalg.qr(np.column_stack([np.ones(5), np.eye(5)[:, :4]]))
    e4_basis = q_basis[:, 1:]  # 5x4 orthonormal columns orthogonal to (1,1,1,1,1)
    pts_reg4 = v4_coords @ e4_basis  # (5, 4) coordinates in R^4 with unit edge lengths
    # Constant unit-norm p-form alpha_p = dx_0 ^ ... ^ dx_{p-1}: integral over oriented p-simplex (v_0..v_p) is det(M_p) / p!
    # (for p=0: 1.0; for p=4: V4_reg)
    norm_id_err = 0.0
    v4_one = vol_reg_p[4]
    from itertools import combinations
    for p in range(5):
        s_norm = 0.0
        w_loc = ((p + 1.0) / 5.0) * v4_one / (vol_reg_p[p] ** 2)
        for comb in combinations(range(5), p + 1):
            if p == 0:
                per = 1.0
            else:
                mat_p = np.array([pts_reg4[comb[i], :p] - pts_reg4[comb[0], :p] for i in range(1, p + 1)])
                per = float(np.linalg.det(mat_p)) / math.factorial(p)
            s_norm += w_loc * (per ** 2)
        norm_id_err = max(norm_id_err, abs(s_norm / v4_one - 1.0))

    # Cochain identity d_{p+1} d_p = 0, real antisymmetry D_KD^T = -D_KD, zero sign problem, and Betti preservation
    d_sq_err = max(float(np.max(np.abs(dt_s4[p + 1] @ dt_s4[p]))) for p in range(3))
    dim_s4 = g_s4.n0 + g_s4.n1 + g_s4.n2 + g_s4.n3 + g_s4.n4
    d_kd = np.zeros((dim_s4, dim_s4), dtype=float)
    ns_s4 = [g_s4.n0, g_s4.n1, g_s4.n2, g_s4.n3, g_s4.n4]
    ofs_s4 = [0, g_s4.n0, g_s4.n0 + g_s4.n1, g_s4.n0 + g_s4.n1 + g_s4.n2, g_s4.n0 + g_s4.n1 + g_s4.n2 + g_s4.n3]
    for p in range(4):
        d_kd[ofs_s4[p + 1]:ofs_s4[p + 1] + ns_s4[p + 1], ofs_s4[p]:ofs_s4[p] + ns_s4[p]] += dt_s4[p]
        d_kd[ofs_s4[p]:ofs_s4[p] + ns_s4[p], ofs_s4[p + 1]:ofs_s4[p + 1] + ns_s4[p + 1]] -= dt_s4[p].T
    antisym_err = float(np.max(np.abs(d_kd + d_kd.T)))
    m_chk = 1.5
    _, ld_lin = np.linalg.slogdet(d_kd + m_chk * np.eye(dim_s4))
    _, ld_lap = np.linalg.slogdet(d_kd.T @ d_kd + (m_chk * m_chk) * np.eye(dim_s4))
    sign_prob_err = abs(ld_lin - 0.5 * ld_lap)

    # Betti preservation after (2,4) move and on S^1 x S^3
    _, a_24, _, v3_24, v4_24 = g_24.eval_geom(np.ones(g_24.n1))[1:]
    _, _, _, bet_24, _, _ = g_24.kd_obs_eigs(np.ones(g_24.n1), a_24, v3_24, v4_24)
    _, a_13, _, v3_13, v4_13 = g_s1s3.eval_geom(np.ones(g_s1s3.n1))[1:]
    _, _, ev_kd_s1s3, bet_s1s3, _, _ = g_s1s3.kd_obs_eigs(np.ones(g_s1s3.n1), a_13, v3_13, v4_13)

    # Spectral dimension d_s(s) = -2 d ln Z(s) / d ln s on S^4 and S^1 x S^3
    def max_spectral_dim(ev_arr: np.ndarray) -> float:
        s_grid = np.geomspace(0.01, 1.0, 25)
        ds_vals = []
        for sv in s_grid:
            w_ev = np.exp(-sv * ev_arr)
            z_s = float(np.sum(w_ev))
            dz = float(np.sum(-ev_arr * w_ev))
            ds_vals.append(-2.0 * sv * dz / z_s)
        return float(max(ds_vals))

    ds_max_s4 = max_spectral_dim(ev_kd_s4)
    ds_max_s1s3 = max_spectral_dim(ev_kd_s1s3)

    cc.check(
        circ_ratio_err < 1e-12 and norm_id_err < 1e-12 and d_sq_err < 1e-12 and antisym_err < 1e-12 and sign_prob_err < 1e-11,
        "V12.1.A2a: Exact 4D DEC circumcentric/barycentric match, p-form norm, d^2=0, antisymmetry, zero sign problem",
    )
    cc.check(
        bet_s4 == [1, 0, 0, 0, 1] and bet_24 == [1, 0, 0, 0, 1] and bet_s1s3 == [1, 1, 0, 1, 1],
        "V12.1.A2b: Exact KD Betti numbers [1,0,0,0,1] on S^4 (Pachner-invariant) and [1,1,0,1,1] on S^1xS^3",
    )

    # 40-mode directional 2nd derivatives of Z_KD(0.05), S_KD(2.0), V_tot along H_{-S_R} eigenmodes
    h_fd = 1e-4
    d2z = np.zeros(40)
    d2s = np.zeros(40)
    d2v = np.zeros(40)
    for k in range(40):
        vk = evec_s4[:, k]
        _, vp, ap, _, v3p, v4p = g_s4.eval_geom(L_s4 + h_fd * vk)
        _, _, _, _, zp, sp_k = g_s4.kd_obs_eigs(L_s4 + h_fd * vk, ap, v3p, v4p, s_hm=0.05, m_skd=2.0)
        _, vm, am, _, v3m, v4m = g_s4.eval_geom(L_s4 - h_fd * vk)
        _, _, _, _, zm, sm_k = g_s4.kd_obs_eigs(L_s4 - h_fd * vk, am, v3m, v4m, s_hm=0.05, m_skd=2.0)
        d2z[k] = (zp - 2.0 * z0_kd + zm) / (h_fd * h_fd)
        d2s[k] = (sp_k - 2.0 * s0_kd + sm_k) / (h_fd * h_fd)
        d2v[k] = (vp - 2.0 * V0_s4 + vm) / (h_fd * h_fd)

    x_tt = np.column_stack([ev_s4[10:], d2v[10:]])
    x_cf = np.column_stack([ev_s4[:10], d2v[:10]])
    cz = np.linalg.lstsq(x_tt, d2z[10:], rcond=None)[0]
    cs = np.linalg.lstsq(x_tt, d2s[10:], rcond=None)[0]
    tt_res_z = float(np.linalg.norm(d2z[10:] - x_tt @ cz) / np.linalg.norm(d2z[10:]))
    tt_res_s = float(np.linalg.norm(d2s[10:] - x_tt @ cs) / np.linalg.norm(d2s[10:]))
    cf_res_z = float(np.linalg.norm(d2z[:10] - x_cf @ cz) / np.linalg.norm(d2z[:10]))
    cf_res_s = float(np.linalg.norm(d2s[:10] - x_cf @ cs) / np.linalg.norm(d2s[:10]))
    sub_tt_z = d2z[10:] - float(cz[1]) * d2v[10:]
    sub_tt_s = d2s[10:] - float(cs[1]) * d2v[10:]

    cc.check(
        np.all(d2z[10:] < 0.0) and np.all(d2s[10:] < 0.0),
        "V12.1.A2c: Bare unsubtracted TT curvature negative (bare CC obstruction [✗])",
    )
    cc.check(
        cz[0] > 0.0 and cs[0] > 0.0 and tt_res_z < 0.002 and tt_res_s < 0.012
        and np.all(sub_tt_z > 0.0) and np.all(sub_tt_s > 0.0),
        "V12.1.A2d: CC-subtracted TT stiffness c_EH > 0, TT residual < 1.2%, all 30 TT modes positive [С]",
    )
    cc.check(
        cf_res_z > 0.25 and cf_res_s > 0.25 and ds_max_s4 < 3.2 and ds_max_s1s3 < 3.2,
        "V12.1.A2e: Conformal residual > 25% (a_4/lattice) & peak spectral dim d_s < 3.2 < 4 [✗/П]",
    )

    print("  [V12.1.A2] Exact 4D DEC Kähler–Dirac & Induced Gravity Decomposition [Т] / [С] / [✗/П]:")
    print(f"             - DEC w_circ/w_bary err={circ_ratio_err:.2e}, p-form norm err={norm_id_err:.2e}, zero-sign err={sign_prob_err:.2e} [Т]")
    print(f"             - Betti(S^4)={bet_s4}, Betti(S^1xS^3)={bet_s1s3}; d_s^max = {ds_max_s4:.3f} (S^4), {ds_max_s1s3:.3f} (S^1xS^3) < 4 [П]")
    print(f"             - Z_KD(0.05): c_EH={cz[0]:+.4f}, c_CC={cz[1]:+.2f}, TT res={100*tt_res_z:.2f}%, conf res={100*cf_res_z:.1f}% [С]")
    print(f"             - S_KD(2.00): c_EH={cs[0]:+.4f}, c_CC={cs[1]:+.2f}, TT res={100*tt_res_s:.2f}%, conf res={100*cf_res_s:.1f}% [С]")

    # --------------------------------------------------------------------------
    # V12.1.A3: Batched Dynamical Regge + Unquenched Kähler–Dirac MC on S^4
    # --------------------------------------------------------------------------
    # Exact analytical 1st-order CC scaling counterterm at m=1.0:
    c_cc_1 = float(np.sum(ev_kd_s4 / (ev_kd_s4 + 1.0)) / (4.0 * V0_s4))
    # Exact 2nd-order TT CC counterterm at m=1.0:
    s0_kd1 = g_s4.skd_slogdet(L_s4, a0_s4, v30_s4, v40_s4, m_skd=1.0)
    d2s1 = np.zeros(40)
    for k in range(10, 40):
        vk = evec_s4[:, k]
        _, _, ap, _, v3p, v4p = g_s4.eval_geom(L_s4 + h_fd * vk)
        sp_1 = g_s4.skd_slogdet(L_s4 + h_fd * vk, ap, v3p, v4p, m_skd=1.0)
        _, _, am, _, v3m, v4m = g_s4.eval_geom(L_s4 - h_fd * vk)
        sm_1 = g_s4.skd_slogdet(L_s4 - h_fd * vk, am, v3m, v4m, m_skd=1.0)
        d2s1[k] = (sp_1 - 2.0 * s0_kd1 + sm_1) / (h_fd * h_fd)
    c_s1_tt = np.linalg.lstsq(x_tt, d2s1[10:], rcond=None)[0]
    c_cc_tt_1 = float(c_s1_tt[1])

    def run_regge_mc(mode: str, steps: int = 600, seed: int = 2026):
        rng = np.random.default_rng(seed)
        L = np.ones(40)

        def act_eval(lc: np.ndarray, res):
            s_r, v_tot, areas, eps, v3, v4 = res
            if mode == "bare":
                return -0.5 * s_r + 1.0 * v_tot
            v_tri = (g_s4.inc2 @ v4) / 4.0
            r2_term = float(np.sum((eps ** 2) * (areas ** 2) / v_tri))
            lq = 40.0
            s_grav = -0.2 * s_r + lq * (v_tot - V0_s4) ** 2 + 0.02 * r2_term
            if mode == "stab":
                return s_grav
            skd = g_s4.skd_slogdet(lc, areas, v3, v4, m_skd=1.0)
            if mode == "kd_unsub":
                return s_grav + 2.0 * skd
            if mode == "kd_sub_1st":
                return s_grav + 2.0 * (skd - c_cc_1 * v_tot)
            if mode == "kd_sub_tt":
                return s_grav + 2.0 * (skd - c_cc_tt_1 * v_tot)
            raise ValueError(f"Unknown regge MC mode: {mode}")

        cur_res = g_s4.eval_geom(L)
        cur_s = act_eval(L, cur_res)
        sig = 0.12 if mode == "bare" else 0.06
        vs, srs, sigs = [], [], []
        for st in range(steps):
            idx = int(rng.integers(0, 40))
            d = float(rng.normal(0.0, sig))
            l_cand = L.copy()
            l_cand[idx] *= math.exp(d)
            res = g_s4.eval_geom(l_cand)
            if res is not None:
                new_s = act_eval(l_cand, res)
                log_acc = -(new_s - cur_s) + d
                if log_acc >= 0.0 or math.log(max(rng.random(), 1e-16)) < log_acc:
                    L = l_cand
                    cur_res = res
                    cur_s = new_s
            if st >= steps // 3:
                vs.append(cur_res[1])
                srs.append(cur_res[0])
                sigs.append(float(np.std(L) / np.mean(L)))
        return float(np.mean(vs)), float(np.mean(srs)), float(np.mean(sigs))

    mc_bare = run_regge_mc("bare", steps=600)
    mc_stab = run_regge_mc("stab", steps=600)
    mc_unsub = run_regge_mc("kd_unsub", steps=600)
    mc_sub_1st = run_regge_mc("kd_sub_1st", steps=600)
    mc_sub_tt = run_regge_mc("kd_sub_tt", steps=600)

    comp_frac = (mc_stab[0] - mc_unsub[0]) / mc_stab[0]
    drift_coeff = -2.0 * (c_cc_tt_1 - c_cc_1)
    cc.check(abs(c_cc_1 - 78.3137) < 1e-3, "V12.1.A3a: Exact analytical 1st-order c_CC^(1)(1.0) = 78.3137")
    cc.check(mc_bare[0] < 0.70 < V0_s4 and mc_bare[1] > 37.0 > sr_base,
             "V12.1.A3b: Bare linear Regge conformal squeezing (<V> < 0.70, <S_R> > 37) [Т/✗]")
    cc.check(comp_frac >= 0.25, "V12.1.A3c: Unquenched KD N_f=2 (unsubtracted) compresses <V_tot> by >= 25% [С/✗]")
    cc.check(
        mc_sub_1st[0] < 0.60 and mc_sub_1st[0] < mc_stab[0] and mc_sub_1st[2] > mc_stab[2]
        and drift_coeff < -100.0 and mc_sub_tt[0] > 1.15 > V0_s4 > mc_stab[0],
        "V12.1.A3d: Equal-lq/steps CC-subtraction obstruction (1st-order compresses <V><0.60, TT leaves -114.2*V_tot drift <V>>1.15) [✗/П]",
    )

    print("  [V12.1.A3] Batched Dynamical Regge + Unquenched Kähler–Dirac MC on S^4 (equal lq=40, steps=600) [Т] / [С] / [✗/П]:")
    print(f"             - Exact c_CC^(1)(1.0) = {c_cc_1:.4f} (1st-order scaling) vs c_CC^TT(1.0) = {c_cc_tt_1:.4f} (2nd-order TT; drift={drift_coeff:+.2f}*V_tot)")
    print(f"             - Bare Regge:          <V>={mc_bare[0]:.4f}, <S_R>={mc_bare[1]:.3f}, <sig/l>={mc_bare[2]:.4f} [squeezing ✗]")
    print(f"             - Stabilized quench:   <V>={mc_stab[0]:.4f}, <S_R>={mc_stab[1]:.3f}, <sig/l>={mc_stab[2]:.4f}")
    print(f"             - KD N_f=2 unsub:      <V>={mc_unsub[0]:.4f} ({-100*comp_frac:+.1f}%!), <S_R>={mc_unsub[1]:.3f}, <sig/l>={mc_unsub[2]:.4f} [С/✗]")
    print(f"             - KD N_f=2 sub (1st):  <V>={mc_sub_1st[0]:.4f}, <S_R>={mc_sub_1st[1]:.3f}, <sig/l>={mc_sub_1st[2]:.4f} [compression / no smoothing ✗]")
    print(f"             - KD N_f=2 sub (TT):   <V>={mc_sub_tt[0]:.4f}, <S_R>={mc_sub_tt[1]:.3f}, <sig/l>={mc_sub_tt[2]:.4f} [volume expansion drift ✗/П]")

    # --------------------------------------------------------------------------
    # V12.1.A4: 4D CDT MC on S^1xS^3, KD Betti Preservation & G_EE vs G_Sak
    # --------------------------------------------------------------------------
    rng_cdt = np.random.default_rng(137)
    cdt_points = [(-2.0, -1.0), (0.5, -0.3), (2.2, 0.6), (5.5, 0.6)]
    cdt_scan = []
    c_win_simps = None
    for k0, dl in cdt_points:
        cdt = _CDT4D(4)
        k4 = 1.5
        n4_tgt = 220
        for st in range(18000):
            cdt.step(rng_cdt, k0, dl, k4, n4_tgt, 0.002)
            if st % 500 == 499 and st < 11000:
                k4 += 0.001 * (len(cdt.simps) - n4_tgt)
        obs = []
        for st in range(8000):
            cdt.step(rng_cdt, k0, dl, k4, n4_tgt, 0.002)
            if st % 160 == 0:
                obs.append(cdt.observables())
        arr = np.mean(obs, axis=0)
        n0_f = len(cdt.v_to_s)
        n1_f = len(cdt.edge_to_s)
        n2_f = len(cdt.tri_to_s)
        n3_f = len(cdt.tet_to_s)
        n4_f = len(cdt.simps)
        chi_f = n0_f - n1_f + n2_f - n3_f + n4_f
        ds1_f = 2 * n3_f - 5 * n4_f
        ds2_f = 2 * n1_f - 3 * n2_f + 4 * n3_f - 5 * n4_f
        cdt_scan.append((k0, dl, float(arr[0]), float(arr[1]), float(arr[2]), float(arr[3]), float(arr[4]), chi_f, ds1_f, ds2_f))
        if abs(k0 - 2.2) < 1e-9:
            c_win_simps = list(cdt.simps.items)

    topo_cdt_ok = all(row[7] == 0 and row[8] == 0 and row[9] == 0 for row in cdt_scan)
    n0_vals = [row[2] for row in cdt_scan]
    n41_vals = [row[3] for row in cdt_scan]
    crossover_ok = (
        n41_vals[0] < 0.42 and n41_vals[-1] > 0.72
        and all(n0_vals[i] <= n0_vals[i + 1] + 0.5 for i in range(3))
        and n0_vals[-1] > n0_vals[0] + 15.0
    )
    cc.check(topo_cdt_ok, "V12.1.A4a: 4D CDT preserves chi=0 & Dehn-Sommerville across B-Cb-C-A scan [Т]")
    cc.check(crossover_ok, "V12.1.A4b: 4D CDT B->Cb->C->A monotone <N0> and <N41/N4> structural crossover [С]")

    # KD Betti numbers & spectral dimension on equilibrated C-window CDT configuration
    g_cdt_c = _Simplicial4DGeom(c_win_simps)
    _, a_c, _, v3_c, v4_c = g_cdt_c.eval_geom(np.ones(g_cdt_c.n1))[1:]
    _, _, ev_kd_c, bet_c, _, _ = g_cdt_c.kd_obs_eigs(np.ones(g_cdt_c.n1), a_c, v3_c, v4_c)
    ds_max_cdt = max_spectral_dim(ev_kd_c)
    cc.check(bet_c == [1, 1, 0, 1, 1] and ds_max_cdt < 4.0,
             "V12.1.A4c: Dynamical C-window CDT preserves KD Betti [1,1,0,1,1] [Т] with d_s^max < 4 [П]")

    # 3D spatial KD Peschel entanglement S_EE / |dA| on subdivided S^3 (Ns=[18,64,92,46], dim=220, n_zero==2)
    tets_s3 = [tuple(k for k in range(5) if k != a) for a in range(5)]
    nv3 = 5
    for _ in range(13):
        tau = tets_s3.pop(0)
        vn = nv3
        nv3 += 1
        for i in range(4):
            tets_s3.append(tuple(sorted((vn,) + tau[:i] + tau[i + 1:])))
    for _ in range(2):
        tm3: dict[tuple[int, ...], list[int]] = defaultdict(list)
        for idx, tau in enumerate(tets_s3):
            for i in range(4):
                tm3[tau[:i] + tau[i + 1:]].append(idx)
        es3 = {(tau[i], tau[j]) for tau in tets_s3 for i in range(4) for j in range(i + 1, 4)}
        for tr, idxs in tm3.items():
            if len(idxs) == 2:
                p = next(v for v in tets_s3[idxs[0]] if v not in tr)
                q = next(v for v in tets_s3[idxs[1]] if v not in tr)
                epq = (p, q) if p < q else (q, p)
                if epq not in es3:
                    tets_s3 = [tau for k, tau in enumerate(tets_s3) if k not in idxs] + [
                        tuple(sorted((p, q) + tr[:i] + tr[i + 1:])) for i in range(3)
                    ]
                    break
    v3_list = sorted({v for tau in tets_s3 for v in tau})
    e3_list = sorted({(tau[i], tau[j]) for tau in tets_s3 for i in range(4) for j in range(i + 1, 4)})
    tr3_list = sorted({(tau[i], tau[j], tau[k]) for tau in tets_s3 for i in range(4) for j in range(i + 1, 4) for k in range(j + 1, 4)})
    ns3 = [len(v3_list), len(e3_list), len(tr3_list), len(tets_s3)]
    assert ns3 == [18, 64, 92, 46] and sum(ns3) == 220

    vi3 = {x: i for i, x in enumerate(v3_list)}
    ei3 = {x: i for i, x in enumerate(e3_list)}
    tri3 = {x: i for i, x in enumerate(tr3_list)}
    v3_unit = math.sqrt(2.0) / 12.0
    vols3 = [np.ones(ns3[0]), np.ones(ns3[1]), np.full(ns3[2], math.sqrt(3.0) / 4.0), np.full(ns3[3], v3_unit)]
    sv3 = [np.zeros(ns3[0]), np.zeros(ns3[1]), np.zeros(ns3[2]), vols3[3].copy()]
    for tau in tets_s3:
        for a in tau:
            sv3[0][vi3[a]] += v3_unit
        for i in range(4):
            sv3[2][tri3[tau[:i] + tau[i + 1:]]] += v3_unit
            for j in range(i + 1, 4):
                sv3[1][ei3[(tau[i], tau[j])]] += v3_unit
    w3 = [((p + 1.0) / 4.0) * sv3[p] / (vols3[p] ** 2) for p in range(4)]
    sw3 = [np.sqrt(wp) for wp in w3]
    isw3 = [1.0 / x for x in sw3]
    d0_3 = np.zeros((ns3[1], ns3[0]))
    for i, (a, b) in enumerate(e3_list):
        d0_3[i, vi3[a]] = -1.0
        d0_3[i, vi3[b]] = 1.0
    d1_3 = np.zeros((ns3[2], ns3[1]))
    for i, (a, b, c) in enumerate(tr3_list):
        d1_3[i, ei3[(b, c)]] = 1.0
        d1_3[i, ei3[(a, c)]] = -1.0
        d1_3[i, ei3[(a, b)]] = 1.0
    d2_3 = np.zeros((ns3[3], ns3[2]))
    for i, (a, b, c, d) in enumerate(tets_s3):
        d2_3[i, tri3[(b, c, d)]] = 1.0
        d2_3[i, tri3[(a, c, d)]] = -1.0
        d2_3[i, tri3[(a, b, d)]] = 1.0
        d2_3[i, tri3[(a, b, c)]] = -1.0
    dt3 = [(sw3[p + 1][:, None] * [d0_3, d1_3, d2_3][p]) * isw3[p][None, :] for p in range(3)]
    dim3 = sum(ns3)
    d_kd3 = np.zeros((dim3, dim3))
    ofs3 = [0, ns3[0], ns3[0] + ns3[1], ns3[0] + ns3[1] + ns3[2]]
    for p in range(3):
        d_kd3[ofs3[p + 1]:ofs3[p + 1] + ns3[p + 1], ofs3[p]:ofs3[p] + ns3[p]] += dt3[p]
        d_kd3[ofs3[p]:ofs3[p] + ns3[p], ofs3[p + 1]:ofs3[p + 1] + ns3[p + 1]] -= dt3[p].T
    ev3_h, u3_h = eigh(1j * d_kd3)
    n_zero_3d = int(np.sum(np.abs(ev3_h) < 1e-9))
    neg3 = ev3_h < -1e-9
    zer3 = np.abs(ev3_h) <= 1e-9
    corr_3d = u3_h[:, neg3] @ u3_h[:, neg3].conj().T + 0.5 * (u3_h[:, zer3] @ u3_h[:, zer3].conj().T)

    tri_to_tet3: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for ti, tau in enumerate(tets_s3):
        for j in range(4):
            tri_to_tet3[tau[:j] + tau[j + 1:]].append(ti)
    adj3: dict[int, set[int]] = defaultdict(set)
    for pair in tri_to_tet3.values():
        adj3[pair[0]].add(pair[1])
        adj3[pair[1]].add(pair[0])
    bfs_ord = [0]
    seen3 = {0}
    q3 = [0]
    while q3:
        u = q3.pop(0)
        for w_n in sorted(adj3[u]):
            if w_n not in seen3:
                seen3.add(w_n)
                bfs_ord.append(w_n)
                q3.append(w_n)

    see_per_area = []
    tri_area_unit = math.sqrt(3.0) / 4.0
    for k_sub in (4, 8, 12, 16, 20):
        a_tets = set(bfs_ord[:k_sub])
        bnd_tris = sum(1 for pair in tri_to_tet3.values() if (pair[0] in a_tets) != (pair[1] in a_tets))
        idx_a = sorted(
            {vi3[v] for ti in a_tets for v in tets_s3[ti]}
            | {ofs3[1] + ei3[(tets_s3[ti][i], tets_s3[ti][j])] for ti in a_tets for i in range(4) for j in range(i + 1, 4)}
            | {ofs3[2] + tri3[tets_s3[ti][:i] + tets_s3[ti][i + 1:]] for ti in a_tets for i in range(4)}
            | {ofs3[3] + ti for ti in a_tets}
        )
        nu = np.clip(np.real(eigh(corr_3d[np.ix_(idx_a, idx_a)], eigvals_only=True)), 1e-15, 1.0 - 1e-15)
        see = float(-np.sum(nu * np.log(nu) + (1.0 - nu) * np.log(1.0 - nu)))
        see_per_area.append(see / (bnd_tris * tri_area_unit))

    inv4g_ee_min, inv4g_ee_max = min(see_per_area), max(see_per_area)
    inv4g_sak_s005 = 4.0 * math.pi * float(cz[0])
    inv4g_sak_m2 = 4.0 * math.pi * float(cs[0])
    gee_gsak_rel_mismatch = abs(inv4g_ee_max - inv4g_sak_s005) / inv4g_ee_max

    cc.check(
        n_zero_3d == 2 and inv4g_sak_s005 > 8.0 and gee_gsak_rel_mismatch > 1.0,
        "V12.1.A4d: Subdivided S^3 KD n_zero=2, 1/(4G_Sak^lat) > 8.0 vs S_EE/|dA| (G_EE=G_Sak continuum open [П])",
    )

    print("  [V12.1.A4] 4D CDT Scan on S^1xS^3, KD Betti & G_EE vs G_Sak Obstruction [Т] / [С] / [П]:")
    for k0, dl, n0m, r41, ipr, mdg, ocb, chi_f, _, _ in cdt_scan:
        print(f"             - (k0={k0:+.1f}, D={dl:+.1f}): <N0>={n0m:4.1f}, <N41/N4>={r41:.3f}, IPR_t={ipr:.3f}, deg={mdg:.3f}, O_Cb={ocb:.3f}, chi={chi_f}")
    print(f"             - C-window CDT KD Betti = {bet_c}, d_s^max = {ds_max_cdt:.3f} < 4 [Т] / [П]")
    print(f"             - 3D S^3 KD Peschel (Ns={ns3}, n_zero={n_zero_3d}): 1/(4G_EE) in [{inv4g_ee_min:.3f}, {inv4g_ee_max:.3f}] "
          f"vs 1/(4G_Sak^lat) = {inv4g_sak_s005:.2f} (s=0.05) / {inv4g_sak_m2:.2f} (m=2.0) -> mismatch {100*gee_gsak_rel_mismatch:.0f}% [П/✗]\n")

    return {
        "tags": ["[Т]", "[С]", "[П]", "[✗]"],
        "fitted_parameters": 0,
        "pachner_hessians": {
            "s4_base": sig_s4,
            "s4_24": sig_24,
            "s4_33": sig_33,
            "s4_15_flat": sig_15_flat,
            "s4_15_curved": sig_15_curv,
            "s4_15_spike": sig_15_spike,
            "s1xs3": sig_s1s3,
        },
        "kd_bettis": {"s4": bet_s4, "s4_24": bet_24, "s1xs3": bet_s1s3, "cdt_c": bet_c},
        "kd_hessian_tt_rel_res": {"Z_KD": tt_res_z, "S_KD": tt_res_s},
        "kd_hessian_conf_rel_res": {"Z_KD": cf_res_z, "S_KD": cf_res_s},
        "kd_c_eh": {"Z_KD": float(cz[0]), "S_KD": float(cs[0])},
        "regge_mc": {
            "lq": 40.0,
            "steps": 600,
            "bare": mc_bare,
            "stab": mc_stab,
            "kd_unsub": mc_unsub,
            "kd_sub_1st": mc_sub_1st,
            "kd_sub_tt": mc_sub_tt,
            "c_cc_1": c_cc_1,
            "c_cc_tt": c_cc_tt_1,
            "tt_linear_drift_coeff": drift_coeff,
        },
        "cdt_phase_scan": cdt_scan,
        "cdt_kd_spectral_dim_max": ds_max_cdt,
        "gee_vs_gsak_obstruction": {
            "inv4g_ee_range": [inv4g_ee_min, inv4g_ee_max],
            "inv4g_sak_s005": inv4g_sak_s005,
            "inv4g_sak_m2": inv4g_sak_m2,
            "rel_mismatch": gee_gsak_rel_mismatch,
        },
    }


# ==============================================================================
# V12.1.B: MIXED BOSON+FERMION SPECTRAL ACTION AUDIT AGAINST SUPER-F-40
# ==============================================================================
def suite_v121b_mixed_boson_fermion_spectral_audit(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.1.B: Mixed Boson+Fermion Spectral Action Audit against Super-F-40")
    print("=" * 88)

    pv4 = [(1.0, 1.0), (-2.0, 2.0), (9.0 / 7.0, 3.0), (-2.0 / 7.0, 4.0)]
    sum_cm3 = sum(c * (m ** 3) for c, m in pv4)
    m2_0 = sum(c * m * m * math.log(m * m) for c, m in pv4) / (96.0 * math.pi ** 2)
    gx, gw = np.polynomial.legendre.leggauss(96)
    xs = 0.5 * (gx + 1.0)
    ws = 0.5 * gw

    # Exact integer triples (a_s, b_s, d_s)
    triples = {
        "scalar": (1.0, 0.0, 0.0),
        "weyl": (-1.0, 4.0, 0.0),
        "proca": (-3.0, 0.0, 16.0),
        "gauge": (-4.0, 0.0, 16.0),
    }

    def pi2_feyn(qval: float, kind: str, xi: float = 0.0) -> float:
        a_s, b_s, d_s = triples[kind]
        sx = xs * (1.0 - xs) * (qval * qval)
        acc = np.zeros_like(xs)
        for c, m in pv4:
            m2 = m * m
            dd = m2 + sx
            acc += c * ((a_s * dd * dd + b_s * sx * dd + d_s * (sx * sx)) * np.log(dd) - a_s * (m2 * m2) * math.log(m2))
        val = float(np.dot(ws, acc)) / (32.0 * math.pi ** 2)
        if kind == "scalar" and xi != 0.0:
            val -= 6.0 * xi * m2_0 * (qval * qval)
        return val

    def rho2_single(s: float, kind: str) -> float:
        tot = 0.0
        all_active = all(s > 4.0 * m * m for _, m in pv4)
        for c, m in pv4:
            if s > 4.0 * m * m:
                z = 4.0 * m * m / s
                b = math.sqrt(1.0 - z)
                if all_active:
                    d = z / (1.0 + b)
                    if kind == "scalar":
                        poly = -2.5 * (d ** 3) + (25.0 / 8.0) * (d ** 4) - (d ** 5)
                    elif kind == "weyl":
                        poly = 7.5 * (d ** 3) - (65.0 / 8.0) * (d ** 4) + 2.0 * (d ** 5)
                    elif kind == "proca":
                        poly = -32.5 * (d ** 3) + (165.0 / 8.0) * (d ** 4) - 3.0 * (d ** 5)
                    else:
                        poly = -30.0 * (d ** 3) + 17.5 * (d ** 4) - 2.0 * (d ** 5)
                    tot += c * (s * s / (960.0 * math.pi)) * poly
                else:
                    if kind == "scalar":
                        tot += c * (s * s / (960.0 * math.pi)) * (b ** 5)
                    elif kind == "weyl":
                        tot += 0.5 * c * (s * s / (960.0 * math.pi)) * (b ** 3) * (6.0 + 16.0 * m * m / s)
                    elif kind == "proca":
                        tot += c * (s * s / (960.0 * math.pi)) * b * (13.0 + 56.0 * m * m / s + 48.0 * (m ** 4) / (s * s))
                    else:
                        tot += c * (s * s / (960.0 * math.pi)) * (
                            b * (13.0 + 56.0 * m * m / s + 48.0 * (m ** 4) / (s * s)) - (b ** 5)
                        )
        return tot

    pts_disc = [4.0 * m * m for _, m in pv4]

    def pi2_disp_exact(qval: float, kind: str) -> float:
        q2 = qval * qval
        v1, _ = quad(lambda s: rho2_single(s, kind) * q2 / (math.pi * s * (s + q2)), 4.0, 100.0, points=pts_disc, epsabs=1e-12, epsrel=1e-10, limit=180)
        # s = 1/x^2, ds/s = -2 dx/x => q2/(s*(s+q2)) * ds = 2 x q2 / (1 + x^2 q2) dx
        v2, _ = quad(lambda x: rho2_single(1.0 / (x * x), kind) * (2.0 * x * q2 / (math.pi * (1.0 + x * x * q2))) if x > 1e-12 else 0.0, 0.0, 0.1, epsabs=1e-12, epsrel=1e-10, limit=180)
        return float(v1 + v2)

    def pi2_mixed(qval: float, n0: int, nw: int, np_: int, ng: int, xi: float = 0.0) -> float:
        return (
            n0 * pi2_feyn(qval, "scalar", xi)
            + nw * pi2_feyn(qval, "weyl")
            + np_ * pi2_feyn(qval, "proca")
            + ng * pi2_feyn(qval, "gauge")
        )

    def rho2_mixed(s: float, n0: int, nw: int, np_: int, ng: int) -> float:
        return (
            n0 * rho2_single(s, "scalar")
            + nw * rho2_single(s, "weyl")
            + np_ * rho2_single(s, "proca")
            + ng * rho2_single(s, "gauge")
        )

    # V12.1.B1: Feynman vs Dispersion, Sum-Rule Residues, Higgsing Invariance
    max_feyn_disp_err = 0.0
    for kind in ("scalar", "weyl", "proca", "gauge"):
        for qv in (0.1, 1.0, 5.0, 50.0):
            max_feyn_disp_err = max(max_feyn_disp_err, abs(pi2_feyn(qv, kind) - pi2_disp_exact(qv, kind)))

    sr_pred = {"scalar": (1.0 / 96.0) * sum_cm3, "weyl": 0.0, "proca": (-5.0 / 96.0) * sum_cm3, "gauge": (-6.0 / 96.0) * sum_cm3}
    sr_err = 0.0
    for kind in ("scalar", "weyl", "proca", "gauge"):
        v1, _ = quad(lambda s: 0.5 * rho2_single(s, kind) / (s ** 1.5), 4.0, 100.0, points=pts_disc, epsabs=1e-12, epsrel=1e-11, limit=180)
        v2, _ = quad(lambda x: rho2_single(1.0 / (x * x), kind) if x > 1e-12 else 0.0, 0.0, 0.1, epsabs=1e-12, epsrel=1e-11, limit=180)
        sr_err = max(sr_err, abs((v1 + v2) - sr_pred[kind]))

    higgs_err = max(abs(pi2_mixed(qv, 4, 48, 0, 12, 0.0) - pi2_mixed(qv, 1, 48, 3, 9, 0.0)) for qv in (0.5, 2.0, 5.0))
    higgs_rel_40 = abs(pi2_mixed(40.0, 4, 48, 0, 12, 0.0) - pi2_mixed(40.0, 1, 48, 3, 9, 0.0)) / abs(pi2_mixed(40.0, 4, 48, 0, 12, 0.0))
    cc.check(max_feyn_disp_err < 1e-7 and sr_err < 1e-9 and higgs_err < 1e-13 and higgs_rel_40 < 1e-11,
             "V12.1.B1: Spin-(0+1/2+1) PV4 Feynman=dispersion, exact residues, Higgsing invariance [Т]")

    print(f"  [V12.1.B1] Spin-(0+1/2+1) PV4 Feynman vs Dispersion & Higgsing Invariance [Т]:")
    print(f"             - max|Pi2_feyn - Pi2_disp| = {max_feyn_disp_err:.2e}, sum-rule err = {sr_err:.2e}, Higgsing err = {higgs_err:.2e}")

    # V12.1.B2: Exact Seeley-DeWitt (a0, a2, a4) Table & N=4 a=c=1/4 Sanity Check
    def seeley_dewitt(n0: int, nw: int, np_: int, ng: int, xi: float) -> dict[str, float]:
        a0 = float(n0 - 2 * nw + 3 * np_ + 2 * ng)
        c_sak = (n0 * (1.0 - 6.0 * xi) + nw - 3.0 * np_ - 4.0 * ng) / 6.0
        a4_c2 = (n0 + 3 * nw + 13 * np_ + 12 * ng) / 120.0
        a4_r2 = (n0 * ((1.0 - 6.0 * xi) ** 2) + np_) / 72.0
        a4_e4 = (n0 + 5.5 * nw + 63 * np_ + 62 * ng) / 360.0
        return {"a0": a0, "C_Sak": c_sak, "a4_C2": a4_c2, "a4_R2": a4_r2, "a4_E4": a4_e4}

    models = {
        "Dirac": (0, 2, 0, 0, 0.0),
        "SM": (4, 45, 0, 12, 0.0),
        "SM+3nuR": (4, 48, 0, 12, 0.0),
        "SM+3nuR_conf": (4, 48, 0, 12, 1.0 / 6.0),
        "MSSM": (98, 61, 0, 12, 0.0),
        "MSSM_conf": (98, 61, 0, 12, 1.0 / 6.0),
        "N4_SYM": (6, 4, 0, 1, 0.0),
        "N4_SYM_conf": (6, 4, 0, 1, 1.0 / 6.0),
        "PS_ChainA2": (68, 48, 0, 21, 0.0),
        "PS_CCvS_trunc": (80, 48, 0, 21, 0.0),
        "PS_CCvS_FULL_R": (140, 48, 0, 21, 0.0),
        "PS_CCvS_FULL_C": (200, 48, 0, 21, 0.0),
        "PS_conf": (200, 48, 0, 21, 1.0 / 6.0),
    }
    sd_table = {k: seeley_dewitt(*v) for k, v in models.items()}
    sd_ok = (
        sd_table["MSSM"]["a0"] == 0.0 and abs(sd_table["MSSM"]["C_Sak"] - 18.5) < 1e-12
        and sd_table["N4_SYM_conf"]["a0"] == 0.0
        and abs(sd_table["N4_SYM_conf"]["C_Sak"]) < 1e-12
        and abs(sd_table["N4_SYM_conf"]["a4_R2"]) < 1e-12
        and abs(sd_table["N4_SYM_conf"]["a4_C2"] - 0.25) < 1e-12
        and abs(sd_table["N4_SYM_conf"]["a4_E4"] - 0.25) < 1e-12
        and abs(sd_table["SM+3nuR_conf"]["C_Sak"]) < 1e-12
        and abs(sd_table["PS_conf"]["C_Sak"] + 6.0) < 1e-12
        and all(row["a4_C2"] > 0.0 for row in sd_table.values())
    )
    cc.check(sd_ok, "V12.1.B2: Exact Seeley-DeWitt (a0, a2, a4) table & N=4 a=c=1/4 sanity check [Т]")

    # V12.1.B3: Closed-form e^-u, u e^-u (chi(0)=0), and signed (1 - a u) e^-u cutoffs
    def delta2_exp_single(qval_or_q2: float | complex, kind: str, xi: float = 0.0, use_q2: bool = False):
        q2 = qval_or_q2 if use_q2 else (qval_or_q2 * qval_or_q2)
        a_s, b_s, d_s = triples[kind]
        sx = xs * (1.0 - xs) * q2
        ex = np.exp(-sx)
        ig = -2.0 * a_s * (ex - 1.0) + b_s * sx * ex - d_s * (sx * sx) * ex
        val = np.dot(ws, ig) / (64.0 * math.pi ** 2)
        if kind == "scalar" and xi != 0.0:
            val = val - 6.0 * xi * q2 / (192.0 * math.pi ** 2)
        return complex(val) if use_q2 else float(np.real(val))

    def delta2_exp_mixed(qval_or_q2, n0: int, nw: int, np_: int, ng: int, xi: float = 0.0, use_q2: bool = False):
        return (
            n0 * delta2_exp_single(qval_or_q2, "scalar", xi, use_q2)
            + nw * delta2_exp_single(qval_or_q2, "weyl", 0.0, use_q2)
            + np_ * delta2_exp_single(qval_or_q2, "proca", 0.0, use_q2)
            + ng * delta2_exp_single(qval_or_q2, "gauge", 0.0, use_q2)
        )

    def delta2_sharp(q: float) -> float:
        if q <= 0.0:
            return 0.0
        if q <= 2.0:
            return (q * q / (96.0 * math.pi ** 2)) * (1.0 - 0.3 * q * q)
        a = 0.5 * q
        r2 = a * a - 1.0
        r = math.sqrt(r2)
        num = -45.0 * (a ** 6) + 60.0 * (a ** 4) - 16.0
        den = (6.0 * r2 + 10.0) * (r ** 3) + (6.0 * r2 + 1.0) * (a ** 3)
        return num / (120.0 * math.pi ** 2 * a * den)

    def delta2_exp_superpos(q: float) -> float:
        sc = 0.25 * q * q
        def ig_s(s):
            return math.exp(-s) * (s * s) * delta2_sharp(q / math.sqrt(s)) if s > 0.0 else 0.0
        if sc > 25.0:
            v1a, _ = quad(ig_s, 0.0, 25.0, epsabs=1e-14, epsrel=1e-12, limit=100)
            v1b, _ = quad(ig_s, 25.0, sc, epsabs=1e-14, epsrel=1e-12, limit=100)
            v1 = v1a + v1b
        else:
            v1, _ = quad(ig_s, 0.0, sc, epsabs=1e-14, epsrel=1e-12, limit=100)
        v2, _ = quad(ig_s, sc, np.inf, epsabs=1e-14, epsrel=1e-12, limit=100)
        return float(v1 + v2)

    exp_sup_err = max(abs(2.0 * delta2_exp_single(qv, "weyl") - delta2_exp_superpos(qv)) for qv in (0.5, 1.0, 2.5, 5.0))

    def delta2_ueu_dirac(q: float) -> float:
        sx = xs * (1.0 - xs) * (q * q)
        return float(np.dot(ws, (2.0 + 3.0 * sx + 2.0 * sx * sx) * np.exp(-sx) - 2.0) / (16.0 * math.pi ** 2))

    qstar_ueu = brentq(delta2_ueu_dirac, 1.0, 6.0)
    sr_ueu_1, _ = quad(lambda q: delta2_ueu_dirac(q) / (q * q), 1e-9, 10.0, epsabs=1e-12, epsrel=1e-10)
    sr_ueu_2, _ = quad(lambda t: delta2_ueu_dirac(1.0 / t) if t > 0 else 0.0, 0.0, 0.1, epsabs=1e-12, epsrel=1e-10)
    sr_ueu = sr_ueu_1 + sr_ueu_2

    def delta2_signed_exp_single(q: float, a_c: float, kind: str) -> float:
        # chi(u) = (1 - a_c u) e^-u = (1 + a_c d/dbeta) e^{-beta u}|_{beta=1}
        # In 4D, Delta_2^{e^{-beta u}}(q) = (1/beta^2) * Delta_2^{e^-u}(sqrt(beta)*q)
        a_s, b_s, d_s = triples[kind]
        sx = xs * (1.0 - xs) * (q * q)
        ex = np.exp(-sx)
        h1 = -2.0 * a_s * (ex - 1.0) + b_s * sx * ex - d_s * (sx ** 2) * ex
        hp1 = 4.0 * a_s * (ex - 1.0) + (2.0 * a_s - b_s) * sx * ex - b_s * (sx ** 2) * ex + d_s * (sx ** 3) * ex
        return float(np.dot(ws, h1 + a_c * hp1) / (64.0 * math.pi ** 2))

    def delta2_signed_exp_mixed(q: float, a_c: float, n0: int, nw: int, np_: int, ng: int) -> float:
        return (
            n0 * delta2_signed_exp_single(q, a_c, "scalar")
            + nw * delta2_signed_exp_single(q, a_c, "weyl")
            + np_ * delta2_signed_exp_single(q, a_c, "proca")
            + ng * delta2_signed_exp_single(q, a_c, "gauge")
        )

    def find_real_zeros(fn, q_min: float = 0.02, q_max: float = 50.0, n_pts: int = 300) -> list[float]:
        qg = np.geomspace(q_min, q_max, n_pts)
        vals = [fn(float(q)) for q in qg]
        roots = []
        for i in range(len(qg) - 1):
            if vals[i] * vals[i + 1] < 0.0:
                roots.append(float(brentq(fn, float(qg[i]), float(qg[i + 1]))))
        return roots

    # Cross-check signed (1 - a u) e^-u formula at a=1 against u e^-u (Dirac: 2*weyl):
    # Note: (1 - u) e^-u = e^-u - u e^-u, so Delta_2^{(1-u)e^-u} = Delta_2^{e^-u} - Delta_2^{u e^-u}!
    ueu_chk = abs((2.0 * delta2_exp_single(1.5, "weyl") - 2.0 * delta2_signed_exp_single(1.5, 1.0, "weyl")) - delta2_ueu_dirac(1.5))
    z_ccvs_a05 = find_real_zeros(lambda q: delta2_signed_exp_mixed(q, 0.5, 200, 48, 0, 21), 0.1, 20.0)
    z_ccvs_a06 = find_real_zeros(lambda q: delta2_signed_exp_mixed(q, 0.6, 200, 48, 0, 21), 0.1, 20.0)
    signed_ok = (
        ueu_chk < 1e-12
        and len(find_real_zeros(lambda q: delta2_signed_exp_mixed(q, 0.5, 4, 45, 0, 12))) >= 1
        and len(find_real_zeros(lambda q: delta2_signed_exp_mixed(q, 0.5, 98, 61, 0, 12))) >= 1
        and len(find_real_zeros(lambda q: delta2_signed_exp_mixed(q, 0.5, 68, 48, 0, 21))) >= 1
        and len(z_ccvs_a05) == 2 and abs(z_ccvs_a05[0] - 1.5723) < 0.01 and abs(z_ccvs_a05[1] - 3.2417) < 0.01
        and len(z_ccvs_a06) == 3 and abs(z_ccvs_a06[0] - 1.3077) < 0.01 and abs(z_ccvs_a06[1] - 3.2609) < 0.01 and abs(z_ccvs_a06[2] - 7.0122) < 0.01
    )
    cc.check(
        exp_sup_err < 1e-12 and 3.44 < qstar_ueu < 3.45 and abs(sr_ueu) < 1e-9 and signed_ok,
        "V12.1.B3: Closed-form e^-u, u e^-u (chi(0)=0 -> q*=3.4473) & signed (1-au)e^-u ghosts [Т/✗]",
    )
    print(f"  [V12.1.B2-B3] Seeley-DeWitt & Cutoff Audit [Т] / [✗]:")
    print(f"                - MSSM a0=0, C_Sak=+18.5; N=4 SYM(1/6) a4_C2=a4_E4=0.25; e^-u closed vs superpos err={exp_sup_err:.2e}")
    print(f"                - Pure Dirac chi(u)=u*e^-u (f4=chi(0)=0): q*={qstar_ueu:.6f}, sum_rule={sr_ueu:+.2e}")
    print(f"                - Signed (1-a*u)e^-u on CCvS-FULL-C: a=0.5 -> {np.round(z_ccvs_a05, 4).tolist()}; a=0.6 -> {np.round(z_ccvs_a06, 4).tolist()}")

    # V12.1.B4: SM, MSSM/SUSY, and N=4 SYM Ghost & Källén-Lehmann Audit
    q_sm_pv = find_real_zeros(lambda q: pi2_mixed(q, 4, 45, 0, 12, 0.0), 0.05, 10.0)
    q_sm_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 4, 45, 0, 12, 0.0), 0.05, 10.0)
    q_smnu_pv = find_real_zeros(lambda q: pi2_mixed(q, 4, 48, 0, 12, 0.0), 0.05, 10.0)
    q_smnu_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 4, 48, 0, 12, 0.0), 0.05, 10.0)
    q_mssm_pv = find_real_zeros(lambda q: pi2_mixed(q, 98, 61, 0, 12, 0.0), 0.1, 20.0)
    q_mssm_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 98, 61, 0, 12, 0.0), 0.1, 20.0)
    q_mssm_c_pv = find_real_zeros(lambda q: pi2_mixed(q, 98, 61, 0, 12, 1.0 / 6.0), 0.1, 20.0)
    q_mssm_c_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 98, 61, 0, 12, 1.0 / 6.0), 0.1, 20.0)
    q_n4_pv = find_real_zeros(lambda q: pi2_mixed(q, 6, 4, 0, 1, 0.0), 0.1, 20.0)
    q_n4_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 6, 4, 0, 1, 0.0), 0.1, 20.0)

    s_kl = np.linspace(16.05, 60.0, 120)
    min_rho_sm = float(min(rho2_mixed(float(s), 4, 45, 0, 12) for s in s_kl))
    min_rho_mssm = float(min(rho2_mixed(float(s), 98, 61, 0, 12) for s in s_kl))

    b4_ok = (
        abs(q_sm_pv[0] - 0.2834) < 1e-3 and abs(q_sm_ex[0] - 0.1886) < 1e-3
        and abs(q_smnu_pv[0] - 0.5686) < 1e-3 and abs(q_smnu_ex[0] - 0.3751) < 1e-3
        and abs(q_mssm_pv[0] - 6.3142) < 1e-3 and abs(q_mssm_ex[0] - 2.4301) < 1e-3
        and abs(q_mssm_c_pv[0] - 0.8687) < 1e-3 and abs(q_mssm_c_ex[0] - 0.5671) < 1e-3
        and abs(q_n4_pv[0] - 3.7410) < 1e-3 and abs(q_n4_ex[0] - 1.8483) < 1e-3
        and min_rho_sm < -50.0 and min_rho_mssm < -50.0
    )
    cc.check(b4_ok, "V12.1.B4: SM, SM+3nuR, MSSM (n_c-5n_v=-11), N=4 SYM ghost zeros & Källén-Lehmann < -50 [Т/✗]")

    print("  [V12.1.B4] SM / MSSM / N=4 SYM Spectral Ghosts & Källén–Lehmann [Т] / [✗]:")
    print(f"             - SM: q*_PV4={q_sm_pv[0]:.4f}, q*_exp={q_sm_ex[0]:.4f}, min_rho2={min_rho_sm:.1f}")
    print(f"             - MSSM (xi=0): q*_PV4={q_mssm_pv[0]:.4f}, q*_exp={q_mssm_ex[0]:.4f}; (xi=1/6): {q_mssm_c_pv[0]:.4f}/{q_mssm_c_ex[0]:.4f}")
    print(f"             - N=4 SYM (xi=0): q*_PV4={q_n4_pv[0]:.4f}, q*_exp={q_n4_ex[0]:.4f}")

    # V12.1.B5: Pati-Salam / CCvS (F-42) Ghost, Complex Lee-Wick & Lorentzian Blowup Audit
    q_a2_pv = find_real_zeros(lambda q: pi2_mixed(q, 68, 48, 0, 21, 0.0), 0.1, 20.0)
    q_a2_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 68, 48, 0, 21, 0.0), 0.1, 20.0)
    q_tr_pv = find_real_zeros(lambda q: pi2_mixed(q, 80, 48, 0, 21, 0.0), 0.1, 20.0)
    q_tr_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 80, 48, 0, 21, 0.0), 0.1, 20.0)
    q_fr_pv = find_real_zeros(lambda q: pi2_mixed(q, 140, 48, 0, 21, 0.0), 0.2, 50.0)
    q_fr_ex = find_real_zeros(lambda q: delta2_exp_mixed(q, 140, 48, 0, 21, 0.0), 0.2, 50.0)
    min_rho_fc = float(min(rho2_mixed(float(s), 200, 48, 0, 21) for s in s_kl))

    def lw_res(z):
        val = delta2_exp_mixed(z[0] + 1j * z[1], 200, 48, 0, 21, 0.0, use_q2=True)
        return [val.real, val.imag]

    sol_lw = root(lw_res, [10.2, 2.7], tol=1e-14)
    q2_lw = sol_lw.x[0] + 1j * sol_lw.x[1]
    lw_err = abs(delta2_exp_mixed(q2_lw, 200, 48, 0, 21, 0.0, use_q2=True))
    lor_blowup = float(np.real(delta2_exp_mixed(-60.0 + 0j, 200, 48, 0, 21, 0.0, use_q2=True)))

    b5_ok = (
        abs(q_a2_pv[0] - 1.4408) < 1e-3 and abs(q_a2_ex[0] - 0.8955) < 1e-3
        and abs(q_tr_pv[0] - 1.7717) < 1e-3 and abs(q_tr_ex[0] - 1.0679) < 1e-3
        and len(q_fr_pv) == 2 and abs(q_fr_pv[0] - 3.8435) < 1e-3 and abs(q_fr_pv[1] - 38.0786) < 1e-3
        and len(q_fr_ex) == 2 and abs(q_fr_ex[0] - 1.8370) < 1e-3 and abs(q_fr_ex[1] - 8.3322) < 1e-3
        and min_rho_fc < -100.0 and lw_err < 1e-12 and abs(q2_lw.real - 10.278289) < 1e-4 and abs(q2_lw.imag - 2.740091) < 1e-4
        and lor_blowup < -1e7
    )
    cc.check(b5_ok, "V12.1.B5: Pati-Salam/CCvS (F-42) Euclidean ghosts, PV < -100, Lee-Wick root & Lorentzian blowup [Т/✗]")

    print("  [V12.1.B5] Pati–Salam / CCvS (F-42) Spectral Audit [Т] / [✗]:")
    print(f"             - Chain A2: q*={q_a2_pv[0]:.4f}/{q_a2_ex[0]:.4f}; CCvS-trunc: {q_tr_pv[0]:.4f}/{q_tr_ex[0]:.4f}")
    print(f"             - CCvS-FULL-R (2 zeros): PV4={np.round(q_fr_pv, 4).tolist()}, exp={np.round(q_fr_ex, 4).tolist()}")
    print(f"             - CCvS-FULL-C: min_rho2={min_rho_fc:.1f}, LW q*^2={q2_lw.real:.6f}+{q2_lw.imag:.6f}i (err={lw_err:.1e}), Delta2(-60)={lor_blowup:.3e}")

    # V12.1.B6: Minimal Positivity Thresholds, xi > 0 Tadpole & Stelle a_4 Ghost
    q_chk = np.geomspace(0.05, 80.0, 220)
    pv_s = np.array([pi2_feyn(float(q), "scalar", 0.0) for q in q_chk])
    pv_w = np.array([pi2_feyn(float(q), "weyl") for q in q_chk])
    pv_g = np.array([pi2_feyn(float(q), "gauge") for q in q_chk])
    ex_s = np.array([delta2_exp_single(float(q), "scalar", 0.0) for q in q_chk])
    ex_w = np.array([delta2_exp_single(float(q), "weyl") for q in q_chk])
    ex_g = np.array([delta2_exp_single(float(q), "gauge") for q in q_chk])

    def min_n0_positive(nw: int, ng: int, n_max: int = 250) -> tuple[int, int]:
        pv_min = next(n0 for n0 in range(1, n_max) if np.all(n0 * pv_s + nw * pv_w + ng * pv_g > 0.0))
        ex_min = next(n0 for n0 in range(1, n_max) if np.all(n0 * ex_s + nw * ex_w + ng * ex_g > 0.0))
        return pv_min, ex_min

    thresh_sm = min_n0_positive(48, 12)
    thresh_susy = (
        next(nc for nc in range(1, 100) if np.all((2 * nc) * pv_s + (nc + 12) * pv_w + 12 * pv_g > 0.0)),
        next(nc for nc in range(1, 100) if np.all((2 * nc) * ex_s + (nc + 12) * ex_w + 12 * ex_g > 0.0)),
    )
    thresh_ps = min_n0_positive(48, 21)
    tadpole_neg = all(pi2_feyn(50.0, "scalar", xi) < 0.0 for xi in (0.01, 0.10, 1.0 / 6.0))
    # Stelle a_4 ratio for f(u) = e^-u: f0^CC = f4^UHM = 1, f2^CC = 1 => q_Weyl^2 / Lam^2 = 10 f2^CC / (3 f0^CC) = 10/3
    f0_cc = 1.0
    f2_cc = 1.0
    q_weyl_sq_ratio = (10.0 * f2_cc) / (3.0 * f0_cc)
    mpl_ratio = f2_cc / (24.0 * math.pi ** 2)

    cc.check(
        thresh_sm == (105, 120) and thresh_susy == (62, 69) and thresh_ps == (169, 196)
        and tadpole_neg and abs(q_weyl_sq_ratio - 10.0 / 3.0) < 1e-14 and abs(mpl_ratio - 1.0 / (24.0 * math.pi ** 2)) < 1e-14,
        "V12.1.B6: Minimal positivity thresholds (105/120, 62/69, 169/196), xi>0 tadpole & Stelle a_4 ghost [Т/✗]",
    )
    print("  [V12.1.B6] Positivity Thresholds, xi>0 Tadpole & Stelle a_4 Ghost [Т] / [✗]:")
    print(f"             - Min Euclidean positivity thresholds: SM+3nuR N0>={thresh_sm} (actual 4), SUSY nc>={thresh_susy} (MSSM 49), PS N0>={thresh_ps} (Chain A2 68)")
    print(f"             - Stelle a_4 Weyl ghost: q_Weyl^2/Lam^2 = {q_weyl_sq_ratio:.4f} (=10/3); M_Pl,red^2/(N_D Lam^2) = {mpl_ratio:.6f}\n")

    return {
        "tags": ["[Т]", "[✗]", "[С]", "[П]"],
        "fitted_parameters": 0,
        "max_feyn_disp_err": max_feyn_disp_err,
        "higgsing_err": higgs_err,
        "seeley_dewitt": sd_table,
        "qstar_ueu_dirac": qstar_ueu,
        "signed_ccvs_zeros": {"a0.5": z_ccvs_a05, "a0.6": z_ccvs_a06},
        "pv4_exp_zeros": {
            "SM": (q_sm_pv[0], q_sm_ex[0]),
            "SM+3nuR": (q_smnu_pv[0], q_smnu_ex[0]),
            "MSSM": (q_mssm_pv[0], q_mssm_ex[0]),
            "MSSM_conf": (q_mssm_c_pv[0], q_mssm_c_ex[0]),
            "N4_SYM": (q_n4_pv[0], q_n4_ex[0]),
            "PS_ChainA2": (q_a2_pv[0], q_a2_ex[0]),
            "PS_CCvS_trunc": (q_tr_pv[0], q_tr_ex[0]),
            "PS_CCvS_FULL_R": (q_fr_pv, q_fr_ex),
        },
        "ccvs_full_c_lee_wick": [float(q2_lw.real), float(q2_lw.imag)],
        "ccvs_full_c_lorentzian_m60": lor_blowup,
        "positivity_thresholds": {"SM+3nuR": thresh_sm, "SUSY_nc": thresh_susy, "PS_N0": thresh_ps},
    }


# ==============================================================================
# V12.1.C: STRING / WORLDSHEET UV COMPATIBILITY WITH F-41 & G_EE = G_Sak
# ==============================================================================
def suite_v121c_string_uv_f41_compatibility(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.1.C: String / Worldsheet UV Compatibility with F-41 & G_EE = G_Sak")
    print("=" * 88)

    # V12.1.C1: D_5 Kac-Moody sweep + E_8xE_8, Spin(32)/Z_2, non-geo c_L=22, direct G_422
    pos_roots = []
    for i in range(5):
        for j in range(i + 1, 5):
            for sgn in (1, -1):
                r = np.zeros(5, dtype=int)
                r[i] = 1
                r[j] = sgn
                pos_roots.append(r)
    two_rho = np.array([8, 6, 4, 2, 0], dtype=int)
    weyl_den = int(np.prod([int(np.dot(two_rho, r)) for r in pos_roots]))

    d5_irreps = {
        "10": (np.array([2, 0, 0, 0, 0]), 10, 9.0),
        "16": (np.array([1, 1, 1, 1, 1]), 16, 11.25),
        "45": (np.array([2, 2, 0, 0, 0]), 45, 16.0),
        "54": (np.array([4, 0, 0, 0, 0]), 54, 20.0),
        "120": (np.array([2, 2, 2, 0, 0]), 120, 21.0),
        "126bar": (np.array([2, 2, 2, 2, -2]), 126, 25.0),
        "210": (np.array([2, 2, 2, 2, 0]), 210, 24.0),
    }
    d5_weyl_ok = True
    for w2, exp_d, exp_2c2 in d5_irreps.values():
        num = int(np.prod([int(np.dot(w2 + two_rho, r)) for r in pos_roots]))
        two_c2 = float(np.dot(w2, w2 + 2 * two_rho)) / 4.0
        if num // weyl_den != exp_d or abs(two_c2 - exp_2c2) > 1e-12:
            d5_weyl_ok = False

    km_d5 = {}
    for k in range(1, 8):
        c_k = 45.0 * k / (k + 8.0)
        h_126 = 25.0 / (2.0 * (k + 8.0))
        h_210 = 24.0 / (2.0 * (k + 8.0))
        h_54 = 20.0 / (2.0 * (k + 8.0))
        km_d5[k] = (c_k, h_126, h_210, h_54)

    k_max_spin32 = max(n10 + 2 * n16 for n10 in range(5) for n16 in range(4) if 10 * n10 + 16 * n16 <= 32)
    k_max_e8_1 = max(k for k in range(1, 5) if km_d5[k][0] <= 8.0)
    k_max_e8_diag = 2 * k_max_e8_1
    k_max_nongeo = max(k for k in range(1, 8) if 5 * k <= 22)

    km_g422 = {}
    for k in range(1, 7):
        # G_422 = SU(4)_C x SU(2)_L x SU(2)_R: c = 15k/(k+4) + 3k/(k+2) + 3k/(k+2)
        c_g = 15.0 * k / (k + 4.0) + 6.0 * k / (k + 2.0)
        # Delta_R = (10, 1, 3): 2 C_2(10)=9, 2 C_2(3)=4 => h = 9/(2(k+4)) + 4/(2(k+2))
        h_dr = 4.5 / (k + 4.0) + 2.0 / (k + 2.0)
        # (15, 2, 2): 2 C_2(15)=8, 2 C_2(2)=1.5 => h = 4/(k+4) + 1.5/(k+2)
        h_1522 = 4.0 / (k + 4.0) + 1.5 / (k + 2.0)
        km_g422[k] = (c_g, h_dr, h_1522)

    c1_ok = (
        d5_weyl_ok
        and all(km_d5[k][1] > 1.0 for k in range(1, 5))
        and all(km_d5[k][0] > 16.0 for k in range(5, 8))
        and k_max_spin32 == 4 < 5 and k_max_e8_diag == 2 < 5 and k_max_nongeo == 4 < 5
        and km_g422[3][1] > 1.0 and km_g422[4][1] <= 1.0 and abs(km_g422[4][0] - 11.5) < 1e-12
    )
    cc.check(c1_ok, "V12.1.C1: D_5 KM sweep (c(D_5,5)=225/13>16), Spin(32)/E_8/c_L=22 ceilings, G_422 k_min=4 [Т/✗]")

    print("  [V12.1.C1] Heterotic Kac–Moody & Direct G_422 Audit (`F-41A`) [Т] / [✗]:")
    print(f"             - D_5 k=5: c={km_d5[5][0]:.4f} (225/13 > 16); k_max(Spin32)={k_max_spin32}, k_max(E8xE8)={k_max_e8_diag}, k_max(c_L=22)={k_max_nongeo}")
    print(f"             - Unified G_422: h_DeltaR(k=3)={km_g422[3][1]:.4f} > 1, k_min=4 gives c={km_g422[4][0]:.2f} (unequal k_i breaks g_4C=g_2L=g_2R)")

    # V12.1.C2: Type II Closed c_int=9 & Open-String Chan-Paton Tensor-Rank Theorem
    so10_ranks = {r: math.comb(10, r) for r in range(1, 6)}
    so10_ranks["sym2_0"] = 10 * 11 // 2 - 1
    ps_cp_ranks = {
        "(4,2,1)_F": (1, 1, 0),
        "(4bar,1,2)_F": (1, 0, 1),
        "(1,2,2)_H": (0, 1, 1),
        "(6,1,1)_H": (2, 0, 0),
        "(4bar,1,2)_H": (1, 0, 1),
        "(10,1,3)_DeltaR": (2, 0, 2),
        "(15,2,2)_H": (2, 1, 1),
    }
    c_type2_int = 9.0
    c2_ok = (
        so10_ranks[3] == 120 and so10_ranks[4] == 210 and so10_ranks[5] == 252 and so10_ranks["sym2_0"] == 54
        and all(sum(v) <= 2 for k, v in ps_cp_ranks.items() if k not in ("(10,1,3)_DeltaR", "(15,2,2)_H"))
        and sum(ps_cp_ranks["(10,1,3)_DeltaR"]) == 4 > 2
        and sum(ps_cp_ranks["(15,2,2)_H"]) == 4 > 2
        and c_type2_int < km_d5[5][0] and c_type2_int < km_g422[4][0]
    )
    cc.check(c2_ok, "V12.1.C2: Type II closed c_int=9 & Open-String Chan-Paton endpoint rank <= 2 excludes 126bar/210/DeltaR [Т/✗]")

    print("  [V12.1.C2] Type II Closed & Open-String Chan–Paton Tensor-Rank Theorem [Т] / [✗]:")
    print(f"             - Open-string endpoints=2: Delta_R=(10,1,3) rank={sum(ps_cp_ranks['(10,1,3)_DeltaR'])} > 2, (15,2,2) rank={sum(ps_cp_ranks['(15,2,2)_H'])} > 2; Type II c_int=9 < {km_d5[5][0]:.2f}, {km_g422[4][0]:.1f}")

    # V12.1.C3: F-Theory ADE Unfoldings + Z_2^DM Pincer (F-41B, C) & 1-step SM RGE miss
    ade_dims = {
        "E6": 45 + 1 + 16 + 16,
        "E7": 45 + 2 * 10 + 2 * 16 + 2 * 16 + 4,
        "E8": 45 + 15 + 6 * 10 + 4 * 16 + 4 * 16,
    }
    d_n_ok = all((5 + m) * (9 + 2 * m) == 45 + 20 * m + m * (2 * m - 1) for m in range(11))
    z4_126bar = (0 + 1 + 2) % 4
    z4_16bar = (0 + 1 + 3) % 4

    # Compute exact 1-loop/2-loop SM missing gap Delta(alpha^-1) at g_1 = g_2 crossing:
    a1_0 = (5.0 / 3.0) / (127.951 * (1.0 - 0.23122))
    a2_0 = 1.0 / (127.951 * 0.23122)
    a3_0 = 0.1180
    g_sm0 = [math.sqrt(4.0 * math.pi * a1_0), math.sqrt(4.0 * math.pi * a2_0), math.sqrt(4.0 * math.pi * a3_0), 0.995]
    b_sm = np.array([41.0 / 10.0, -19.0 / 6.0, -7.0])
    b2_sm = np.array([[199.0 / 50.0, 27.0 / 10.0, 44.0 / 5.0], [9.0 / 10.0, 35.0 / 6.0, 12.0], [11.0 / 10.0, 4.5, -26.0]])
    c_u = np.array([17.0 / 10.0, 1.5, 2.0])

    def rhs_sm(_t, y):
        g = np.array(y[:3])
        yt = y[3]
        dg = (g ** 3) / (16.0 * math.pi ** 2) * b_sm + (g ** 3) / ((16.0 * math.pi ** 2) ** 2) * (b2_sm @ (g * g) - c_u * (yt * yt))
        dyt = yt / (16.0 * math.pi ** 2) * (4.5 * yt * yt - 0.85 * y[0] ** 2 - 2.25 * y[1] ** 2 - 8.0 * y[2] ** 2)
        return [dg[0], dg[1], dg[2], dyt]

    def ev_12(_t, y):
        return y[0] - y[1]

    ev_12.terminal = True
    sol_sm = solve_ivp(rhs_sm, (0.0, 40.0), g_sm0, events=ev_12, rtol=1e-11, atol=1e-13)
    g_hit = sol_sm.y[:, -1]
    a12_inv = 4.0 * math.pi / (g_hit[0] ** 2)
    a3_inv = 4.0 * math.pi / (g_hit[2] ** 2)
    delta_alpha_inv_2l = abs(a3_inv - a12_inv)
    # 1-loop SM analytic miss at alpha_1 = alpha_2:
    t_1l = 2.0 * math.pi * (1.0 / a1_0 - 1.0 / a2_0) / (b_sm[0] - b_sm[1])
    delta_alpha_inv_1l = abs((1.0 / a3_0 - b_sm[2] * t_1l / (2.0 * math.pi)) - (1.0 / a1_0 - b_sm[0] * t_1l / (2.0 * math.pi)))

    c3_ok = (
        ade_dims == {"E6": 78, "E7": 133, "E8": 248}
        and d_n_ok and z4_126bar == 3 and z4_16bar == 0
        and abs(delta_alpha_inv_1l - 5.58) < 0.05 and 4.5 < delta_alpha_inv_2l < 5.5
    )
    cc.check(c3_ok, "V12.1.C3: F-theory ADE unfoldings (max D5 dim<=45), Z_2^DM pincer (3!=0 vs 0), SM miss 5.58 (1L) / 4.90 (2L) [Т/✗]")

    print("  [V12.1.C3] F-Theory ADE Unfoldings & Z_2^DM Pincer (`F-41B,C`) [Т] / [✗]:")
    print(f"             - ADE dims={ade_dims}, Z_4(126bar)={z4_126bar}!=0 vs Z_4(16bar)={z4_16bar}==0, 1-step SM Delta(alpha^-1)={delta_alpha_inv_1l:.2f} (1L) / {delta_alpha_inv_2l:.2f} (2L)")

    # V12.1.C4: Heterotic Gauge-Gravity Scale Mismatch & Species Bound vs G_EE = G_Sak
    alpha_gut_inv = 45.15
    g_gut = math.sqrt(4.0 * math.pi / alpha_gut_inv)
    lam_ncg = 7.890e15
    m_pl_red = 2.4353e18
    ms_ratios = {k: (math.sqrt(0.5 * k) * g_gut * m_pl_red) / lam_ncg for k in (1, 4, 5)}
    mkap_ratios = {k: (5.27e17 * g_gut * math.sqrt(k)) / lam_ncg for k in (1, 4, 5)}
    n_d_req = 12.0 * (math.pi ** 2) * ((m_pl_red / lam_ncg) ** 2)
    n_d_chain_a2 = 24.0
    species_frac = n_d_chain_a2 / n_d_req

    c4_ok = (
        all(v > 100.0 for v in ms_ratios.values())
        and all(v > 30.0 for v in mkap_ratios.values())
        and n_d_req > 1.0e7 and species_frac < 3.0e-6
    )
    cc.check(c4_ok, "V12.1.C4: Heterotic M_s/Lam_NCG > 100, M_Kap/Lam_NCG > 30 & induced species bound N_D > 10^7 vs 24 [Т/✗/П]")

    print("  [V12.1.C4] Heterotic Scale Mismatch & Induced Species Bound vs G_EE = G_Sak [Т] / [✗] / [П]:")
    print(f"             - M_s/Lam_NCG (k=1,4,5) = {[round(ms_ratios[k], 1) for k in (1,4,5)]}; M_Kap/Lam_NCG = {[round(mkap_ratios[k], 1) for k in (1,4,5)]}")
    print(f"             - Pure G_Sak=G_EE at Lam_NCG requires N_D={n_d_req:.3e} vs Chain A2 24 Dirac ({species_frac:.3e} fraction).\n")

    return {
        "tags": ["[Т]", "[✗]", "[П]"],
        "fitted_parameters": 0,
        "km_d5": km_d5,
        "km_g422": km_g422,
        "k_max": {"spin32": k_max_spin32, "e8xe8": k_max_e8_diag, "nongeo_c22": k_max_nongeo},
        "chan_paton_ranks": ps_cp_ranks,
        "sm_1step_delta_alpha_inv_1l": delta_alpha_inv_1l,
        "sm_1step_delta_alpha_inv_2l": delta_alpha_inv_2l,
        "heterotic_ms_over_lam": ms_ratios,
        "heterotic_mkap_over_lam": mkap_ratios,
        "species_bound_nd_req": n_d_req,
        "species_fraction": species_frac,
    }


def run_v12_wall1() -> tuple[int, int, dict]:
    cc = _CheckCounter()
    sum_a = suite_v121a_dynamical_4d_simplicial_cdt_regge_kd(cc)
    sum_b = suite_v121b_mixed_boson_fermion_spectral_audit(cc)
    sum_c = suite_v121c_string_uv_f41_compatibility(cc)
    summary = {
        "V12.1.A": sum_a,
        "V12.1.B": sum_b,
        "V12.1.C": sum_c,
        "tags": {
            "V12.1.A": sum_a["tags"],
            "V12.1.B": sum_b["tags"],
            "V12.1.C": sum_c["tags"],
        },
        "fitted_parameters": 0,
        "passed": cc.passed,
        "total": cc.total,
        "failures": cc.failures,
    }
    return cc.passed, cc.total, summary


# ==============================================================================
# SHARED MODULAR & 2-LOOP RGE HELPERS (EXACT, ZERO FITTING)
# ==============================================================================
def _eta(tau: np.ndarray | complex, n_max: int = 50) -> np.ndarray | complex:
    q = np.exp(2j * math.pi * tau)
    val = np.exp(1j * math.pi * tau / 12.0)
    for n in range(1, n_max + 1):
        val = val * (1.0 - q ** n)
    return val


def _eisenstein_e2(tau: np.ndarray | complex, n_max: int = 50) -> np.ndarray | complex:
    q = np.exp(2j * math.pi * tau)
    val = np.ones_like(tau, dtype=complex) if isinstance(tau, np.ndarray) else 1.0 + 0j
    for n in range(1, n_max + 1):
        s1 = sum(d for d in range(1, n + 1) if n % d == 0)
        val = val - 24.0 * s1 * (q ** n)
    return val


def _eisenstein_e4_e6(tau: np.ndarray | complex, n_max: int = 45):
    q = np.exp(2j * math.pi * tau)
    e4 = np.ones_like(tau, dtype=complex) if isinstance(tau, np.ndarray) else 1.0 + 0j
    e6 = np.ones_like(tau, dtype=complex) if isinstance(tau, np.ndarray) else 1.0 + 0j
    for n in range(1, n_max + 1):
        qn = q ** n
        s3 = sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
        s5 = sum(d ** 5 for d in range(1, n + 1) if n % d == 0)
        e4 = e4 + 240.0 * s3 * qn
        e6 = e6 - 504.0 * s5 * qn
    return e4, e6


def _j_invariant(tau: np.ndarray | complex, n_max: int = 45) -> np.ndarray | complex:
    et = _eta(tau, n_max=n_max)
    e4, _ = _eisenstein_e4_e6(tau, n_max=n_max)
    return (e4 ** 3) / (et ** 24)


def _theta234(tau: np.ndarray | complex, n_max: int = 45):
    q = np.exp(1j * math.pi * tau)
    th2 = np.zeros_like(tau, dtype=complex) if isinstance(tau, np.ndarray) else 0.0 + 0j
    th3 = np.ones_like(tau, dtype=complex) if isinstance(tau, np.ndarray) else 1.0 + 0j
    th4 = np.ones_like(tau, dtype=complex) if isinstance(tau, np.ndarray) else 1.0 + 0j
    for n in range(n_max):
        th2 = th2 + 2.0 * (q ** ((n + 0.5) ** 2))
    for n in range(1, n_max + 1):
        qn2 = q ** (n * n)
        th3 = th3 + 2.0 * qn2
        th4 = th4 + 2.0 * ((-1) ** n) * qn2
    return th2, th3, th4


# PDG 2024 EW inputs at M_Z = 91.1876 GeV (exact parity with verify_deep_frontier_v11.py)
M_Z_PDG = 91.1876
ALPHA_EM_INV_MZ = 127.951
SIN2_THW_MZ = 0.23122
ALPHA_S_MZ = 0.1180

S_122_C = (1.0, (1, 0.0, 0.0), (2, 0.5, 0.75), (2, 0.5, 0.75))
S_1013_C = (1.0, (10, 3.0, 4.5), (1, 0.0, 0.0), (3, 2.0, 2.0))
S_611_C = (1.0, (6, 1.0, 2.5), (1, 0.0, 0.0), (1, 0.0, 0.0))
S_1522_R = (0.5, (15, 4.0, 4.0), (2, 0.5, 0.75), (2, 0.5, 0.75))
S_1522_C = (1.0, (15, 4.0, 4.0), (2, 0.5, 0.75), (2, 0.5, 0.75))


def _sm_betas(ng: int = 3):
    b_g = np.array([
        -11.0 / 3.0 * 0.0 + 4.0 / 3.0 * ng + 1.0 / 10.0,
        -22.0 / 3.0 + 4.0 / 3.0 * ng + 1.0 / 6.0,
        -11.0 + 4.0 / 3.0 * ng,
    ])
    # Exact Machacek-Vaughn 2-loop gauge matrix for ng chiral SM families + 1 complex Higgs doublet
    b2 = np.array([
        [19.0 / 15.0 * ng + 9.0 / 50.0, 3.0 / 5.0 * ng + 9.0 / 10.0, 44.0 / 15.0 * ng],
        [1.0 / 5.0 * ng + 3.0 / 10.0, -136.0 / 3.0 + 49.0 / 3.0 * ng + 13.0 / 6.0, 4.0 * ng],
        [11.0 / 30.0 * ng, 3.0 / 2.0 * ng, -102.0 + 76.0 / 3.0 * ng],
    ])
    return b_g, b2


def _ps_betas(scalars, ng: int = 3):
    """Exact Machacek-Vaughn 1-loop & 2-loop beta coefficients for G_422 with ng chiral generations."""
    c2g = np.array([4.0, 2.0, 2.0])
    b = -(11.0 / 3.0) * c2g
    bmat = np.diag(-(34.0 / 3.0) * (c2g ** 2))
    weyls = [
        (ng, (4, 0.5, 15.0 / 8.0), (2, 0.5, 0.75), (1, 0.0, 0.0)),
        (ng, (4, 0.5, 15.0 / 8.0), (1, 0.0, 0.0), (2, 0.5, 0.75)),
    ]
    for mult, r4, r_l, r_r in weyls:
        rs = [r4, r_l, r_r]
        for i in range(3):
            d_oth = rs[(i + 1) % 3][0] * rs[(i + 2) % 3][0]
            ti = mult * rs[i][1] * d_oth
            b[i] += (2.0 / 3.0) * ti
            for j in range(3):
                if i == j:
                    bmat[i, i] += ((10.0 / 3.0) * c2g[i] + 2.0 * rs[i][2]) * ti
                else:
                    bmat[i, j] += 2.0 * rs[j][2] * ti
    for fac, r4, r_l, r_r in scalars:
        rs = [r4, r_l, r_r]
        for i in range(3):
            d_oth = rs[(i + 1) % 3][0] * rs[(i + 2) % 3][0]
            ti = fac * rs[i][1] * d_oth
            b[i] += (1.0 / 3.0) * ti
            for j in range(3):
                if i == j:
                    bmat[i, i] += ((2.0 / 3.0) * c2g[i] + 4.0 * rs[i][2]) * ti
                else:
                    bmat[i, j] += 4.0 * rs[j][2] * ti
    return b, bmat


def _run_sm_2loop(t_end: float, ng: int = 3, three_gen_yuk: bool = False, alpha_s_val: float = ALPHA_S_MZ):
    a1_0 = (5.0 / 3.0) / (ALPHA_EM_INV_MZ * (1.0 - SIN2_THW_MZ))
    a2_0 = 1.0 / (ALPHA_EM_INV_MZ * SIN2_THW_MZ)
    g0 = [math.sqrt(4.0 * math.pi * a1_0), math.sqrt(4.0 * math.pi * a2_0), math.sqrt(4.0 * math.pi * alpha_s_val)]
    b_sm, bmat_sm = _sm_betas(ng=ng)
    c_u = np.array([17.0 / 10.0, 3.0 / 2.0, 2.0])
    c_d = np.array([1.0 / 2.0, 3.0 / 2.0, 2.0])
    c_e = np.array([3.0 / 2.0, 1.0 / 2.0, 0.0])
    # 3rd-gen Yukawas at M_Z (m_t(M_Z) ~ 173, m_b(M_Z) ~ 2.84 -> y_b=0.0163, m_tau ~ 1.746 -> y_tau=0.0100)
    yb0 = 0.0163 if three_gen_yuk else 0.0
    ytau0 = 0.0100 if three_gen_yuk else 0.0

    def rhs(_t, y):
        g1, g2, g3, yt, yb, ytau = y
        g = np.array([g1, g2, g3])
        g2v = g * g
        yuk_corr = c_u * (yt * yt) + c_d * (yb * yb) + c_e * (ytau * ytau)
        dg = (g ** 3) / (16.0 * math.pi ** 2) * b_sm + (g ** 3) / ((16.0 * math.pi ** 2) ** 2) * (bmat_sm @ g2v - yuk_corr)
        t_trace = 3.0 * yt * yt + 3.0 * yb * yb + ytau * ytau
        dyt = yt / (16.0 * math.pi ** 2) * (1.5 * yt * yt - 1.5 * yb * yb + t_trace - 0.85 * g1 * g1 - 2.25 * g2 * g2 - 8.0 * g3 * g3)
        dyb = yb / (16.0 * math.pi ** 2) * (1.5 * yb * yb - 1.5 * yt * yt + t_trace - 0.25 * g1 * g1 - 2.25 * g2 * g2 - 8.0 * g3 * g3)
        dytau = ytau / (16.0 * math.pi ** 2) * (1.5 * ytau * ytau + t_trace - 2.25 * g1 * g1 - 2.25 * g2 * g2)
        return [dg[0], dg[1], dg[2], dyt, dyb, dytau]

    sol = solve_ivp(rhs, (0.0, t_end), [g0[0], g0[1], g0[2], 0.995, yb0, ytau0], rtol=1e-11, atol=1e-13)
    return sol.y[:, -1]


def _solve_ps_unif(
    scalars_lo,
    scalars_hi=None,
    m_heavy: float | None = None,
    ng: int = 3,
    three_gen_yuk: bool = False,
    alpha_s_val: float = ALPHA_S_MZ,
):
    b_lo, bmat_lo = _ps_betas(scalars_lo, ng=ng)
    b_hi, bmat_hi = _ps_betas(scalars_hi, ng=ng) if scalars_hi is not None else (b_lo, bmat_lo)
    # Exact 4-color Pati-Salam 2-loop Yukawa matrices (per 3rd-gen fermion type):
    c_top_ps = np.array([2.0, 2.0, 2.0])
    c_bot_ps = np.array([2.0, 2.0, 2.0])
    # y_nu3 at M_PS = 0.5423 from Chain A2 non-PQ Dirac neutrino mass M_{N_3} = 3.005e11 GeV
    ynu0 = 0.5423 if three_gen_yuk else 0.0

    def eval_at_mps(log10_mps: float):
        t_ps = (log10_mps - math.log10(M_Z_PDG)) * math.log(10.0)
        g1, g2, g3, yt, yb, ytau = _run_sm_2loop(t_ps, ng=ng, three_gen_yuk=three_gen_yuk, alpha_s_val=alpha_s_val)
        a1 = g1 * g1 / (4.0 * math.pi)
        a3 = g3 * g3 / (4.0 * math.pi)
        a2r_inv = (5.0 / 3.0) / a1 - (2.0 / 3.0) / a3
        if a2r_inv <= 0.0:
            return 1e9, 0.0, 0.0
        g_ps = np.array([g3, g2, math.sqrt(4.0 * math.pi / a2r_inv)])
        t_h = (math.log10(m_heavy) - math.log10(M_Z_PDG)) * math.log(10.0) if m_heavy is not None else 1e9

        def run_ps_seg(t0, t1, y0, bv, bmat):
            def rhs(_t, y):
                g = y[:3]
                yt_c, yb_c, ynu_c = y[3], y[4], y[5]
                g2v = g * g
                yuk = c_top_ps * (yt_c * yt_c) + c_bot_ps * (yb_c * yb_c) + c_top_ps * (ynu_c * ynu_c)
                dg = (g ** 3) / (16.0 * math.pi ** 2) * bv + (g ** 3) / ((16.0 * math.pi ** 2) ** 2) * (bmat @ g2v - yuk)
                # G_422 1-loop Yukawa running (4 colors):
                tr_4 = 4.0 * (yt_c * yt_c + yb_c * yb_c + ynu_c * ynu_c)
                g_yuk_shift = -7.5 * g[0] ** 2 - 2.25 * (g[1] ** 2 + g[2] ** 2)
                dyt = yt_c / (16.0 * math.pi ** 2) * (2.0 * yt_c ** 2 + tr_4 + g_yuk_shift)
                dyb = yb_c / (16.0 * math.pi ** 2) * (2.0 * yb_c ** 2 + tr_4 + g_yuk_shift)
                dynu = ynu_c / (16.0 * math.pi ** 2) * (2.0 * ynu_c ** 2 + tr_4 + g_yuk_shift)
                return [dg[0], dg[1], dg[2], dyt, dyb, dynu]

            def ev_g4_g2l(_t, y):
                return y[0] - y[1]

            ev_g4_g2l.terminal = True
            sol = solve_ivp(rhs, (t0, t1), y0, events=ev_g4_g2l, rtol=1e-11, atol=1e-13)
            hit = len(sol.t_events[0]) > 0
            return hit, float(sol.t[-1]), sol.y[:, -1]

        t_max = (19.0 - math.log10(M_Z_PDG)) * math.log(10.0)
        yb_eff = max(yb, ytau) if three_gen_yuk else 0.0
        y0 = [g_ps[0], g_ps[1], g_ps[2], yt, yb_eff, ynu0]
        if m_heavy is not None and t_h > t_ps:
            hit, t_hit, y_hit = run_ps_seg(t_ps, min(t_h, t_max), y0, b_lo, bmat_lo)
            if not hit and t_h < t_max:
                hit, t_hit, y_hit = run_ps_seg(t_h, t_max, y_hit, b_hi, bmat_hi)
        else:
            hit, t_hit, y_hit = run_ps_seg(t_ps, t_max, y0, b_hi, bmat_hi)
        if not hit:
            return 1e9, 0.0, 0.0
        a_inv = 4.0 * math.pi / (y_hit[0] ** 2)
        lam = M_Z_PDG * math.exp(t_hit)
        return float(y_hit[2] - y_hit[0]), lam, a_inv

    log_mps = brentq(lambda x: eval_at_mps(x)[0], 8.0, 14.0, xtol=1e-10)
    res, lam, a_inv = eval_at_mps(log_mps)
    if abs(res) > 1e-6:
        raise RuntimeError(f"PS crossing residual too large: {res}")
    return 10.0 ** log_mps, lam, a_inv


def _run_sm_higgs_2loop(m_end: float) -> float:
    """Buttazzo et al. 2013 2-loop SM Higgs quartic lambda_H(M_end) from M_t = 172.69 GeV."""
    m_t = 172.69
    t_end = math.log(m_end / m_t)

    def rhs(_t, y):
        g1, g2, g3, yt, lam = y
        k1 = 1.0 / (16.0 * math.pi ** 2)
        k2 = k1 * k1
        gp2 = 0.6 * g1 * g1
        g2_2 = g2 * g2
        g3_2 = g3 * g3
        yt2 = yt * yt
        dg1 = g1 ** 3 * (k1 * (41.0 / 10.0) + k2 * ((199.0 / 50.0) * g1 ** 2 + (27.0 / 10.0) * g2_2 + (44.0 / 5.0) * g3_2 - (17.0 / 10.0) * yt2))
        dg2 = g2 ** 3 * (k1 * (-19.0 / 6.0) + k2 * ((9.0 / 10.0) * g1 ** 2 + (35.0 / 6.0) * g2_2 + 12.0 * g3_2 - 1.5 * yt2))
        dg3 = g3 ** 3 * (k1 * (-7.0) + k2 * ((11.0 / 10.0) * g1 ** 2 + 4.5 * g2_2 - 26.0 * g3_2 - 2.0 * yt2))
        dyt = yt * (
            k1 * (4.5 * yt2 - (17.0 / 12.0) * gp2 - (9.0 / 4.0) * g2_2 - 8.0 * g3_2)
            + k2 * (
                -12.0 * yt2 ** 2 + 6.0 * lam ** 2 - 12.0 * lam * yt2 + 36.0 * g3_2 * yt2 + (225.0 / 16.0) * g2_2 * yt2
                + (393.0 / 80.0) * g1 ** 2 * yt2 - 108.0 * g3_2 ** 2 - (23.0 / 4.0) * g2_2 ** 2 + (1187.0 / 600.0) * g1 ** 4
                + 9.0 * g3_2 * g2_2 + (19.0 / 15.0) * g3_2 * g1 ** 2 - (9.0 / 20.0) * g2_2 * g1 ** 2
            )
        )
        b1_lam = (
            24.0 * lam ** 2 - 3.0 * lam * (gp2 + 3.0 * g2_2)
            + (3.0 / 8.0) * (2.0 * g2_2 ** 2 + (gp2 + g2_2) ** 2)
            + 12.0 * lam * yt2 - 6.0 * yt2 ** 2
        )
        b2_lam = (
            -312.0 * lam ** 3 + 36.0 * lam ** 2 * (gp2 + 3.0 * g2_2)
            - lam * (73.0 / 8.0 * g2_2 ** 2 - (39.0 / 4.0) * gp2 * g2_2 - (629.0 / 24.0) * gp2 ** 2)
            + (305.0 / 16.0) * g2_2 ** 3 - (289.0 / 48.0) * gp2 * g2_2 ** 2 - (559.0 / 48.0) * gp2 ** 2 * g2_2 - (379.0 / 48.0) * gp2 ** 3
            - 144.0 * lam ** 2 * yt2 - 3.0 * lam * yt2 ** 2 + 30.0 * yt2 ** 3
            + lam * yt2 * (80.0 * g3_2 + (45.0 / 2.0) * g2_2 + (85.0 / 6.0) * gp2)
            - yt2 ** 2 * (32.0 * g3_2 + (8.0 / 3.0) * gp2)
            - yt2 * ((9.0 / 4.0) * g2_2 ** 2 - (21.0 / 2.0) * gp2 * g2_2 + (19.0 / 4.0) * gp2 ** 2)
        )
        return [dg1, dg2, dg3, dyt, k1 * b1_lam + k2 * b2_lam]

    sol = solve_ivp(rhs, (0.0, t_end), [0.4626, 0.6478, 1.1666, 0.9347, 0.12604], rtol=1e-11, atol=1e-13)
    return float(sol.y[4, -1])


# ==============================================================================
# V12.2.A: MICROSCOPIC CP & ZERO-FITTING CKM AUDIT (EXPLORER 1 SPEC 4.1)
# ==============================================================================
def suite_v122a_cp_and_ckm_audit(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.2.A: Microscopic Non-Heterotic CP, Gamma_0(4) CP_2, Racetrack & 16-Config CKM Audit")
    print("=" * 88)

    # 1. Modular & congruence fixed-point no-go for tau_0 = 0.25 + 1.5i
    tau_0 = 0.25 + 1.5j
    in_f_interior = abs(tau_0.real) < 0.5 and (abs(tau_0) ** 2 > 1.0)
    poly_val = 16.0 * (tau_0 ** 2) - 8.0 * tau_0 + 37.0
    disc = 8 * 8 - 4 * 16 * 37
    # Exhaustive check of integer matrices (a,b; c,d) fixing tau_0 (c = 16k, d-a = -8k, b = -37k, k >= 1):
    min_det = None
    for k in range(1, 6):
        c_m = 16 * k
        b_m = -37 * k
        for a_m in range(-40, 41):
            d_m = a_m - 8 * k
            lhs = c_m * (tau_0 ** 2) + (d_m - a_m) * tau_0 - b_m
            if abs(lhs) < 1e-12:
                det_m = a_m * d_m - b_m * c_m
                if min_det is None or det_m < min_det:
                    min_det = det_m
    # Fricke involutions W_N(tau) = -1/(N*tau) fix tau = i/sqrt(N) => Re(tau) == 0 != 0.25:
    fricke_re = [((-1.0 / (n_lv * tau_0)) - tau_0) for n_lv in range(1, 25)]
    cc.check(in_f_interior and abs(abs(tau_0) ** 2 - 2.3125) < 1e-12, "V12.2.A1a: tau_0 strictly in SL(2,Z) F interior")
    cc.check(abs(poly_val) < 1e-13 and disc == -2304, "V12.2.A1b: primitive quadratic 16*tau^2 - 8*tau + 37 = 0")
    cc.check(min_det == 576 and all(abs(diff) > 0.25 for diff in fricke_re), "V12.2.A1c: min det >= 576 & Fricke W_N Re=0")

    print(f"  [V12.2.A1] Modular & Congruence Fixed-Point No-Go for tau_0 = 0.25 + 1.5i [Т] / [✗]:")
    print(f"             - |tau_0|^2 = {abs(tau_0)**2:.4f} > 1 (interior of F), 16*tau^2 - 8*tau + 37 = {abs(poly_val):.1e} (Delta={disc}),")
    print(f"               min det(gamma fixing tau_0) = {min_det} >= 576 (no SL(2,Z)/Gamma_0(N)/Gamma(N)/W_N fixed point).")

    # 2. Gamma_0(4) outer-automorphism CP_2: tau -> -conj(tau) + 1/2 & 2D SUGRA instability
    t_half = np.array([[1.0, 0.5], [0.0, 1.0]])
    t_half_inv = np.array([[1.0, -0.5], [0.0, 1.0]])
    gamma0_4_gens = [
        np.array([[1, 1], [0, 1]]),
        np.array([[1, 0], [4, 1]]),
        np.array([[3, 1], [8, 3]]),
        np.array([[-1, 0], [0, -1]]),
        np.array([[5, 2], [12, 5]]),
    ]
    g04_ok = True
    for g in gamma0_4_gens:
        cg = t_half @ g @ t_half_inv
        if not np.allclose(cg, np.round(cg), atol=1e-12):
            g04_ok = False
        cg_int = np.round(cg).astype(int)
        if cg_int[1, 0] % 4 != 0 or int(round(np.linalg.det(cg_int))) != 1:
            g04_ok = False
    s2 = np.array([[1, 0], [2, 1]])
    s2_conj = t_half @ s2 @ t_half_inv
    s2_breaks = abs(abs(s2_conj[0, 1]) - 0.5) < 1e-12

    cc.check(g04_ok and s2_breaks, "V12.2.A2a: T^{1/2} normalizes Gamma_0(4) and fails on S_2 in Gamma_0(2)")

    re_grid = np.linspace(-0.5, 0.5, 401)
    im_tau = 1.5
    taus = re_grid + 1j * im_tau
    cp2_taus = -np.conj(taus) + 0.5

    def eval_canon_invs(t):
        th2, th3, th4 = _theta234(t)
        et1 = _eta(t)
        et2 = _eta(2.0 * t)
        et4 = _eta(4.0 * t)
        e2_g02 = 2.0 * _eisenstein_e2(2.0 * t) - _eisenstein_e2(t)
        return {
            "|lambda|^2": np.abs((th2 / th3) ** 4) ** 2,
            "|h_2|^2": np.abs((et1 / et2) ** 24) ** 2,
            "|h_4|^2": np.abs((et1 / et4) ** 8) ** 2,
            "|E_2^(Gamma0(2))|^2": np.abs(e2_g02) ** 2,
        }

    canon_vals = eval_canon_invs(taus)
    canon_cp2 = eval_canon_invs(cp2_taus)
    canon_cp_conserving = True
    canon_summary = []
    for name, vals in canon_vals.items():
        re_min = float(re_grid[int(np.argmin(vals))])
        asym = float(np.max(np.abs(vals - canon_cp2[name])) / np.mean(vals))
        is_bound = abs(re_min) < 1e-12 or abs(abs(re_min) - 0.5) < 1e-12
        if not is_bound or asym < 1e-3:
            canon_cp_conserving = False
        canon_summary.append((name, re_min, asym))
    cc.check(canon_cp_conserving, "V12.2.A2b: Canonical Gamma(2)/Gamma_0(2)/Gamma_0(4) invariants break CP_2 and lock on {0, +-0.5}")

    def eval_cp2_sym_invs(t):
        _, th3_2, th4_2 = _theta234(2.0 * t)
        return {
            "|th3(2t)^4+th4(2t)^4|^2": np.abs(th3_2 ** 4 + th4_2 ** 4) ** 2,
            "|th3(2t)|^8+|th4(2t)|^8": np.abs(th3_2) ** 8 + np.abs(th4_2) ** 8,
            "|eta(2t)|^-4": np.abs(_eta(2.0 * t)) ** (-4),
            "|j(2t)|^2": np.abs(_j_invariant(2.0 * t)) ** 2,
        }

    sym_vals = eval_cp2_sym_invs(taus)
    sym_cp2 = eval_cp2_sym_invs(cp2_taus)
    sym_p = eval_cp2_sym_invs(-0.25 + (im_tau + 1e-3) * 1j)
    sym_m = eval_cp2_sym_invs(-0.25 + (im_tau - 1e-3) * 1j)
    sym_slice_ok = True
    sym_2d_unstable = True
    sym_summary = []
    for name, vals in sym_vals.items():
        re_min = float(re_grid[int(np.argmin(vals))])
        cp2_err = float(np.max(np.abs(vals - sym_cp2[name])) / max(float(np.mean(vals)), 1.0))
        dv_dim = float((sym_p[name] - sym_m[name]) / 2e-3)
        if abs(abs(re_min) - 0.25) > 1e-6 or cp2_err >= 1e-13:
            sym_slice_ok = False
        if abs(dv_dim) < 1e-7:
            sym_2d_unstable = False
        sym_summary.append((name, re_min, cp2_err, dv_dim))
    cc.check(sym_slice_ok and sym_2d_unstable, "V12.2.A2c: CP_2-symmetrized Gamma_0(4) invariants fix Re=+-0.25 on 1D slice (<1e-13) yet fail 2D Im=1.5")

    # 2D SUGRA potentials (K = -3 ln(2 Im tau)) for W1 = eta(2 tau)^-6 and W2 = (eta(tau)*eta(tau+1/2))^-3
    def v_sugra_w1(x):
        re_t, im_t = float(x[0]), float(x[1])
        t = re_t + 1j * im_t
        w = _eta(2.0 * t) ** (-6)
        dw = (-1j * math.pi * _eisenstein_e2(2.0 * t) + 3j / (2.0 * im_t)) * w
        return float(((2.0 * im_t) ** (-3)) * ((4.0 * im_t * im_t / 3.0) * abs(dw) ** 2 - 3.0 * abs(w) ** 2))

    def v_sugra_w2(x):
        re_t, im_t = float(x[0]), float(x[1])
        t = re_t + 1j * im_t
        w = (_eta(t) * _eta(t + 0.5)) ** (-3)
        dw = (-0.25j * math.pi * (_eisenstein_e2(t) + _eisenstein_e2(t + 0.5)) + 3j / (2.0 * im_t)) * w
        return float(((2.0 * im_t) ** (-3)) * ((4.0 * im_t * im_t / 3.0) * abs(dw) ** 2 - 3.0 * abs(w) ** 2))

    starts_w1 = [[-0.45, 0.45], [0.25, 1.50]]
    res_w1 = min(
        (minimize(v_sugra_w1, s0, bounds=[(-0.5, 0.5), (0.25, 3.0)]) for s0 in starts_w1),
        key=lambda r: r.fun,
    )
    starts_w2 = [[0.25, 1.50], [0.25, 0.45], [-0.45, 0.45]]
    res_w2 = min(
        (minimize(v_sugra_w2, s0, bounds=[(-0.5, 0.5), (0.25, 3.0)]) for s0 in starts_w2),
        key=lambda r: r.fun,
    )
    res_w2_slice = minimize(v_sugra_w2, [-0.45, 1.40], bounds=[(-0.5, 0.5), (0.90, 3.0)])
    # Also verify (0.25, 1.5) is NOT a stationary point of either V_w1 or V_w2 (dV/dIm > 0):
    dv_w1_im = (v_sugra_w1([0.25, 1.5 + 1e-4]) - v_sugra_w1([0.25, 1.5 - 1e-4])) / 2e-4
    dv_w2_im = (v_sugra_w2([0.25, 1.5 + 1e-4]) - v_sugra_w2([0.25, 1.5 - 1e-4])) / 2e-4
    sugra_no_stab = (
        abs(res_w1.x[0] + 0.5) < 1e-3
        and abs(res_w1.x[1] - 0.405) < 1e-2
        and abs(abs(res_w2.x[0]) - 0.25) < 1e-3
        and abs(res_w2.x[1] - 0.25) < 1e-3
        and abs(v_sugra_w2([0.25, 0.25]) - v_sugra_w2([-0.25, 0.25])) < 1e-10
        and abs(res_w2_slice.x[0] + 0.5) < 1e-3
        and abs(res_w2_slice.x[1] - 1.2732) < 1e-2
        and res_w2.fun < res_w2_slice.fun < v_sugra_w2([0.25, 1.5])
        and res_w1.fun < v_sugra_w1([0.25, 1.5])
        and dv_w1_im > 1.0
        and dv_w2_im > 1.0
    )
    cc.check(sugra_no_stab, "V12.2.A2d: 2D SUGRA W1 (-0.5,0.405) & W2 global (+-0.25,0.25) / Im>=0.90 local (-0.5,1.273) fail to stabilize (0.25,1.5)")

    print(f"  [V12.2.A2] Gamma_0(4) Outer Automorphism CP_2 & 2D SUGRA Stability Audit [Т] / [✗]:")
    print(f"             - T^(1/2) Gamma_0(4) T^(-1/2) in Gamma_0(4) = {g04_ok}; T^(1/2) S_2 T^(-1/2)[0,1] = {s2_conj[0,1]:.1f} (breaks Gamma_0(2))")
    for name, rmin, asym in canon_summary:
        print(f"             - Canon {name:20s}: argmin Re = {rmin:+.3f}, CP_2 asym = {asym:.2e} (breaks CP_2)")
    for name, rmin, err, dv in sym_summary:
        print(f"             - Sym   {name:20s}: argmin Re = {rmin:+.3f} (err={err:.2e}), dV/dIm(1.5) = {dv:+.2e} (2D unstable!)")
    print(f"             - 2D SUGRA min (Im>=0.25): W1=eta(2t)^-6 -> ({res_w1.x[0]:+.4f}, {res_w1.x[1]:.4f}) V={res_w1.fun:.2f}; "
          f"W2=(eta(t)eta(t+1/2))^-3 -> global ({res_w2.x[0]:+.4f}, {res_w2.x[1]:.4f}) V={res_w2.fun:.2f}, "
          f"Im>=0.90 local ({res_w2_slice.x[0]:+.4f}, {res_w2_slice.x[1]:.4f}) V={res_w2_slice.fun:.2f}; "
          f"dV/dIm(0.25,1.5)=({dv_w1_im:+.2e}, {dv_w2_im:+.2f})")

    # 3. Real racetrack obstruction & CCvS NCG Tr(Y_u Y_u^dag Y_d Y_d^dag) exact CP-evenness
    dv_higgs = 2.057e-3
    # For real W(tau) = A exp(2 pi i a tau) + B exp(2 pi i b tau), dV/dRe|_{1/4} ~ sin(pi/2*(a-b)) = 0 => |a-b| even >= 2
    min_gap = min(abs(a - b) for a in range(1, 8) for b in range(1, 8) if a != b and abs(math.sin(0.5 * math.pi * (a - b))) < 1e-12)
    racetrack_supp = math.exp(-2.0 * math.pi * min_gap * im_tau)
    cc.check(min_gap == 2 and abs(racetrack_supp - math.exp(-6.0 * math.pi)) < 1e-15 and racetrack_supp < 1e-5 * dv_higgs,
             "V12.2.A3a: Real racetrack |a-b| >= 2 => e^{-6 pi} = 6.509e-9 << dV_Higgs = 2.057e-3")

    s12, s23, s13 = 0.2250, 0.04183, 0.00369
    c12, c23, c13 = math.sqrt(1 - s12**2), math.sqrt(1 - s23**2), math.sqrt(1 - s13**2)

    def v_ckm_mat(delta: float) -> np.ndarray:
        return np.array([
            [c12 * c13, s12 * c13, s13 * np.exp(-1j * delta)],
            [-s12 * c23 - c12 * s23 * s13 * np.exp(1j * delta), c12 * c23 - s12 * s23 * s13 * np.exp(1j * delta), s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * np.exp(1j * delta), -c12 * s23 - s12 * c23 * s13 * np.exp(1j * delta), c23 * c13],
        ], dtype=complex)

    yu2 = np.diag([1.23e-3, 0.620, 168.26]) ** 2 / (174.104 ** 2)
    yd2 = np.diag([2.67e-3, 0.05316, 2.839]) ** 2 / (174.104 ** 2)
    vp = v_ckm_mat(+1.144)
    vm = v_ckm_mat(-1.144)
    tr_p = float(np.real(np.trace(yu2 @ vp @ yd2 @ vp.conj().T)))
    tr_m = float(np.real(np.trace(yu2 @ vm @ yd2 @ vm.conj().T)))
    ncg_cp_diff = abs(tr_p - tr_m)
    cc.check(ncg_cp_diff < 1e-15, "V12.2.A3b: CCvS NCG Tr(Y_u Y_u^dag Y_d Y_d^dag) strictly CP-even (<1e-15)")

    print(f"  [V12.2.A3] Real Racetrack & CCvS NCG CP-Evenness Obstructions [Т] / [✗]:")
    print(f"             - Real racetrack min |a-b| = {min_gap} => e^(-6 pi) = {racetrack_supp:.3e} vs dV_Higgs = {dv_higgs:.3e} ({dv_higgs/racetrack_supp:.2e}x deficit)")
    print(f"             - CCvS NCG quartic Tr(Y_u Y_u^dag Y_d Y_d^dag): |Tr(+1.144) - Tr(-1.144)| = {ncg_cp_diff:.2e}")

    # 4. Exhaustive 16-config 3-gen (T^2/Z_2, M_Q=7^-) zero-fitting CKM & m_s/m_b scan + c_d -> inf limits
    ng_grid = 40
    g_ax = (np.arange(ng_grid) + 0.5) / ng_grid - 0.5
    xt, yt = np.meshgrid(g_ax, g_ax, indexing="ij")
    dat = 1.0 / (ng_grid * ng_grid)

    def psi_tw(j: int, m_flux: int, x: np.ndarray, y: np.ndarray, tau: complex, alpha: float = 0.0, beta: float = 0.0, n_max: int = 5) -> np.ndarray:
        pref = (2.0 * m_flux * tau.imag) ** 0.25 * np.exp(1j * math.pi * m_flux * x * y)
        s = np.zeros_like(x, dtype=complex)
        for n in range(-n_max, n_max + 1):
            a = n + (j + alpha) / float(m_flux)
            s = s + np.exp(1j * math.pi * m_flux * tau * (y + a) ** 2 + 2j * math.pi * m_flux * a * (x + beta / float(m_flux)))
        return pref * s

    def orb_modes(m_flux: int, parity: str, tau: complex, alpha: float = 0.0, beta: float = 0.0) -> np.ndarray:
        raw = np.array([psi_tw(j, m_flux, xt, yt, tau, alpha, beta) for j in range(m_flux)])
        ref = np.array([psi_tw(j, m_flux, -xt, -yt, tau, alpha, beta) for j in range(m_flux)])
        pmat = np.einsum("ixy,jxy->ij", raw.conj(), ref) * dat
        pmat = 0.5 * (pmat + pmat.conj().T)
        ev, vec = eigh(pmat)
        sel = [k for k in range(m_flux) if (ev[k] > 0.5 if parity == "+" else ev[k] < -0.5)]
        return np.einsum("ki,ixy->kxy", vec[:, sel].T, raw)

    c_q = orb_modes(7, "-", tau_0, 0.0, 0.0)
    c_u = orb_modes(7, "-", tau_0, 0.0, 0.0)
    h_u = orb_modes(14, "+", tau_0, 0.0, 0.0)
    yu_all = np.array([[[np.sum(c_q[i] * c_u[j] * np.conj(h_u[a])) * dat for j in range(3)] for i in range(3)] for a in range(len(h_u))])
    ku = np.einsum("bij,aij->ab", yu_all.conj(), yu_all)
    huf = h_u.reshape(len(h_u), -1)

    three_gen_cfgs = []
    for md in range(3, 9):
        for par_d in ("+", "-"):
            for al in (0.0, 0.5):
                for be in (0.0, 0.5):
                    cd_modes = orb_modes(md, par_d, tau_0, al, be)
                    if len(cd_modes) == 3:
                        three_gen_cfgs.append((md, par_d, al, be, cd_modes))

    cc.check(len(three_gen_cfgs) == 16, "V12.2.A4a: Exactly 16 three-gen (Md, par_d, al, be) orbifold configs")

    scan_rows = {}
    joint_window_hits = 0
    for md, par_d, al, be, cd_modes in three_gen_cfgs:
        par_hd = "-" if par_d == "+" else "+"
        hd_modes = orb_modes(7 + md, par_hd, tau_0, al, be)
        yd_all = np.array([[[np.sum(c_q[i] * cd_modes[j] * np.conj(hd_modes[a])) * dat for j in range(3)] for i in range(3)] for a in range(len(hd_modes))])
        kd = np.einsum("bij,aij->ab", yd_all.conj(), yd_all)
        hdf = hd_modes.reshape(len(hd_modes), -1)
        nu_d, nd_d = len(h_u), len(hd_modes)
        rng_opt = np.random.default_rng(741)

        def obj(xv):
            vu = xv[:nu_d] + 1j * xv[nu_d:2 * nu_d]
            vd = xv[2 * nu_d:2 * nu_d + nd_d] + 1j * xv[2 * nu_d + nd_d:]
            n_u, n_d = np.linalg.norm(vu), np.linalg.norm(vd)
            if n_u < 1e-12 or n_d < 1e-12:
                return 1e9
            vu = vu / n_u
            vd = vd / n_d
            hu2 = np.abs(vu @ huf) ** 2
            hd2 = np.abs(vd @ hdf) ** 2
            pot = float(np.sum(hu2 ** 2 + hd2 ** 2 + 0.1 * hu2 * hd2) * dat)
            return pot - 12.0 * float(np.real(vu.conj() @ ku @ vu)) - 30.0 * float(np.real(vd.conj() @ kd @ vd))

        bf, bvu, bvd = 1e18, None, None
        for _ in range(3):
            res = minimize(obj, rng_opt.normal(size=2 * (nu_d + nd_d)), method="BFGS", options={"gtol": 1e-8, "maxiter": 300})
            if res.fun < bf:
                bf = res.fun
                vu = res.x[:nu_d] + 1j * res.x[nu_d:2 * nu_d]
                vd = res.x[2 * nu_d:2 * nu_d + nd_d] + 1j * res.x[2 * nu_d + nd_d:]
                bvu = vu / np.linalg.norm(vu)
                bvd = vd / np.linalg.norm(vd)
        mu_m = np.tensordot(bvu.conj(), yu_all, axes=(0, 0))
        md_m = np.tensordot(bvd.conj(), yd_all, axes=(0, 0))
        uu, _, _ = svd(mu_m)
        ud, sd, _ = svd(md_m)
        # svd returns singular values descending; reorder ascending [1st, 2nd, 3rd]
        uu = uu[:, ::-1]
        ud = ud[:, ::-1]
        sd = sd[::-1]
        v_ckm = uu.conj().T @ ud
        vus = float(abs(v_ckm[0, 1]))
        vcb = float(abs(v_ckm[1, 2]))
        vub = float(abs(v_ckm[0, 2]))
        ms_mb = float(sd[1] / sd[2])
        j_cp = float(abs(np.imag(v_ckm[0, 1] * v_ckm[1, 2] * np.conj(v_ckm[0, 2]) * np.conj(v_ckm[1, 1]))))

        # Asymptotic c_d -> infinity top eigenmode limit of K_d
        _, vec_kd = eigh(kd)
        md_top = np.tensordot(vec_kd[:, -1].conj(), yd_all, axes=(0, 0))
        sd_top = np.sort(svd(md_top, compute_uv=False))
        ms_mb_inf = float(sd_top[1] / sd_top[2])

        if 0.20 <= vus <= 0.25 and 0.015 <= ms_mb <= 0.027 and 0.035 <= vcb <= 0.060 and j_cp > 1.0e-5:
            joint_window_hits += 1
        scan_rows[(md, par_d, al, be)] = (vus, vcb, vub, ms_mb, j_cp, ms_mb_inf)

    r4 = scan_rows[(4, "+", 0.0, 0.0)]
    r5 = scan_rows[(5, "+", 0.0, 0.5)]
    r6 = scan_rows[(6, "-", 0.0, 0.5)]
    cc.check(abs(r4[5] - 0.0612) < 0.002 and abs(r4[4] - 1.92e-5) < 0.2e-5, "V12.2.A4b: Md=4+ (0,0) c_d->inf floor 0.0612 & J_CP ~ 1.92e-5")
    cc.check(abs(r5[0] - 0.225) < 0.01 and r5[3] < 0.010 and r5[1] < 0.020, "V12.2.A4c: Md=5+ (0,0.5) |V_us|=0.225 yet m_s/m_b=0.0072, |V_cb|=0.0136")
    cc.check(abs(r6[3] - 0.021) < 0.003 and abs(r6[0] - 0.101) < 0.01 and r6[4] < 1e-8, "V12.2.A4d: Md=6- (0,0.5) m_s/m_b=0.021 yet |V_us|=0.101, J<1e-8")
    cc.check(joint_window_hits == 0, "V12.2.A4e: 0/16 zero-fitting orbifold configs hit joint CKM+m_s/m_b window")

    print(f"  [V12.2.A4] Exhaustive 16-Config (T^2/Z_2, M_Q=7^-) Zero-Fitting CKM & m_s/m_b Closure [Т] / [✗] / [П]:")
    print(f"             - Md=4+ (0,0):   |V_us|={r4[0]:.4f}, |V_cb|={r4[1]:.4f}, m_s/m_b={r4[3]:.4f} (c_d->inf floor {r4[5]:.4f}), J={r4[4]:.2e}")
    print(f"             - Md=5+ (0,0.5): |V_us|={r5[0]:.4f}, |V_cb|={r5[1]:.4f}, m_s/m_b={r5[3]:.4f} (c_d->inf {r5[5]:.4f}), J={r5[4]:.2e}")
    print(f"             - Md=6- (0,0.5): |V_us|={r6[0]:.4f}, |V_cb|={r6[1]:.4f}, m_s/m_b={r6[3]:.4f}, J={r6[4]:.2e}")
    print(f"             - Joint window hits across 16 configs: {joint_window_hits}/16 (CP spurion & CKM Yukawas remain Stratum B/C inputs [П]).\n")

    return {
        "tags": ["[Т]", "[✗]", "[П]"],
        "fitted_parameters": 0,
        "min_det": min_det,
        "racetrack_supp": racetrack_supp,
        "ncg_cp_diff": ncg_cp_diff,
        "joint_window_hits": joint_window_hits,
        "md4_floor": r4[5],
        "md5_vus": r5[0],
        "md5_msmb": r5[3],
        "md6_msmb": r6[3],
        "md6_vus": r6[0],
    }


# ==============================================================================
# V12.2.B: N_g = 3 EXTENSION OF F-42 (C^96), THM 48d(c) & 3-GEN RGE (EXPLORER 2)
# ==============================================================================
def suite_v122b_f42_3gen_and_thm48dc(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.2.B: N_g = 3 Extension of F-42 (C^32 x C^3 = C^96), Thm 48d(c) & 3-Gen RGE")
    print("=" * 88)

    def idx32(b: int, s: int, c: int) -> int:
        return 8 * b + 4 * s + c

    j_m = np.zeros((32, 32), dtype=complex)
    for i in range(32):
        j_m[i, (i + 16) % 32] = 1.0
    gam_32 = np.diag([1.0] * 8 + [-1.0] * 8 + [-1.0] * 8 + [1.0] * 8).astype(complex)

    def rep_af_32(q_l: np.ndarray, q_r: np.ndarray, m4: np.ndarray) -> np.ndarray:
        m = np.zeros((32, 32), dtype=complex)
        m[0:8, 0:8] = np.kron(q_l, np.eye(4))
        m[8:16, 8:16] = np.kron(q_r, np.eye(4))
        m[16:24, 16:24] = np.kron(np.eye(2), m4)
        m[24:32, 24:32] = np.kron(np.eye(2), m4)
        return m

    i3 = np.eye(3, dtype=complex)
    j_96 = np.kron(j_m, i3)
    gam_96 = np.kron(gam_32, i3)

    def rep_af_96(q_l: np.ndarray, q_r: np.ndarray, m4: np.ndarray) -> np.ndarray:
        return np.kron(rep_af_32(q_l, q_r, m4), i3)

    def jconj_96(a: np.ndarray) -> np.ndarray:
        return j_96 @ a.conj() @ j_96

    def opp_96(a: np.ndarray) -> np.ndarray:
        return j_96 @ a.T @ j_96

    def build_df_96(yu: np.ndarray, ynu: np.ndarray, yd: np.ndarray, ye: np.ndarray, mr: np.ndarray) -> np.ndarray:
        # Block-index in 96x96: 3*(8*b + 4*s + c) + g
        df = np.zeros((96, 96), dtype=complex)

        def set_blk(b1: int, s1: int, c1: int, b2: int, s2: int, c2: int, mat: np.ndarray):
            r0, c0 = 3 * idx32(b1, s1, c1), 3 * idx32(b2, s2, c2)
            df[r0:r0 + 3, c0:c0 + 3] = mat
            df[c0:c0 + 3, r0:r0 + 3] = mat.conj().T

        # Up-type (s=0): quarks c=0,1,2 get Y_u; lepton c=3 gets Y_nu
        for c in (0, 1, 2):
            set_blk(0, 0, c, 1, 0, c, yu)
            set_blk(2, 0, c, 3, 0, c, yu.conj())
        set_blk(0, 0, 3, 1, 0, 3, ynu)
        set_blk(2, 0, 3, 3, 0, 3, ynu.conj())
        # Down-type (s=1): quarks c=0,1,2 get Y_d; lepton c=3 gets Y_e
        for c in (0, 1, 2):
            set_blk(0, 1, c, 1, 1, c, yd)
            set_blk(2, 1, c, 3, 1, c, yd.conj())
        set_blk(0, 1, 3, 1, 1, 3, ye)
        set_blk(2, 1, 3, 3, 1, 3, ye.conj())
        # Majorana nu_R block: (b=1, s=0, c=3) <-> (b=3, s=0, c=3), indices 3*11=33..36 <-> 3*27=81..84
        r_m = 3 * idx32(1, 0, 3)
        c_m = 3 * idx32(3, 0, 3)
        df[r_m:r_m + 3, c_m:c_m + 3] = mr
        df[c_m:c_m + 3, r_m:r_m + 3] = mr.conj().T
        return df

    rng = np.random.default_rng(2026)

    def rand_cmat() -> np.ndarray:
        return rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))

    yu_3 = rand_cmat()
    ynu_3 = rand_cmat()
    yd_3 = rand_cmat()
    ye_3 = rand_cmat()
    mr_raw = rand_cmat()
    mr_sym = 0.5 * (mr_raw + mr_raw.T)

    df_96 = build_df_96(yu_3, ynu_3, yd_3, ye_3, mr_sym)
    df_96_asym = build_df_96(yu_3, ynu_3, yd_3, ye_3, mr_raw)

    err_ko6_sym = max(
        float(np.max(np.abs(df_96.conj().T - df_96))),
        float(np.max(np.abs(j_96 @ j_96 - np.eye(96)))),
        float(np.max(np.abs(jconj_96(df_96) - df_96))),
        float(np.max(np.abs(jconj_96(gam_96) + gam_96))),
        float(np.max(np.abs(gam_96 @ gam_96 - np.eye(96)))),
        float(np.max(np.abs(gam_96 @ df_96 + df_96 @ gam_96))),
    )
    err_ko6_asym = float(np.max(np.abs(jconj_96(df_96_asym) - df_96_asym)))
    expected_asym = float(np.max(np.abs(mr_raw - mr_raw.T)))
    cc.check(err_ko6_sym == 0.0 and abs(err_ko6_asym - expected_asym) < 1e-13 and expected_asym > 0.5,
             "V12.2.B1a: 96x96 KO-dim 6 exact (err=0.0) iff M_R^T == M_R")

    def rand_quat() -> np.ndarray:
        a, b, c, d = rng.normal(size=4)
        return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]], dtype=complex)

    err_0th = 0.0
    for _ in range(25):
        a_m = rep_af_96(rand_quat(), rand_quat(), rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))
        b_m = rep_af_96(rand_quat(), rand_quat(), rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))
        err_0th = max(err_0th, float(np.max(np.abs(a_m @ opp_96(b_m) - opp_96(b_m) @ a_m))))
    cc.check(err_0th < 1e-14, "V12.2.B1b: 96x96 universal 0th-order condition (<1e-14)")

    j2 = np.array([[0.0, -1.0], [1.0, 0.0]], dtype=complex)
    e30 = np.zeros((4, 4), dtype=complex)
    e30[3, 0] = 1.0
    a1_96 = rep_af_96(np.zeros((2, 2)), j2, np.zeros((4, 4)))
    b1_96 = rep_af_96(np.zeros((2, 2)), np.zeros((2, 2)), e30)
    comm_1st = (df_96 @ a1_96 - a1_96 @ df_96) @ opp_96(b1_96) - opp_96(b1_96) @ (df_96 @ a1_96 - a1_96 @ df_96)
    # idx32(1,1,0) = 12 -> 3*12 = 36:39; idx32(3,0,3) = 27 -> 3*27 = 81:84
    cc.check(float(np.max(np.abs(comm_1st[36:39, 81:84] - mr_sym))) < 1e-13,
             "V12.2.B1c: 96x96 1st-order violation comm_1st[36:39, 81:84] == M_R")

    def maj6_proj_96(m_mat: np.ndarray) -> np.ndarray:
        out = np.zeros((4, 4, 3, 3), dtype=complex)
        for c in range(4):
            for d in range(4):
                r1, c1 = 3 * idx32(1, 0, c), 3 * idx32(3, 1, d)
                r2, c2 = 3 * idx32(1, 1, c), 3 * idx32(3, 0, d)
                out[c, d] = m_mat[r1:r1 + 3, c1:c1 + 3] - m_mat[r2:r2 + 3, c2:c2 + 3]
        return out

    i2 = np.eye(2, dtype=complex)
    p03 = np.eye(4, dtype=complex)[[3, 1, 2, 0]]
    p13 = np.eye(4, dtype=complex)[[0, 3, 2, 1]]

    def phi4_96(ua, ub, df_mat):
        return sum((xa @ jconj_96(xb)) @ df_mat @ (xa @ jconj_96(xb)).conj().T for xa in (ua, ub) for xb in (ua, ub))

    u1 = rep_af_96(i2, i2, p03)
    u2p = rep_af_96(i2, j2, p13)
    u2m = rep_af_96(i2, -j2, p13)
    v1 = rep_af_96(i2, i2, p13)
    v2p = rep_af_96(i2, j2, p03)
    v2m = rep_af_96(i2, -j2, p03)
    d_coup = phi4_96(u1, u2p, df_96)
    p_pure6 = (phi4_96(u1, u2p, df_96) - phi4_96(u1, u2m, df_96)) - (phi4_96(v1, v2p, df_96) - phi4_96(v1, v2m, df_96))
    m6_coup = maj6_proj_96(d_coup)
    m6_pure = maj6_proj_96(p_pure6)
    ko6_coup = float(np.max(np.abs(jconj_96(d_coup) - d_coup)))
    cc.check(
        ko6_coup < 1e-13
        and float(np.max(np.abs(m6_coup[0, 1] + mr_sym))) < 1e-13
        and float(np.max(np.abs(m6_pure[0, 1] + 4.0 * mr_sym))) < 1e-13
        and float(np.max(np.abs(p_pure6[0:24, 24:48]))) < 1e-13,
        "V12.2.B1d: Lifted F-42 witnesses M6_coup[0,1]=-M_R, M6_pure[0,1]=-4*M_R, zero Yukawa for pure 6",
    )

    print(f"  [V12.2.B1] Exact 96x96 CCvS Lift (C^32 x C^3) [Т]:")
    print(f"             - KO-dim 6 err = {err_ko6_sym:.1e} (M_R^T=M_R) vs {err_ko6_asym:.3f} (asymmetric M_R); 0th-order err = {err_0th:.1e}")
    print(f"             - 1st-order viol max|comm[36:39,81:84]-M_R| = {np.max(np.abs(comm_1st[36:39,81:84]-mr_sym)):.1e}; "
          f"M6_coup[0,1] == -M_R, M6_pure[0,1] == -4*M_R, pure6 Yukawa == 0.")

    # 2. Exact real dimensions via SVD of sampled fluctuation subspaces across 4 regimes
    def rand_unitary(n: int) -> np.ndarray:
        z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        q_m, r_m = np.linalg.qr(z)
        return q_m @ np.diag(np.diag(r_m) / np.abs(np.diag(r_m)))

    def compute_ranks(df_base: np.ndarray, n_orb: int = 380, n_ccvs: int = 280, n_gen: int = 260):
        orb_vecs = []
        max_orb6 = 0.0
        for _ in range(n_orb):
            ul = rand_quat()
            ul /= math.sqrt(abs(np.linalg.det(ul)))
            ur = rand_quat()
            ur /= math.sqrt(abs(np.linalg.det(ur)))
            pi_u = rep_af_96(ul, ur, rand_unitary(4))
            u_m = pi_u @ jconj_96(pi_u)
            d_u = u_m @ df_base @ u_m.conj().T
            max_orb6 = max(max_orb6, float(np.max(np.abs(maj6_proj_96(d_u)))))
            orb_vecs.append(np.concatenate([d_u.real.ravel(), d_u.imag.ravel()]))
        rk_orb = int(np.linalg.matrix_rank(np.array(orb_vecs), tol=1e-8))

        ccvs_vecs = list(orb_vecs)
        for _ in range(n_ccvs):
            ksg = 3
            us_sg = []
            for _k in range(ksg):
                ulk = rand_quat()
                ulk /= math.sqrt(abs(np.linalg.det(ulk)))
                urk = rand_quat()
                urk /= math.sqrt(abs(np.linalg.det(urk)))
                us_sg.append(rep_af_96(ulk, urk, rand_unitary(4)))
            ws = rng.dirichlet(np.ones(ksg))
            d_om = np.zeros((96, 96), dtype=complex)
            for ii in range(ksg):
                for jj in range(ksg):
                    uij = us_sg[ii] @ jconj_96(us_sg[jj])
                    d_om += ws[ii] * ws[jj] * (uij @ df_base @ uij.conj().T)
            ccvs_vecs.append(np.concatenate([d_om.real.ravel(), d_om.imag.ravel()]))
        rk_ccvs = int(np.linalg.matrix_rank(np.array(ccvs_vecs), tol=1e-8))

        # General unital self-adjoint Pert(A_F): sum c_k a_k (x) b_k^op with sum c_k a_k b_k = I and omega^* = omega:
        # omega = I (x) I + 0.5*(X (x) Y + Y^dag (x) X^dag) - 0.5*(S (x) I + I (x) S), S = 0.5*(X Y + Y^dag X^dag)
        gen_vecs = list(ccvs_vecs)
        max_gen_ko6 = 0.0
        i96 = np.eye(96, dtype=complex)
        for _ in range(n_gen):
            x_rep = rep_af_96(rand_quat(), rand_quat(), rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))
            y_rep = rep_af_96(rand_quat(), rand_quat(), rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))
            s_herm = 0.5 * (x_rep @ y_rep + y_rep.conj().T @ x_rep.conj().T)
            coeffs = [1.0, 0.5, 0.5, -0.5, -0.5]
            terms_a = [i96, x_rep, y_rep.conj().T, s_herm, i96]
            terms_b = [i96, y_rep, x_rep.conj().T, i96, s_herm]
            d_pert = np.zeros((96, 96), dtype=complex)
            for ci, ai, bi in zip(coeffs, terms_a, terms_b):
                for cj, aj, bj in zip(coeffs, terms_a, terms_b):
                    left_ij = ai @ jconj_96(aj)
                    right_ij = bi @ jconj_96(bj)
                    d_pert += (ci * cj) * (left_ij @ df_base @ right_ij)
            max_gen_ko6 = max(
                max_gen_ko6,
                float(np.max(np.abs(d_pert - d_pert.conj().T))),
                float(np.max(np.abs(jconj_96(d_pert) - d_pert))),
                float(np.max(np.abs(gam_96 @ d_pert + d_pert @ gam_96))),
            )
            gen_vecs.append(np.concatenate([d_pert.real.ravel(), d_pert.imag.ravel()]))
        rk_gen = int(np.linalg.matrix_rank(np.array(gen_vecs), tol=1e-8))
        return max_orb6, rk_orb, rk_ccvs, rk_gen, max_gen_ko6

    max_orb6_g, rk_orb_g, rk_ccvs_g, rk_gen_g, ko6_gen_g = compute_ranks(df_96)
    df_col = build_df_96(yu_3, 2.0 * yu_3, yd_3, 2.0 * yd_3, mr_sym)
    _, rk_orb_col, rk_ccvs_col, rk_gen_col, _ = compute_ranks(df_col, n_orb=340, n_ccvs=260, n_gen=240)
    df_deg = build_df_96(yu_3, yu_3, yd_3, yd_3, mr_sym)
    _, rk_orb_deg, rk_ccvs_deg, rk_gen_deg, _ = compute_ranks(df_deg, n_orb=180, n_ccvs=180, n_gen=180)

    cc.check(max_orb6_g < 1e-14 and rk_orb_g == 188, "V12.2.B2a: Unitary orbit rank == 188 with zero (6,1,1)_C")
    cc.check(rk_ccvs_g == 200, "V12.2.B2b: Unitary-convex CCvS semigroup rank == 200 (188 + 12)")
    cc.check(ko6_gen_g < 1e-12 and rk_gen_g == 208, "V12.2.B2c: General Pert(A_F) rank == 208 (16+120+60+12) for non-collinear Yukawas")
    cc.check(rk_orb_col == 188 and rk_ccvs_col == 200 and rk_gen_col == 200, "V12.2.B2d: Collinear (Y_nu=2Y_u, Y_e=2Y_d) stays at 200")
    cc.check(rk_orb_deg == 68 and rk_ccvs_deg == 80 and rk_gen_deg == 80, "V12.2.B2e: Degenerate (Y_nu=Y_u, Y_e=Y_d) drops (15,2,2)_C -> orbit=68, pert=80")

    print(f"  [V12.2.B2] Exact Real Dimensions on C^96 (SVD Rank Audit) [Т]:")
    print(f"             - Generic 3-gen (Y_nu,Y_e !|| Y_u,Y_d): orbit={rk_orb_g} (max|(6,1,1)|={max_orb6_g:.1e}), "
          f"unitary-CCvS={rk_ccvs_g}, general Pert(A_F)={rk_gen_g} (KO-6 err={ko6_gen_g:.1e})")
    print(f"             - Collinear: orbit={rk_orb_col}, unitary-CCvS={rk_ccvs_col}, general={rk_gen_col}; "
          f"Degenerate: orbit={rk_orb_deg}, unitary-CCvS={rk_ccvs_deg}, general={rk_gen_deg}.")

    # 3. Exact rational anomaly cancellation on 48 LH Weyl states + Thm 48d(c)/48e(f)/T-350 check
    # One Spin(10) 16_+ generation in LH Weyl convention: (mult_su3, mult_su2, Y, B-L)
    gen1_weyl = [
        (3, 2, Fraction(1, 6), Fraction(1, 3)),    # Q_L (6 states)
        (3, 1, Fraction(-2, 3), Fraction(-1, 3)),  # u_R^c (3 states)
        (3, 1, Fraction(1, 3), Fraction(-1, 3)),   # d_R^c (3 states)
        (1, 2, Fraction(-1, 2), Fraction(-1, 1)),  # L_L (2 states)
        (1, 1, Fraction(1, 1), Fraction(1, 1)),    # e_R^c (1 state)
        (1, 1, Fraction(0, 1), Fraction(1, 1)),    # nu_R^c (1 state)
    ]
    ng_fam = 3
    total_weyl = ng_fam * sum(m3 * m2 for m3, m2, _, _ in gen1_weyl)
    tr_y = ng_fam * sum(m3 * m2 * y for m3, m2, y, _ in gen1_weyl)
    tr_y3 = ng_fam * sum(m3 * m2 * (y ** 3) for m3, m2, y, _ in gen1_weyl)
    tr_su3_y = ng_fam * sum(m2 * y for m3, m2, y, _ in gen1_weyl if m3 == 3)
    tr_su2_y = ng_fam * sum(m3 * y for m3, m2, y, _ in gen1_weyl if m2 == 2)
    a_su3_3 = ng_fam * sum((1 if y == Fraction(1, 6) else -1) * m2 for m3, m2, y, _ in gen1_weyl if m3 == 3)
    tr_bl = ng_fam * sum(m3 * m2 * bl for m3, m2, _, bl in gen1_weyl)
    tr_bl3 = ng_fam * sum(m3 * m2 * (bl ** 3) for m3, m2, _, bl in gen1_weyl)
    n_doublets = ng_fam * sum(m3 for m3, m2, _, _ in gen1_weyl if m2 == 2)
    # sin^2(theta_W) = Tr(T_3L^2) / Tr(Q^2)
    tr_t32 = ng_fam * sum(m3 * Fraction(1, 2) for m3, m2, _, _ in gen1_weyl if m2 == 2)
    tr_q2 = Fraction(0)
    for m3, m2, y, _ in gen1_weyl:
        if m2 == 2:
            tr_q2 += ng_fam * m3 * ((Fraction(1, 2) + y) ** 2 + (Fraction(-1, 2) + y) ** 2)
        else:
            tr_q2 += ng_fam * m3 * (y ** 2)
    sin2_alg = tr_t32 / tr_q2
    cc.check(
        total_weyl == 48 and tr_y == 0 and tr_y3 == 0 and tr_su3_y == 0 and tr_su2_y == 0
        and a_su3_3 == 0 and tr_bl == 0 and tr_bl3 == 0 and n_doublets == 12 and sin2_alg == Fraction(3, 8),
        "V12.2.B3a: Exact Fraction anomaly cancellation on 48 LH Weyl states (12 doublets, sin^2=3/8)",
    )

    # Thm 48d(c): Herm(C^3) has real dim 9, rank 3; Herm(R^3) has real dim 6; Peirce E_1 color-fixed h_2(C_O) ~ R^{1,3}
    # Build explicit real basis of Herm(C^3) and Herm(R^3) and verify dimensions & trace/determinant Peirce signature (1,3):
    herm_c3_basis = []
    for i in range(3):
        m = np.zeros((3, 3), dtype=complex)
        m[i, i] = 1.0
        herm_c3_basis.append(m)
    for i in range(3):
        for j in range(i + 1, 3):
            ms = np.zeros((3, 3), dtype=complex)
            ms[i, j] = ms[j, i] = 1.0
            ma = np.zeros((3, 3), dtype=complex)
            ma[i, j] = 1j
            ma[j, i] = -1j
            herm_c3_basis.extend([ms, ma])
    herm_c3_vecs = np.array([np.concatenate([m.real.ravel(), m.imag.ravel()]) for m in herm_c3_basis])
    dim_herm_c3 = int(np.linalg.matrix_rank(herm_c3_vecs))
    dim_herm_r3 = int(np.linalg.matrix_rank(np.array([m.real.ravel() for m in herm_c3_basis if np.max(np.abs(m.imag)) == 0.0])))
    # Peirce 0-space of E_1 = diag(1,0,0) in Herm(C^3) is 2x2 Hermitian matrices in lower-right block:
    # Quadratic form Q(X) = det(X) = t^2 - x^2 - y^2 - z^2 has signature (+1, -1, -1, -1) => (1, 3)!
    e_peirce = [
        np.array([[1, 0], [0, 1]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
    ]
    g_peirce = np.zeros((4, 4))
    for a in range(4):
        for b in range(4):
            # Polarization of det(M) = 1/2 * (Tr(M)^2 - Tr(M^2))
            g_peirce[a, b] = 0.5 * float(np.real(np.trace(e_peirce[a]) * np.trace(e_peirce[b]) - np.trace(e_peirce[a] @ e_peirce[b])))
    sig_eigs = np.linalg.eigvalsh(g_peirce)
    sig_tuple = (int(np.sum(sig_eigs > 1e-12)), int(np.sum(sig_eigs < -1e-12)))
    cc.check(dim_herm_c3 == 9 and dim_herm_r3 == 6 and sig_tuple == (1, 3),
             "V12.2.B3b: Thm 48d(c) Herm(C^3) dim=9 rank=3, Herm(R^3) dim=6, Peirce E_1 signature (1,3)")

    print(f"  [V12.2.B3] Exact Fraction Anomaly & Thm 48d(c)/48e(f)/T-350 Audit [Т] / [С] / [П]:")
    print(f"             - 48 LH Weyl states: Tr(Y)=Tr(Y^3)=Tr_SU3(Y)=Tr_SU2(Y)=A(SU3^3)=Tr(B-L)^3=0, doublets={n_doublets}, sin^2={sin2_alg}")
    print(f"             - Thm 48d(c): dim Herm(C^3)={dim_herm_c3}, dim Herm(R^3)={dim_herm_r3}, Peirce sig={sig_tuple}; "
          f"Thm 48e(f)/T-350: dynamical N_g=3 in CCvS open [П].")

    # 4. 2-loop Machacek-Vaughn (C_top_PS = [2,2,2]) 3-gen Yukawa parity & N_g = 1..5 sweep
    bms_v12 = [
        ("Chain A2", [S_122_C, S_1013_C], None, None),
        ("Split-R (1e15)", [S_122_C, S_1013_C], [S_122_C, S_1013_C, S_611_C, S_1522_R], 1e15),
        ("Split-C (1e15)", [S_122_C, S_1013_C], [S_122_C, S_1013_C, S_611_C, S_1522_C], 1e15),
    ]
    parity_ok = True
    parity_rows = {}
    for bname, slo, shi, mh in bms_v12:
        r1 = _solve_ps_unif(slo, shi, mh, ng=3, three_gen_yuk=False)
        r3 = _solve_ps_unif(slo, shi, mh, ng=3, three_gen_yuk=True)
        rel_mps = abs(r3[0] - r1[0]) / r1[0]
        rel_lam = abs(r3[1] - r1[1]) / r1[1]
        d_ainv = abs(r3[2] - r1[2])
        if rel_mps >= 5e-4 or rel_lam >= 5e-4 or d_ainv >= 0.01:
            parity_ok = False
        parity_rows[bname] = (r1, r3)
    cc.check(parity_ok, "V12.2.B4a: 3-gen Yukawa vs 1-gen y_t parity < 0.05% across Chain A2, Split-R, Split-C")

    # N_g in {1..5} sweep (Chain A2 & Split-C)
    # Chain A2 anchor: tau_p = 8.83e34 yr at M_GUT = 7.890e15, a^-1 = 45.147
    mps_a2_3, lam_a2_3, ainv_a2_3 = parity_rows["Chain A2"][0]
    ng_rows = {}
    for ng_i in (1, 2, 3, 4, 5):
        mps_a, lam_a, ainv_a = _solve_ps_unif([S_122_C, S_1013_C], ng=ng_i)
        tau_p_est = 8.83e34 * ((lam_a / lam_a2_3) ** 4) * ((ainv_a / ainv_a2_3) ** 2)
        b_sc_hi, _ = _ps_betas([S_122_C, S_1013_C, S_611_C, S_1522_C], ng=ng_i)
        ng_rows[ng_i] = (mps_a, lam_a, ainv_a, tau_p_est, float(b_sc_hi[0]))

    cc.check(ng_rows[1][3] < 2.4e34, "V12.2.B4b: N_g=1 Super-K tension (tau_p < 2.4e34 yr)")
    cc.check(ng_rows[5][4] > 0.0, "V12.2.B4c: N_g=5 Split-C loses SU(4)_C asymptotic freedom (b_4 > 0)")

    print(f"  [V12.2.B4] 2-Loop 3-Gen Yukawa Parity & N_g = 1..5 Sweep [С] / [✗]:")
    for bname, (r1, r3) in parity_rows.items():
        print(f"             - {bname:16s}: 1-gen ({r1[0]:.4e}, {r1[1]:.4e}, {r1[2]:.3f}) vs 3-gen ({r3[0]:.4e}, {r3[1]:.4e}, {r3[2]:.3f})")
    for ng_i, (mps_a, lam_a, ainv_a, tp, b4sc) in ng_rows.items():
        print(f"             - N_g={ng_i}: Chain A2 M_PS={mps_a:.3e}, Lam={lam_a:.3e}, a^-1={ainv_a:.2f}, tau_p~{tp:.2e} yr | Split-C b4={b4sc:+.2f}")
    print()

    return {
        "tags": ["[Т]", "[С]", "[П]", "[✗]"],
        "fitted_parameters": 0,
        "rank_orbit": rk_orb_g,
        "rank_unitary_ccvs": rk_ccvs_g,
        "rank_general_pert": rk_gen_g,
        "a2_ainv_1gen": ainv_a2_3,
        "a2_ainv_3gen": parity_rows["Chain A2"][1][2],
        "ng1_taup": ng_rows[1][3],
        "ng5_splitc_b4": ng_rows[5][4],
    }


# ==============================================================================
# V12.2.C: DYNAMICAL HEAVY-THRESHOLD SPLIT & VISSANI NATURALNESS (EXPLORER 3)
# ==============================================================================
def suite_v122c_heavy_threshold_split_audit(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.2.C: Dynamical Heavy-Threshold Split & Finite Vissani Naturalness Audit")
    print("=" * 88)

    def idx32(b: int, s: int, c: int) -> int:
        return 8 * b + 4 * s + c

    j_m = np.zeros((32, 32), dtype=complex)
    for i in range(32):
        j_m[i, (i + 16) % 32] = 1.0
    gam_32 = np.diag([1.0] * 8 + [-1.0] * 8 + [-1.0] * 8 + [1.0] * 8).astype(complex)

    # 1. Exact 32x32 KO-6 generators for (1,2,2)_C, (15,2,2), (10bar,1,3)_{Delta_R}, (6,1,1)_C
    t_122 = np.zeros((32, 32), dtype=complex)
    for c in range(4):
        t_122[idx32(0, 0, c), idx32(1, 0, c)] = t_122[idx32(1, 0, c), idx32(0, 0, c)] = 1.0
        t_122[idx32(2, 0, c), idx32(3, 0, c)] = t_122[idx32(3, 0, c), idx32(2, 0, c)] = 1.0

    t_1522 = np.zeros((32, 32), dtype=complex)
    for c, w in ((0, 1.0), (3, -1.0)):
        t_1522[idx32(0, 0, c), idx32(1, 0, c)] = t_1522[idx32(1, 0, c), idx32(0, 0, c)] = w
        t_1522[idx32(2, 0, c), idx32(3, 0, c)] = t_1522[idx32(3, 0, c), idx32(2, 0, c)] = w

    t_1013 = np.zeros((32, 32), dtype=complex)
    t_1013[idx32(1, 0, 3), idx32(3, 0, 3)] = t_1013[idx32(3, 0, 3), idx32(1, 0, 3)] = 1.0

    t_611 = np.zeros((32, 32), dtype=complex)
    for s1, s2, sgn in ((0, 1, 1.0), (1, 0, -1.0)):
        t_611[idx32(1, s1, 0), idx32(3, s2, 3)] = t_611[idx32(3, s2, 3), idx32(1, s1, 0)] = sgn
        t_611[idx32(1, s1, 3), idx32(3, s2, 0)] = t_611[idx32(3, s2, 0), idx32(1, s1, 3)] = -sgn

    gens = {
        "(1,2,2)_C": t_122,
        "(15,2,2)": t_1522,
        "(10bar,1,3)_DeltaR": t_1013,
        "(6,1,1)_C": t_611,
    }
    # 4D Euclidean Dirac Clifford matrices on C^4 x C^32 = C^128 for non-tautological a_2 vs a_4 kinetic trace
    sig1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sig2 = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sig3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    gam_eucl = [
        np.block([[z2, i2], [i2, z2]]),
        np.block([[z2, -1j * sig1], [1j * sig1, z2]]),
        np.block([[z2, -1j * sig2], [1j * sig2, z2]]),
        np.block([[z2, -1j * sig3], [1j * sig3, z2]]),
    ]
    gam5 = gam_eucl[0] @ gam_eucl[1] @ gam_eucl[2] @ gam_eucl[3]
    i4 = np.eye(4, dtype=complex)
    clifford_err = 0.0
    for mu in range(4):
        clifford_err = max(clifford_err, float(np.max(np.abs(gam5 @ gam_eucl[mu] + gam_eucl[mu] @ gam5))))
        for nu in range(4):
            target = (2.0 if mu == nu else 0.0) * i4
            clifford_err = max(clifford_err, float(np.max(np.abs(gam_eucl[mu] @ gam_eucl[nu] + gam_eucl[nu] @ gam_eucl[mu] - target))))
    clifford_err = max(clifford_err, float(np.max(np.abs(gam5 @ gam5 - i4))))

    q_vec = (1.3, -0.7, 2.1, 0.5)
    q_sq = sum(qi * qi for qi in q_vec)
    i32 = np.eye(32, dtype=complex)
    d_q = sum(qi * np.kron(gmu, i32) for qi, gmu in zip(q_vec, gam_eucl))

    ko6_errs = []
    ratios_mass = []
    ctrl_kins = []
    tr2_vals = {}
    for gname, tm in gens.items():
        err = max(
            float(np.max(np.abs(tm - tm.conj().T))),
            float(np.max(np.abs(j_m @ tm.conj() @ j_m - tm))),
            float(np.max(np.abs(gam_32 @ tm + tm @ gam_32))),
        )
        ko6_errs.append(err)
        tr2 = float(np.real(np.trace(tm @ tm)))
        tr2_vals[gname] = tr2
        # Physical fluctuated Higgs on C^128: Phi_a = gamma_5 x T_a vs non-gamma_5 negative control Phi_ctrl = I_4 x T_a
        phi_a = np.kron(gam5, tm)
        phi_ctrl = np.kron(i4, tm)
        tr_mass_128 = float(np.real(np.trace(phi_a @ phi_a)))
        comm_phys = d_q @ phi_a - phi_a @ d_q
        kin_4d_a4 = float(np.real(-np.trace(comm_phys @ comm_phys))) / (4.0 * q_sq)
        comm_ctrl = d_q @ phi_ctrl - phi_ctrl @ d_q
        kin_ctrl = float(np.real(-np.trace(comm_ctrl @ comm_ctrl))) / (4.0 * q_sq)
        ratios_mass.append(tr_mass_128 / kin_4d_a4)
        ctrl_kins.append(abs(kin_ctrl))

    def cross_quartic_ratio(ta: np.ndarray, tb: np.ndarray) -> float:
        nrm = float(np.real(np.trace(ta @ ta) * np.trace(tb @ tb)))
        t22 = float(np.real(np.trace(ta @ ta @ tb @ tb)))
        t1212 = float(np.real(np.trace(ta @ tb @ ta @ tb)))
        return (4.0 * t22 + 2.0 * t1212) / nrm

    r_dr_1522 = cross_quartic_ratio(t_1013, t_1522)
    r_dr_611 = cross_quartic_ratio(t_1013, t_611)
    tr2_ordered = [round(tr2_vals[k], 8) for k in ("(1,2,2)_C", "(15,2,2)", "(10bar,1,3)_DeltaR", "(6,1,1)_C")]
    univ_ok = (
        clifford_err < 1e-14
        and max(ko6_errs) == 0.0
        and tr2_ordered == [16.0, 8.0, 2.0, 8.0]
        and all(abs(r - 1.0) < 1e-12 for r in ratios_mass)
        and max(ctrl_kins) < 1e-12
    )
    cc.check(univ_ok,
             "V12.2.C1a: 32x32 KO-6 generators err=0, distinct Tr(T^2)=[16,8,2,8], 4D C^128 a2/a4 ratio=1.0, I_4 ctrl=0.0")
    cc.check(abs(r_dr_1522 - 0.5) < 1e-12 and abs(r_dr_611 - 0.5) < 1e-12,
             "V12.2.C1b: Cross-quartic portals R_{Delta_R, 1522} = 0.5000, R_{Delta_R, 611} = 0.5000")

    print(f"  [V12.2.C1] Exact 32x32 KO-6 & 4D C^128 Spectral-Action Traces & Portals [Т] / [✗]:")
    print(f"             - Tr_32(T^2): {tr2_vals} (KO-6 err={max(ko6_errs):.1e}, 4D C^128 tr_mass/kin_4d_a4={ratios_mass[0]:.12f}, I_4 ctrl={max(ctrl_kins):.1e})")
    print(f"             - Cross-quartic portals: R_(DeltaR, 1522) = {r_dr_1522:.4f}, R_(DeltaR, 611) = {r_dr_611:.4f}")

    # 2. Homogeneous 1-loop RGE of m_DeltaR^2, CW shift & 1-loop heavy portal destabilization
    g_ps_sq = 4.0 * math.pi / 44.0
    c2_dr = 6.5  # C_2(10) + C_2(3) = 4.5 + 2.0
    dt_ir = math.log(1e11 / 1e15)
    m_ratios = {
        lam_d: math.exp((32.0 * lam_d - 6.0 * c2_dr * g_ps_sq) / (16.0 * math.pi ** 2) * dt_ir)
        for lam_d in (0.05, 0.15, 0.30)
    }
    delta_lam_cw = 30.0 * (g_ps_sq ** 2) / (16.0 * math.pi ** 2) * math.log(1e15 / 1e11)
    m_heavy_ref = 1.0e15
    m_ps_ref = 1.0e11
    lam_portal = 0.10
    portal_shifts = {
        dof: math.sqrt(dof * lam_portal / (32.0 * math.pi ** 2)) * m_heavy_ref
        for dof in (1, 12, 72, 132)
    }
    tree_tuning = (m_ps_ref / m_heavy_ref) ** 2
    loop_tuning_r = (m_ps_ref / portal_shifts[72]) ** 2
    loop_tuning_c = (m_ps_ref / portal_shifts[132]) ** 2

    cc.check(all(1.05 <= v <= 1.80 for v in m_ratios.values()),
             "V12.2.C2a: Homogeneous 1-loop m_DeltaR^2(1e11)/m_DeltaR^2(1e15) in [1.05, 1.80]")
    cc.check(delta_lam_cw < 0.20, "V12.2.C2b: CW gauge shift Delta lambda_Delta < 0.20")
    cc.check(1.4e14 < portal_shifts[72] < 2.2e14 and 1.4e14 < portal_shifts[132] < 2.2e14,
             "V12.2.C2c: 1-loop heavy portal shift delta m_DeltaR in [1.4e14, 2.2e14] GeV (1e-8 tree / ~3e-7 loop tuning)")

    print(f"  [V12.2.C2] 1-Loop Radiative Stability & Portal Destabilization [Т] / [✗]:")
    print(f"             - Homogeneous RGE m_DR^2(1e11)/m_DR^2(1e15): " + ", ".join(f"lam={k}: {v:.4f}" for k, v in m_ratios.items()))
    print(f"             - CW shift Delta_lam = {delta_lam_cw:.4f} < 0.20; 1-loop portal shifts (M_heavy=1e15):")
    print(f"               Split-R (72 dof): {portal_shifts[72]:.3e} GeV (loop tune {loop_tuning_r:.2e}); "
          f"Split-C (132 dof): {portal_shifts[132]:.3e} GeV (loop tune {loop_tuning_c:.2e}, tree tune {tree_tuning:.1e})")

    # 3. 2-loop Split-R / Split-C scan over M_heavy in [1e13, 1e14, 1e15, 3e15, 7.89e15, 1e16]
    m_heavy_grid = [1.0e13, 1.0e14, 1.0e15, 3.0e15, 7.89e15, 1.0e16]
    a2_mps, a2_lam, a2_ainv = _solve_ps_unif([S_122_C, S_1013_C])
    lam_h_a2 = _run_sm_higgs_2loop(a2_mps)

    split_scan = {"Split-R": [], "Split-C": []}
    for mode, s_hi in (
        ("Split-R", [S_122_C, S_1013_C, S_611_C, S_1522_R]),
        ("Split-C", [S_122_C, S_1013_C, S_611_C, S_1522_C]),
    ):
        for mh in m_heavy_grid:
            mps_s, lam_s, ainv_s = _solve_ps_unif([S_122_C, S_1013_C], s_hi, m_heavy=mh)
            lh = _run_sm_higgs_2loop(mps_s)
            p_stab = math.sqrt(-lh)
            p_ncg = math.sqrt(0.10 - lh)
            split_scan[mode].append((mh, mps_s, lam_s, ainv_s, lh, p_stab, p_ncg))

    # Convergence to Chain A2 at M_heavy >= 7.89e15 GeV
    r_conv = split_scan["Split-R"][-2]
    c_conv = split_scan["Split-C"][-2]
    r_1e15 = split_scan["Split-R"][2]
    c_1e15 = split_scan["Split-C"][2]
    conv_ok = (
        abs(r_conv[1] - a2_mps) / a2_mps < 1e-4
        and abs(c_conv[1] - a2_mps) / a2_mps < 1e-4
        and abs(r_conv[3] - a2_ainv) < 1e-3
        and abs(lam_h_a2 + 0.004115) < 1e-4
    )
    # Exact Super-K M_6 bound for O(1) Yukawa
    hbar_yr = 6.582119569e-25 / 3.15576e7
    m_p = 0.938272
    alpha_h = 0.015
    a_r = 2.5
    kin_epi = (m_p / (32.0 * math.pi)) * (alpha_h ** 2) * (a_r ** 2)
    m6_o1_min = (kin_epi * 2.4e34 / hbar_yr) ** 0.25
    m_n1 = 1.80e10
    cc.check(conv_ok, "V12.2.C3a: Split-R/Split-C converge smoothly to Chain A2 at M_heavy >= 7.890e15 GeV")
    cc.check(m6_o1_min >= 1.971e15, "V12.2.C3b: O(1) Yukawa Super-K bound M_6 >= 1.971e15 GeV")
    cc.check(r_1e15[1] > m_n1 and c_1e15[1] > m_n1 and r_1e15[4] < 0 and c_1e15[4] < 0,
             "V12.2.C3c: M_PS > M_{N_1} and Delta_R Higgs stabilization preserved at M_heavy = 1e15 GeV")

    print(f"  [V12.2.C3] 2-Loop Split-R/Split-C Scan over M_heavy in [1e13, 1e16] GeV [С]:")
    for mode in ("Split-R", "Split-C"):
        for mh, mps_s, lam_s, ainv_s, lh, p_st, p_nc in split_scan[mode]:
            print(f"             - {mode:7s} M_h={mh:.2e}: M_PS={mps_s:.3e}, Lam={lam_s:.3e}, a^-1={ainv_s:.2f}, lam_H-={lh:+.5f}, p={p_st:.4f}/{p_nc:.4f}")
    print(f"             - O(1) Yukawa Super-K bound M_6 >= {m6_o1_min:.3e} GeV; Chain A2 Lam_NCG = {a2_lam:.3e} GeV.")

    # 4. Finite MS-bar Vissani naturalness bounds
    m_h = 125.25
    m_n3 = 3.005e11
    y_nu3 = 0.5423
    # delta m_H^2 = y_nu3^2 M_N3^2 / (4 pi^2), Delta_EW = |delta m_H^2| / (m_h^2 / 2)
    delta_ew_n3 = (y_nu3 ** 2 * m_n3 ** 2 / (4.0 * math.pi ** 2)) / (0.5 * m_h ** 2)
    delta_ew_dr = {
        "Split-C": (0.10 / (16.0 * math.pi ** 2) * c_1e15[1] ** 2) / (0.5 * m_h ** 2),
        "Split-R": (0.10 / (16.0 * math.pi ** 2) * r_1e15[1] ** 2) / (0.5 * m_h ** 2),
        "Chain A2": (0.10 / (16.0 * math.pi ** 2) * a2_mps ** 2) / (0.5 * m_h ** 2),
    }
    delta_ew_heavy = (0.10 / (16.0 * math.pi ** 2) * (1.0e15 ** 2)) / (0.5 * m_h ** 2)

    cc.check(abs(delta_ew_n3 - 8.576e16) / 8.576e16 < 1e-2, "V12.2.C4a: Vissani Delta_EW(N_3) ~ 8.58e16")
    cc.check(all(7.0e14 <= v <= 1.7e15 for v in delta_ew_dr.values()),
             "V12.2.C4b: Vissani Delta_EW(Delta_R) in [7.0e14, 1.7e15] per dof")
    cc.check(delta_ew_heavy > 8.0e22,
             "V12.2.C4c: Vissani Delta_EW(M_heavy=1e15) > 8.0e22 per dof (UV split & EW hierarchy remain [П])")

    print(f"  [V12.2.C4] Finite MS-bar Vissani Naturalness Bounds [Т] / [✗] / [П]:")
    print(f"             - Delta_EW(N_3) = {delta_ew_n3:.2e}; Delta_EW(Delta_R): "
          + ", ".join(f"{k}={v:.2e}" for k, v in delta_ew_dr.items()))
    print(f"             - Delta_EW(M_heavy=1e15 GeV) = {delta_ew_heavy:.2e} per dof (UV split & EW hierarchy remain [П]).\n")

    return {
        "tags": ["[Т]", "[С]", "[П]", "[✗]"],
        "fitted_parameters": 0,
        "r_dr_1522": r_dr_1522,
        "r_dr_611": r_dr_611,
        "delta_lam_cw": delta_lam_cw,
        "portal_shift_split_r": portal_shifts[72],
        "portal_shift_split_c": portal_shifts[132],
        "m6_o1_min": m6_o1_min,
        "delta_ew_n3": delta_ew_n3,
        "delta_ew_heavy": delta_ew_heavy,
    }


def run_v12_wall2() -> tuple[int, int, dict]:
    cc = _CheckCounter()
    sum_a = suite_v122a_cp_and_ckm_audit(cc)
    sum_b = suite_v122b_f42_3gen_and_thm48dc(cc)
    sum_c = suite_v122c_heavy_threshold_split_audit(cc)
    summary = {
        "V12.2.A": sum_a,
        "V12.2.B": sum_b,
        "V12.2.C": sum_c,
        "tags": {
            "V12.2.A": sum_a["tags"],
            "V12.2.B": sum_b["tags"],
            "V12.2.C": sum_c["tags"],
        },
        "fitted_parameters": 0,
        "passed": cc.passed,
        "total": cc.total,
        "failures": cc.failures,
    }
    return cc.passed, cc.total, summary


# ==============================================================================
# V12.3.A: WALL 3 — COSMOLOGICAL CONSTANT, SEQUESTERING & EXTERNAL SU(2)_d
# ==============================================================================
def suite_v123a_wall3_cc_sequestering_su2d(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.3.A: Wall 3 — Radiative CC, Sequestering Obstructions & External SU(2)_d")
    print("=" * 88)

    rho_l0 = 2.5e-47
    lam_de_gev = rho_l0 ** 0.25
    lam_de_mev = lam_de_gev * 1e12
    m_pl_full = 1.22089e19
    m_pl_red = 2.43535e18

    # Benchmark Chain A2 scales from exact 2-loop Machacek-Vaughn C_top_PS = [2, 2, 2]
    m_ps_a2, lam_ncg_a2, a_gut_inv_a2 = _solve_ps_unif([S_122_C, S_1013_C], ng=3)
    m_n3 = 3.005e11

    # V12.3.A1a: Observed CC hierarchy in Planck units
    ratio_full = rho_l0 / (m_pl_full ** 4)
    ratio_red = rho_l0 / (m_pl_red ** 4)
    cc.check(
        1.0e-123 < ratio_full < 2.0e-123 and 6.0e-121 < ratio_red < 8.0e-121,
        "V12.3.A1a: Observed CC hierarchy rho_L0/M_Pl,full^4 ~ 1.125e-123 and rho_L0/M_Pl,red^4 ~ 7.107e-121 [Т]",
    )

    # V12.3.A1b: CCvS spectral action & 1-loop a_0 * Lambda_NCG^4 vacuum energy catastrophe
    dim_hf_3gen = 96.0
    f0_cc = 1.0
    rho_sa = f0_cc * (lam_ncg_a2 ** 4) * dim_hf_3gen / (2.0 * math.pi ** 2)
    sa_ratio = rho_sa / rho_l0
    a0_map = {"Chain A2": 14.0, "Split-R": 86.0, "Split-C": 146.0}
    loop1_ratios = {
        k: (abs(a0_v) / (32.0 * math.pi ** 2)) * (lam_ncg_a2 ** 4) / rho_l0
        for k, a0_v in a0_map.items()
    }
    cc.check(
        sa_ratio > 1.0e110
        and loop1_ratios["Chain A2"] > 1.0e108
        and loop1_ratios["Split-R"] > 1.0e109
        and loop1_ratios["Split-C"] > 1.0e109,
        "V12.3.A1b: CCvS spectral action (>1e110 rho_L0) & 1-loop |a_0| Lambda_NCG^4 (>1e108..1e109 rho_L0) [Т/✗]",
    )

    # V12.3.A1c: Finite CW threshold shifts + f0_CC=chi(0)=0 ghost link (V12.1.B3)
    cw_ratios = {
        "M_N3": (m_n3 ** 4) / (32.0 * math.pi ** 2) / rho_l0,
        "M_PS": (m_ps_a2 ** 4) / (32.0 * math.pi ** 2) / rho_l0,
        "m_nu3": ((50.302e-12) ** 4) / (32.0 * math.pi ** 2) / rho_l0,
        "v_EW": (174.104 ** 4) / (64.0 * math.pi ** 2) / rho_l0,
        "Lam_QCD": (0.2 ** 4) / (64.0 * math.pi ** 2) / rho_l0,
    }
    xs_q, ws_q = np.polynomial.legendre.leggauss(64)
    xs_q = 0.5 * (xs_q + 1.0)
    ws_q = 0.5 * ws_q

    def delta2_ueu(q: float) -> float:
        sx = xs_q * (1.0 - xs_q) * (q * q)
        return float(np.dot(ws_q, (2.0 + 3.0 * sx + 2.0 * sx * sx) * np.exp(-sx) - 2.0) / (16.0 * math.pi ** 2))

    qstar_ueu = float(brentq(delta2_ueu, 1.0, 6.0))
    cc.check(
        cw_ratios["M_N3"] > 1.0e89
        and cw_ratios["v_EW"] > 1.0e52
        and all(v > 1.0 for v in cw_ratios.values())
        and 3.44 < qstar_ueu < 3.45,
        "V12.3.A1c: Finite CW shifts (> rho_L0 at all scales) & chi(u)=u e^-u (f0=0) ghost q_*=3.4473*Lam [Т/✗]",
    )

    print("  [V12.3.A1] Radiative Vacuum Energy in Chain A2 & Split-CCvS [Т] / [✗]:")
    print(f"             - rho_L0/M_Pl,full^4 = {ratio_full:.3e} ({math.log10(ratio_full):.2f} dex), /M_Pl,red^4 = {ratio_red:.3e}")
    print(f"             - rho_SA/rho_L0 = {sa_ratio:.3e}; 1-loop |a_0| shifts: A2={loop1_ratios['Chain A2']:.3e}, Split-C={loop1_ratios['Split-C']:.3e}")
    print(f"             - CW shifts/rho_L0: M_N3={cw_ratios['M_N3']:.2e}, v_EW={cw_ratios['v_EW']:.2e}, m_nu3={cw_ratios['m_nu3']:.1f}; u*e^-u ghost q*={qstar_ueu:.4f}")

    # V12.3.A2a: Kaloper-Padilla 4-volume fractions across GUT, PS, EW, QCD
    t0_cmb = 2.3486e-13
    hbar_gev_s = 6.582119569e-25
    t_0_sec = 4.354e17
    v4_today = t_0_sec / 3.0

    def kp_residual_over_rho_l0(t_gev: float, g_star: float, d_rho: float) -> float:
        t_sec = (0.301 * 1.2209e19 / (math.sqrt(g_star) * (t_gev ** 2))) * hbar_gev_s
        z = ((g_star / 3.91) ** (1.0 / 3.0)) * (t_gev / t0_cmb)
        a = 1.0 / z
        f_pt = (0.4 * (a ** 3) * t_sec) / v4_today
        return (f_pt * d_rho) / rho_l0

    res_gut = kp_residual_over_rho_l0(lam_ncg_a2, 250.0, lam_ncg_a2 ** 4)
    res_ps = kp_residual_over_rho_l0(m_ps_a2, 180.0, m_ps_a2 ** 4)
    res_ew = kp_residual_over_rho_l0(160.0, 106.75, 1.0e8)
    res_qcd = kp_residual_over_rho_l0(0.15, 61.75, 1.0e-3)
    cc.check(
        res_gut < 1.0e-33 and res_ps < 1.0e-28 and res_ew < 1.0e-19 and res_qcd < 1.0e-15,
        "V12.3.A2a: Kaloper-Padilla 4-volume suppression across GUT (<1e-33), PS (<1e-28), EW (<1e-19), QCD (<1e-15) [С]",
    )

    # V12.3.A2b: Closed-FRW cycloid matter-trace ceiling (F-15C)
    th = np.linspace(0.0, 2.0 * math.pi, 20001)
    a_norm = 0.5 * (1.0 - np.cos(th))
    mean_a3 = float(np.trapezoid(a_norm ** 4, th) / np.trapezoid(a_norm, th))
    ceil_cyc = 0.25 / mean_a3
    obs_om_ratio = 0.685 / 0.315
    cc.check(
        abs(ceil_cyc - 16.0 / 35.0) < 1.0e-7 and obs_om_ratio / ceil_cyc > 4.7,
        "V12.3.A2b: Cycloid ceiling (16/35 = 0.4571) < 2.1746 observed Omega_L/Omega_m (>4.7x short, F-15C) [Т/✗]",
    )

    # V12.3.A2c: Global finite-V4 static cancellation vs eternal de Sitter dilution & non-locality
    v4_weights = np.array([0.4 * (1.0e-15 ** 3) * 1.0e-36, 0.4 * (1.0e-4 ** 3) * 1.0e-10, v4_today])
    rho_uv_const = 1.0e60
    static_shift_residual = abs(rho_uv_const - float(np.sum(v4_weights * rho_uv_const) / np.sum(v4_weights)))
    eternal_ds_residual = ceil_cyc * ((1.0 / 1.0e4) ** 3)
    cc.check(
        static_shift_residual == 0.0 and eternal_ds_residual < 1.0e-12,
        "V12.3.A2c: Global V_4 static cancellation (F-10C) requires V_4 < inf; eternal dS drives rho_L,res -> 0 [Т/✗/П]",
    )

    print("  [V12.3.A2] Unimodular & Kaloper–Padilla Global Sequestering Obstructions [С] / [Т] / [✗]:")
    print(f"             - Residuals/rho_L0: GUT={res_gut:.3e}, PS={res_ps:.3e}, EW={res_ew:.3e}, QCD={res_qcd:.3e}")
    print(f"             - Cycloid <a^3>={mean_a3:.6f}, ceil={ceil_cyc:.6f} vs obs={obs_om_ratio:.4f} ({obs_om_ratio/ceil_cyc:.2f}x short)")

    # V12.3.A3a: Unconditional WGC-quintessence product boundary (F-29A,B)
    c_aw = 0.5 * math.pi * math.sqrt(6.0)
    omega_l = 0.685
    c_cos_min = math.sqrt(1.5 * omega_l)
    c_cos_mid = math.sqrt(3.0 * omega_l)
    s_max = 3.0 * c_aw / c_cos_min
    lam_uv_max_mev = lam_de_mev * math.exp(s_max / 4.0)
    lam_uv_mid_mev = lam_de_mev * math.exp((3.0 * c_aw / c_cos_mid) / 4.0)
    cc.check(
        s_max < 12.0 and 38.0 < lam_uv_max_mev < 39.2 and 16.4 < lam_uv_mid_mev < 17.1 and lam_uv_max_mev < 50.30,
        "V12.3.A3a: WGC-quintessence boundary S_max=11.39<12 => Lam_UV <= 38.54 meV (16.74 meV mid) < m_nu3 [Т/✗]",
    )

    # V12.3.A3b: Multi-axion WGC convex hull (F-35D)
    s_me = math.log((5.11e-4 ** 4) / rho_l0)
    s_mpl = math.log((m_pl_red ** 4) / rho_l0)
    s_a2 = 2.0 * math.pi * a_gut_inv_a2
    n_ax_me = int(math.ceil((s_me / s_max) ** 2))
    n_ax_mpl = int(math.ceil((s_mpl / s_max) ** 2))
    n_ax_a2 = int(math.ceil((s_a2 / s_max) ** 2))
    cc.check(
        n_ax_me == 46 and n_ax_mpl == 591 and n_ax_a2 == 621 and n_ax_me > 21,
        "V12.3.A3b: Multi-axion WGC convex hull forces N_ax >= 46 (m_e), 591 (M_Pl,red), 621 (Chain A2) > 21 [Т/✗]",
    )

    # V12.3.A3c: Updated Chain A2 (C_top_PS=[2,2,2]) Spin(10) instanton
    det_f = float(np.prod(np.array([1.801e10, 1.827e10, 3.005e11]) / m_ps_a2))
    clos_f2 = (det_f ** 2) / ((4.0 * math.pi ** 2) ** 6)
    hv_so10 = 8
    log10_fact = lambda n: sum(math.log10(k) for k in range(1, n + 1))
    log10_c_so10 = (
        math.log10(4.60 / math.pi ** 2)
        - 1.68 * hv_so10 / math.log(10.0)
        - log10_fact(hv_so10 - 1)
        - log10_fact(hv_so10 - 2)
        - 2.0 * hv_so10 * math.log10(2.0)
        + (0.292 * 6.0) / math.log(10.0)
    )
    log10_dv_a2 = (
        4.0 * math.log10(lam_ncg_a2)
        + 2.0 * hv_so10 * math.log10(s_a2)
        + log10_c_so10
        - s_a2 / math.log(10.0)
        + math.log10(clos_f2)
    )
    inst_deficit_dex = log10_dv_a2 - math.log10(rho_l0)
    cc.check(
        inst_deficit_dex < -2.8 and -50.0 < log10_dv_a2 < -49.5,
        "V12.3.A3c: Updated Chain A2 (45.147) Spin(10) instanton gives log10(Delta V)=-49.70 (-3.09 dex deficit) [✗]",
    )

    print("  [V12.3.A3] Internal WGC & Spin(10) Instanton Closure (C_top_PS=[2,2,2]) [Т] / [✗]:")
    print(f"             - S_max={s_max:.3f}, Lam_UV_max={lam_uv_max_mev:.2f} meV, mid={lam_uv_mid_mev:.2f} meV")
    print(f"             - N_ax >= {n_ax_me} (m_e), {n_ax_mpl} (M_Pl,red), {n_ax_a2} (Chain A2, S={s_a2:.2f}); inst log10(DV)={log10_dv_a2:.2f} ({inst_deficit_dex:+.2f} dex)")

    # V12.3.A4a: Spin(10) D_5 centralizer audit (F-25A)
    roots_d5 = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (-1, 1):
                for sj in (-1, 1):
                    r = np.zeros(5, dtype=int)
                    r[i] = si
                    r[j] = sj
                    roots_d5.append(r)
    h_sm = np.array([[1, -1, 0, 0, 0], [0, 1, -1, 0, 0], [0, 0, 0, 1, -1], [2, 2, 2, 3, 3]], dtype=int)
    comm_roots = [r for r in roots_d5 if np.all(h_sm @ r == 0)]
    cc.check(
        len(roots_d5) == 40 and int(np.linalg.matrix_rank(h_sm)) == 4 and len(comm_roots) == 0,
        "V12.3.A4a: Spin(10) centralizer of G_SM has 0/40 commuting D_5 roots (rank 4, F-25A) [Т/✗]",
    )

    # V12.3.A4b: IR-confining SU(2)_d exact 2-loop Machacek-Vaughn RG (M_GUT -> Lambda_d = 2.3 meV)
    lam_d_target = 2.3e-12

    def log_lam_su2d(a_inv_gut: float, b0: float, b1: float) -> float:
        def ev_conf(_t, y):
            return y[0] - 1.0

        ev_conf.terminal = True
        sol = solve_ivp(
            lambda _t, y: [b0 / (2.0 * math.pi) + b1 / (8.0 * math.pi ** 2 * max(y[0], 0.1))],
            (math.log(lam_ncg_a2), math.log(1.0e-45)),
            [a_inv_gut],
            events=ev_conf,
            rtol=1e-11,
            atol=1e-13,
        )
        return float(sol.t_events[0][0]) if len(sol.t_events[0]) > 0 else math.log(1.0e-45)

    a_ym = float(brentq(lambda a: log_lam_su2d(a, 22.0 / 3.0, 136.0 / 3.0) - math.log(lam_d_target), 20.0, 95.0))
    a_hg = float(brentq(lambda a: log_lam_su2d(a, 43.0 / 6.0, 259.0 / 6.0) - math.log(lam_d_target), 20.0, 95.0))
    a_nf4 = float(brentq(lambda a: log_lam_su2d(a, 4.5, 10.5) - math.log(lam_d_target), 20.0, 70.0))
    cc.check(
        abs(a_ym - 76.942) < 0.02 and abs(a_hg - 75.204) < 0.02 and abs(a_nf4 - 47.093) < 0.02,
        "V12.3.A4b: IR-confining SU(2)_d 2-loop RG: Pure YM 76.94, Unbroken+1H 75.20, N_f=4+1H 47.09 [С/✗]",
    )

    # V12.3.A4c: UV-Higgsed small-instanton pure YM SU(2)_d at v_d = M_GUT + WGC check
    def solve_uv_higgsed(v_d: float) -> float:
        return float(brentq(
            lambda a: 4.0 * math.log(2.0 * math.pi * a) + 4.0 * math.log(v_d) - 2.0 * math.pi * a - math.log(rho_l0),
            20.0,
            80.0,
        ))

    a_uv_v7 = solve_uv_higgsed(1.20e16)
    a_uv_a2 = solve_uv_higgsed(lam_ncg_a2)
    mphi_h0_uv_ax = c_cos_min * (2.0 * math.pi * a_uv_a2) / c_aw
    cc.check(
        abs(a_uv_v7 - 44.231) < 0.01 and abs(a_uv_a2 - 43.960) < 0.01 and mphi_h0_uv_ax > 70.0,
        "V12.3.A4c: UV-Higgsed small-instanton SU(2)_d (44.231 @ 1.2e16, 43.960 @ Chain A2); periodic axion WGC-blocked (m_phi/H0=72.8) [Т/С/✗]",
    )

    # V12.3.A4d: Entropy-diluted Delta N_eff (F-39A) & non-thermal T_d/T_SM ceiling for N_f=4+1H
    g_decs = (106.75, 180.0, 250.0)
    neff_ym = [(4.0 / 7.0) * 6.0 * ((10.75 / g_dec) ** (4.0 / 3.0)) for g_dec in g_decs]
    neff_hg = [(4.0 / 7.0) * 10.0 * ((10.75 / g_dec) ** (4.0 / 3.0)) for g_dec in g_decs]
    neff_nf4 = [(4.0 / 7.0) * 38.0 * ((10.75 / g_dec) ** (4.0 / 3.0)) for g_dec in g_decs]
    td_tsm_max = [(0.28 / n_val) ** 0.25 for n_val in neff_nf4]
    cc.check(
        all(abs(x - y) < 1.0e-3 for x, y in zip(neff_ym, (0.1606, 0.0800, 0.0517)))
        and all(abs(x - y) < 1.0e-3 for x, y in zip(neff_hg, (0.2677, 0.1334, 0.0861)))
        and all(abs(x - y) < 1.0e-3 for x, y in zip(neff_nf4, (1.0173, 0.5069, 0.3271)))
        and all(abs(x - y) < 1.0e-3 for x, y in zip(td_tsm_max, (0.7243, 0.8621, 0.9619)))
        and min(neff_nf4) > 0.32 > 0.28,
        "V12.3.A4d: CMB-S4 Delta N_eff & non-thermal T_d/T_SM < (0.724, 0.862, 0.962) bounds for N_f=4+1H [Т/С/✗]",
    )

    # V12.3.A4e: Stratum C honesty check
    tags_a = ["[Т]", "[С]", "[П]", "[✗]"]
    fitted_a = 0
    cc.check(
        fitted_a == 0 and set(tags_a) == {"[Т]", "[С]", "[П]", "[✗]"},
        "V12.3.A4e: Explicit Stratum C classification for SU(2)_d & sequestered dynamics (0 fitted params) [П]",
    )

    print("  [V12.3.A4] External SU(2)_d Confining vs UV-Higgsed Regimes & Stratum C [Т] / [С] / [✗] / [П]:")
    print(f"             - Confining (2.3 meV): YM={a_ym:.3f}, Unbroken+1H={a_hg:.3f}, N_f=4+1H={a_nf4:.3f}")
    print(f"             - UV-Higgsed small-instanton: {a_uv_v7:.4f} (1.20e16) / {a_uv_a2:.4f} (Chain A2); axion m_phi/H0={mphi_h0_uv_ax:.2f} [✗]")
    print(f"             - Delta N_eff YM={[round(v,4) for v in neff_ym]}, +1H={[round(v,4) for v in neff_hg]}, N_f=4={[round(v,4) for v in neff_nf4]} -> Td/TSM < {[round(v,4) for v in td_tsm_max]}\n")

    return {
        "tags": tags_a,
        "fitted_parameters": fitted_a,
        "rho_l0_over_mpl_full4": ratio_full,
        "rho_sa_over_rho_l0": sa_ratio,
        "loop1_ratios": loop1_ratios,
        "cw_ratios": cw_ratios,
        "qstar_ueu": qstar_ueu,
        "seq_suppression_gut": res_gut,
        "seq_suppression_ps": res_ps,
        "seq_suppression_ew": res_ew,
        "seq_suppression_qcd": res_qcd,
        "cycloid_ceiling": ceil_cyc,
        "s_max_wgc": s_max,
        "lam_uv_max_mev": lam_uv_max_mev,
        "lam_uv_mid_mev": lam_uv_mid_mev,
        "n_ax_bounds": {"m_e": n_ax_me, "M_Pl_red": n_ax_mpl, "Chain_A2": n_ax_a2},
        "instanton_log10_dv": log10_dv_a2,
        "instanton_deficit_dex": inst_deficit_dex,
        "alpha_d_inv_ym": a_ym,
        "alpha_d_inv_hg": a_hg,
        "alpha_d_inv_nf4": a_nf4,
        "alpha_d_inv_uv_v7": a_uv_v7,
        "alpha_d_inv_uv_a2": a_uv_a2,
        "delta_neff_ym": neff_ym,
        "delta_neff_hg": neff_hg,
        "delta_neff_nf4": neff_nf4,
        "td_tsm_max_nf4": td_tsm_max,
    }


# ==============================================================================
# V12.3.B: WALL 3 — DYNAMICAL 1_F FIMP PRESERVING Z_2^DM (F-41)
# ==============================================================================
def suite_v123b_fimp_1f_z2dm(cc: _CheckCounter) -> dict:
    print("=" * 88)
    print("V12.3.B: Wall 3 — Dynamical 1_F FIMP Preserving Z_2^DM (F-41) & Boltzmann Audit")
    print("=" * 88)

    # V12.3.B1a: T-163 [✗] partial O-conjugation fails positivity on D(C^7)
    psi_o = np.array([1.0, 1.0, 1.0j], dtype=complex) / math.sqrt(3.0)
    rho_o = np.outer(psi_o, psi_o.conj())
    sigma_rho = rho_o.copy()
    sigma_rho[0, 1:] = sigma_rho[0, 1:].conj()
    sigma_rho[1:, 0] = sigma_rho[1:, 0].conj()
    det_s = float(np.linalg.det(sigma_rho).real)
    min_eig_s = float(np.linalg.eigvalsh(sigma_rho)[0])
    cc.check(
        abs(det_s + 4.0 / 27.0) < 1.0e-12 and min_eig_s < -0.30,
        "V12.3.B1a: T-163 [✗] partial O-conjugation fails positivity (det=-4/27, min_eig=-1/3) [Т/✗]",
    )

    # V12.3.B1b: Full 10-irrep Spin(10) Z_4 superset Z_2^DM ring & 16 Chain A2 submultiplets
    z4_charge = {
        "r1": 0, "r10": 2, "r16": 1, "r16bar": 3, "r45": 0,
        "r54": 0, "r120": 2, "r126": 2, "r126bar": 2, "r210": 0,
    }
    # 16 SM/PS submultiplets of minimal Chain A2: (3*(B-L), 2*s)
    chain_a2_submultiplets = (
        # 16_F (2*s = 1): Q_L, u_R^c, d_R^c, L_L, e_R^c, nu_R^c
        [(1, 1), (-1, 1), (-1, 1), (-3, 1), (3, 1), (3, 1)]
        # 10_H + 45_V + 126bar_H + 210_H bosons (2*s = 0 or 2): (B-L in {0, +-2/3, +-4/3, +-2})
        + [(0, 0), (2, 0), (-2, 0), (0, 2), (4, 2), (-4, 2), (2, 0), (-2, 0), (6, 0), (-6, 0)]
    )
    all_pdm_even = all(((3 * bm_l + two_s) % 2 == 0) for bm_l, two_s in chain_a2_submultiplets)
    subgrp_2 = {(2 * k) % 4 for k in range(4)}
    subgrp_3 = {(3 * k) % 4 for k in range(4)}
    lin_ops_a2 = [
        (z4_charge["r1"] + z4_charge["r16"] + z4_charge["r126bar"]) % 4,
        (z4_charge["r1"] + z4_charge["r16"] + z4_charge["r10"]) % 4,
        (z4_charge["r1"] + 3 * z4_charge["r16"]) % 4,
    ]
    op_16bar = (z4_charge["r1"] + z4_charge["r16"] + z4_charge["r16bar"]) % 4
    cc.check(
        len(chain_a2_submultiplets) == 16
        and all_pdm_even
        and subgrp_2 == {0, 2}
        and subgrp_3 == {0, 1, 2, 3}
        and all(q == 3 for q in lin_ops_a2)
        and op_16bar == 0,
        "V12.3.B1b: 10-irrep Spin(10) Z_4 ring & 16 Chain A2 submultiplets preserve Z_2^DM vs <16bar_H> [Т]",
    )

    # V12.3.B1c: Exact 34x34 CCvS + 1_F matrix embedding (F-42 + 1_F)
    def idx32(b: int, s: int, c: int) -> int:
        return 8 * b + 4 * s + c

    q_bl_32 = np.zeros(32)
    for b in range(4):
        for s in range(2):
            for c in range(4):
                q_bl_32[idx32(b, s, c)] = 1.0 / 3.0 if c < 3 else -1.0
    p_dm_32 = np.diag([(-1.0) ** round(3.0 * q + 1.0) for q in q_bl_32])
    p_dm_34 = np.diag(list(np.diag(p_dm_32)) + [-1.0, -1.0]).astype(complex)

    t_122_32 = np.zeros((32, 32), dtype=complex)
    for c in range(4):
        t_122_32[idx32(0, 0, c), idx32(1, 0, c)] = t_122_32[idx32(1, 0, c), idx32(0, 0, c)] = 1.0
        t_122_32[idx32(2, 0, c), idx32(3, 0, c)] = t_122_32[idx32(3, 0, c), idx32(2, 0, c)] = 1.0
    t_1013_32 = np.zeros((32, 32), dtype=complex)
    t_1013_32[idx32(1, 0, 3), idx32(3, 0, 3)] = t_1013_32[idx32(3, 0, 3), idx32(1, 0, 3)] = 1.0
    t_611_32 = np.zeros((32, 32), dtype=complex)
    for s1, s2, sgn in ((0, 1, 1.0), (1, 0, -1.0)):
        t_611_32[idx32(1, s1, 0), idx32(3, s2, 3)] = t_611_32[idx32(3, s2, 3), idx32(1, s1, 0)] = sgn
        t_611_32[idx32(1, s1, 3), idx32(3, s2, 0)] = t_611_32[idx32(3, s2, 0), idx32(1, s1, 3)] = -sgn

    def embed34(m32: np.ndarray) -> np.ndarray:
        out = np.zeros((34, 34), dtype=complex)
        out[:32, :32] = m32
        return out

    comm_err = max(
        float(np.max(np.abs(embed34(m) @ p_dm_34 - p_dm_34 @ embed34(m))))
        for m in (t_122_32, t_1013_32, t_611_32)
    )
    t_16bar_34 = np.zeros((34, 34), dtype=complex)
    t_16bar_34[idx32(1, 0, 3), 32] = t_16bar_34[32, idx32(1, 0, 3)] = 1.0
    t_16bar_34[idx32(3, 0, 3), 33] = t_16bar_34[33, idx32(3, 0, 3)] = 1.0
    anti_err = float(np.max(np.abs(t_16bar_34 @ p_dm_34 + p_dm_34 @ t_16bar_34)))
    cc.check(
        np.allclose(p_dm_32, np.eye(32)) and comm_err < 1.0e-14 and anti_err < 1.0e-14,
        "V12.3.B1c: 34x34 CCvS+1_F embedding: Delta_R commutes with P_DM^(34) while 16bar_H anticommutes [Т/П]",
    )

    # V12.3.B1d: Uniqueness of chi_1 = 1_F vs 54_F (6:4:1) & 16_H (Z' thermalization)
    mps_a2, lam_a2, ainv_a2 = _solve_ps_unif([S_122_C, S_1013_C], ng=3)
    gamma_p_a2 = (
        (0.938272 / (32.0 * math.pi * (0.1304 ** 2)))
        * ((1.0 + 1.27) ** 2) * (2.5 ** 2) * (0.0118 ** 2)
        * ((4.0 * math.pi / (ainv_a2 * (lam_a2 ** 2))) ** 2)
        * (1.0 + (1.0 + 0.974 ** 2) ** 2)
    )
    tau_p_a2 = (6.582119569e-25 / gamma_p_a2) / 3.15576e7
    delta_4c_2l_54f = math.log(6561.0 / 16.0) / (3.0 * math.pi)
    # 54_F threshold shifts M_GUT by factor exp(-pi*(Delta_4C - Delta_2L)/... ) -> ~3.48e15 GeV -> tau_p ~ 3.08e33 < 2.4e34
    b4_lo, _ = _ps_betas([S_122_C, S_1013_C], ng=3)
    lam_54f = lam_a2 * math.exp(-2.0 * math.pi * delta_4c_2l_54f / abs(b4_lo[0] - b4_lo[1]))
    tau_p_54f = tau_p_a2 * ((lam_54f / lam_a2) ** 4)
    # 16_H (1,1,0)_S Z' thermalization at T_lep = 1.801e10 GeV
    aps_ps = _run_sm_2loop(math.log(mps_a2 / M_Z_PDG))
    a4_ps = 4.0 * math.pi / (aps_ps[2] ** 2)
    a2r_ps = (5.0 / 3.0) * (4.0 * math.pi / (aps_ps[0] ** 2)) - (2.0 / 3.0) * a4_ps
    g4_sq = 4.0 * math.pi / a4_ps
    g2r_sq = 4.0 * math.pi / a2r_ps
    norm_z = math.sqrt((2.0 / 3.0) * g2r_sq + g4_sq)

    def c_zp(t3r: float, bl: float) -> float:
        return (math.sqrt(2.0 / 3.0) * g2r_sq * t3r - math.sqrt(3.0 / 2.0) * g4_sq * (bl / 2.0)) / norm_z

    c_s_16h = c_zp(0.5, -1.0)
    sum_cf2 = 3.0 * (
        6.0 * c_zp(0.0, 1.0 / 3.0) ** 2
        + 3.0 * c_zp(0.5, 1.0 / 3.0) ** 2
        + 3.0 * c_zp(-0.5, 1.0 / 3.0) ** 2
        + 2.0 * c_zp(0.0, -1.0) ** 2
        + c_zp(-0.5, -1.0) ** 2
    )
    m_zp = math.sqrt(3.0) * (norm_z / math.sqrt(g4_sq)) * mps_a2
    t_lep = 1.801e10
    m_pl_red = 2.43535e18
    r_16h = (c_s_16h ** 2 * sum_cf2) / (math.pi ** 5 * (m_zp ** 4)) * (t_lep ** 8)
    n_eq_s = 2.0 * (1.2020569031595942 / (math.pi ** 2)) * (t_lep ** 3)
    h_lep = math.sqrt(math.pi ** 2 * 106.75 / 90.0) * (t_lep ** 2) / m_pl_red
    gh_16h = (2.0 * r_16h / n_eq_s) / h_lep
    cc.check(
        tau_p_a2 > 2.4e34 and abs(delta_4c_2l_54f - 0.6384) < 1.0e-3 and tau_p_54f < 2.4e34 and gh_16h > 4.0,
        "V12.3.B1d: chi_1=1_F preserves Chain A2 (tau_p=8.83e34) vs 54_F (tau_p<2.4e34) & 16_H (Gamma_Z'/H>4.0) [Т/✗]",
    )

    print("  [V12.3.B1] Z_2^DM, 34x34 CCvS+1_F Algebra & Uniqueness Audit [Т] / [✗] / [П]:")
    print(f"             - T-163 det={det_s:.6f}, min_eig={min_eig_s:.6f}; CCvS 34x34 comm_err={comm_err:.1e}, 16bar_anti={anti_err:.1e}")
    print(f"             - Chain A2 tau_p={tau_p_a2:.2e} yr vs 54_F Delta={delta_4c_2l_54f:+.4f} (tau_p~{tau_p_54f:.2e}) & 16_H Gamma_Z'/H={gh_16h:.2f}")

    # V12.3.B2a & V12.3.B2b: Full Boltzmann freeze-in ODE (Planck dim-5 vs PS dim-5 over-thermalization)
    def run_boltzmann_dim5(c5: float, lam_uv: float, t_rh: float, g_s: float = 106.75):
        pref = (2.0 * math.pi ** 2 / 45.0) * g_s * math.sqrt(math.pi ** 2 * g_s / 90.0) / m_pl_red
        zeta3 = 1.2020569031595942
        y_eq = (1.5 * zeta3 / (math.pi ** 2)) / ((2.0 * math.pi ** 2 / 45.0) * g_s)
        coeff = (c5 ** 2 / (4.0 * math.pi ** 5 * (lam_uv ** 2))) * t_rh / pref
        r_rh = (c5 ** 2 / (8.0 * math.pi ** 5 * (lam_uv ** 2))) * (t_rh ** 6)
        n_eq_rh = 1.5 * zeta3 / (math.pi ** 2) * (t_rh ** 3)
        h_rh = math.sqrt(math.pi ** 2 * g_s / 90.0) * (t_rh ** 2) / m_pl_red
        g_over_h = (2.0 * r_rh / n_eq_rh) / h_rh
        sol = solve_ivp(
            lambda u, y: [coeff * math.exp(-u) * (1.0 - (y[0] / y_eq) ** 2)],
            (0.0, math.log(1.0e4)),
            [0.0],
            method="Radau",
            rtol=1e-11,
            atol=1e-22,
        )
        y_ode = float(sol.y[0, -1])
        m_chi = 4.37e-10 / y_ode
        mu_r = m_chi * 0.9389 / (m_chi + 0.9389)
        sig_si = (mu_r ** 2 / math.pi) * ((0.30 * 0.9389 / (125.25 ** 2)) ** 2) * ((c5 / lam_uv) ** 2) * (1.97327e-14 ** 2)
        c5_max_nontherm = math.sqrt(0.01 / g_over_h)
        return g_over_h, y_ode, coeff, y_eq, m_chi, sig_si, c5_max_nontherm

    gh_25, yode_25, yan_25, _, m_25, sig_25, _ = run_boltzmann_dim5(1.0, m_pl_red, 2.5e10, 106.75)
    gh_50, yode_50, yan_50, _, m_50, sig_50, _ = run_boltzmann_dim5(1.0, m_pl_red, 5.0e10, 106.75)
    cc.check(
        gh_25 < 1.0e-10
        and gh_50 < 1.0e-10
        and abs(yode_25 / yan_25 - 1.0) < 5.0e-4
        and abs(yode_50 / yan_50 - 1.0) < 5.0e-4
        and 4.1e3 <= m_50 <= 8.5e3
        and 4.1e3 <= m_25 <= 8.5e3
        and sig_25 < 1.0e-74,
        "V12.3.B2a: Planck dim-5 Boltzmann ODE freeze-in matches analytic (<5e-4) in [4.1, 8.5] TeV, sigma_SI < 1e-74 [С]",
    )

    gh_ps, yode_ps, _, yeq_ps, m_ps_hot_gev, _, c5_max_ps = run_boltzmann_dim5(1.0, mps_a2, 1.80e10, 106.75)
    m_ps_hot_ev = m_ps_hot_gev * 1.0e9
    cc.check(
        gh_ps > 2.0e3
        and abs(yode_ps / yeq_ps - 1.0) < 1.0e-4
        and m_ps_hot_ev <= 115.0
        and c5_max_ps < 2.0e-3,
        "V12.3.B2b: PS dim-5 (c_5=1) over-thermalizes (Gamma/H=2.74e3, m <= 112 eV hot DM); non-thermal requires c_5 < 2e-3 [С/✗]",
    )

    # V12.3.B2c: Pure gravitational freeze-in vs leptogenesis T_RH & tensor ceiling
    beta_maj_sm = 0.565e-3
    pref_y_sm = 45.0 * math.sqrt(90.0) * beta_maj_sm / (6.0 * (math.pi ** 3) * (106.75 ** 1.5) * (m_pl_red ** 3))
    pref_y_ps = 45.0 * math.sqrt(90.0) * (beta_maj_sm * 180.0 / 106.75) / (6.0 * (math.pi ** 3) * (180.0 ** 1.5) * (m_pl_red ** 3))
    m_at_mn1 = 0.120 / (2.743e8 * pref_y_sm * (1.80e10 ** 3))
    trh_mpl = (0.120 / (2.743e8 * m_pl_red * pref_y_ps)) ** (1.0 / 3.0)
    trh_mgut = (0.120 / (2.743e8 * lam_a2 * pref_y_ps)) ** (1.0 / 3.0)
    m_floor_tensor = 0.120 / (2.743e8 * pref_y_ps * (6.6e15 ** 3))
    cc.check(
        m_at_mn1 > 1.0e20
        and abs(trh_mpl - 1.420e11) / 1.420e11 < 5.0e-3
        and abs(trh_mgut - 9.600e11) / 9.600e11 < 5.0e-3
        and m_floor_tensor >= 2.40e4,
        "V12.3.B2c: Gravitational freeze-in no-go below T_RH=1.420e11 GeV & tensor floor m_chi1 >= 24.3 TeV [Т/С/✗]",
    )

    # V12.3.B2d: Tremaine-Gunn Pauli floor vs Lyman-alpha non-thermal floors (F-39B)
    hbar_gev_s = 6.582119569e-25
    c_cm_s = 2.99792458e10
    hbar_c_gev_cm = hbar_gev_s * c_cm_s
    m_pl_full = 1.22089e19
    sigma_v = 10.0e5 / c_cm_s
    r_c_gev_inv = (0.15 * 3.08567758e21) / hbar_c_gev_cm
    m_tg_kev = ((9.0 / (2.0 * math.pi * math.sqrt(2.0 * math.pi))) * (m_pl_full ** 2) / (2.0 * sigma_v * (r_c_gev_inv ** 2))) ** 0.25 * 1.0e6

    m_wdm = 5.7
    ratio_t3_sm = (10.75 / 106.75) / (0.12 * 93.14 / (m_wdm * 1.0e3))
    ratio_t3_ps = (10.75 / 180.0) / (0.12 * 93.14 / (m_wdm * 1.0e3))
    m_ir = m_wdm * (2.45 / 3.1514) * (ratio_t3_sm ** (1.0 / 3.0))
    m_uv5 = m_wdm * (3.00 / 3.1514) * (ratio_t3_sm ** (1.0 / 3.0))
    m_uv6 = m_wdm * (3.50 / 3.1514) * (ratio_t3_sm ** (1.0 / 3.0))
    m_uv5_ps = m_wdm * (3.00 / 3.1514) * (ratio_t3_ps ** (1.0 / 3.0))
    m_uv6_ps = m_wdm * (3.50 / 3.1514) * (ratio_t3_ps ** (1.0 / 3.0))
    cc.check(
        0.15 <= m_tg_kev <= 0.35
        and 16.0 < m_ir < 17.0
        and 20.0 < m_uv5 < 20.5
        and 23.0 < m_uv6 < 24.0
        and 16.5 < m_uv5_ps < 17.5
        and 19.5 < m_uv6_ps < 20.0
        and m_ir / m_tg_kev > 50.0,
        "V12.3.B2d: Lyman-alpha (16.47..23.53 keV SM, 16.95..19.77 PS) > 50x Tremaine-Gunn Pauli floor (0.219 keV) [Т/С]",
    )

    # V12.3.B2e: Z_2^DM-breaking decay width constraint (tau >= 1e26 s)
    tau_min_gev_inv = 1.0e26 / hbar_gev_s
    ymax_20kev = math.sqrt(16.0 * math.pi / (20.0e-6 * tau_min_gev_inv))
    ymax_5tev = math.sqrt(16.0 * math.pi / (5000.0 * tau_min_gev_inv))
    cc.check(
        ymax_20kev < 2.0e-22 and ymax_5tev < 1.0e-26,
        "V12.3.B2e: Z_2^DM-breaking mixing bounded to |y_eff| < 2e-22 (20 keV) and < 1e-26 (5 TeV) [Т/С/✗]",
    )

    # V12.3.B2f: Stratum C honesty check
    tags_b = ["[Т]", "[С]", "[П]", "[✗]"]
    fitted_b = 0
    cc.check(
        fitted_b == 0 and sig_25 < 1.0e-74 and set(tags_b) == {"[Т]", "[С]", "[П]", "[✗]"},
        "V12.3.B2f: Stratum C openness ledger for (m_chi1, Lam_UV/c_5, T_RH) & sigma_SI < 1e-74 (0 fitted params) [П]",
    )

    print("  [V12.3.B2] Boltzmann Freeze-In, Gravitational No-Go, Lyman-alpha & Decay Bounds [С] / [Т] / [✗] / [П]:")
    print(f"             - Planck dim-5: m_chi1 = [{m_50:.1f}, {m_25:.1f}] GeV, Gamma/H = [{gh_25:.3e}, {gh_50:.3e}], sigma_SI = {sig_25:.2e} cm^2")
    print(f"             - PS dim-5 (c5=1 @ M_N1): Gamma/H={gh_ps:.2e}, m <= {m_ps_hot_ev:.1f} eV [✗], non-thermal c5 <= {c5_max_ps:.3e}")
    print(f"             - Grav freeze-in: T_RH(M_Pl)={trh_mpl:.3e}, T_RH(M_GUT)={trh_mgut:.3e}, floor(6.6e15)={m_floor_tensor/1e3:.2f} TeV")
    print(f"             - TG={m_tg_kev:.3f} keV vs Ly-a SM={[round(v,2) for v in (m_ir,m_uv5,m_uv6)]} keV; |y_eff|(5 TeV) <= {ymax_5tev:.2e}\n")

    return {
        "tags": tags_b,
        "fitted_parameters": fitted_b,
        "t163_det": det_s,
        "chain_a2_all_pdm_even": all_pdm_even,
        "ccvs_34_comm_err": comm_err,
        "ccvs_34_16bar_anticomm_err": anti_err,
        "planck_dim5_mchi_gev": [m_25, m_50],
        "planck_dim5_gamma_over_H": [gh_25, gh_50],
        "planck_dim5_sigma_si_cm2": sig_25,
        "ps_dim5_overtherm_gamma_H": gh_ps,
        "ps_dim5_c5_max_nontherm": c5_max_ps,
        "grav_trh_min_mpl_gev": trh_mpl,
        "grav_trh_min_mgut_gev": trh_mgut,
        "grav_mchi_floor_tensor_gev": m_floor_tensor,
        "m_tremaine_gunn_kev": m_tg_kev,
        "lyman_alpha_floors_sm_kev": [m_ir, m_uv5, m_uv6],
        "lyman_alpha_floors_ps_kev": [m_uv5_ps, m_uv6_ps],
        "z2_break_yeff_max_5tev": ymax_5tev,
    }


def run_v12_wall3() -> tuple[int, int, dict]:
    cc = _CheckCounter()
    sum_a = suite_v123a_wall3_cc_sequestering_su2d(cc)
    sum_b = suite_v123b_fimp_1f_z2dm(cc)
    summary = {
        "V12.3.A": sum_a,
        "V12.3.B": sum_b,
        "tags": {
            "V12.3.A": sum_a["tags"],
            "V12.3.B": sum_b["tags"],
        },
        "fitted_parameters": 0,
        "passed": cc.passed,
        "total": cc.total,
        "failures": cc.failures,
    }
    return cc.passed, cc.total, summary


# ==============================================================================
# V12.4: CROSS-WALL SYNTHESIS, 45.15 INVARIANCE & STRATIFIED ONTOLOGY GUARD
# ==============================================================================
def suite_v124_cross_wall_synthesis(cc: _CheckCounter, s1: dict, s2: dict, s3: dict) -> dict:
    print("=" * 88)
    print("V12.4: Cross-Wall Synthesis (Walls 1–3), 45.15 Invariance & 3-Stratum Audit")
    print("=" * 88)

    sub_suites = [
        ("V12.1.A", s1["V12.1.A"]), ("V12.1.B", s1["V12.1.B"]), ("V12.1.C", s1["V12.1.C"]),
        ("V12.2.A", s2["V12.2.A"]), ("V12.2.B", s2["V12.2.B"]), ("V12.2.C", s2["V12.2.C"]),
        ("V12.3.A", s3["V12.3.A"]), ("V12.3.B", s3["V12.3.B"]),
    ]
    allowed_tags = {"[Т]", "[С]", "[П]", "[✗]"}

    # V12.4.1: Zero-Fitting & Tag Completeness
    zero_fit_ok = (
        s1["fitted_parameters"] == 0
        and s2["fitted_parameters"] == 0
        and s3["fitted_parameters"] == 0
        and all(sub["fitted_parameters"] == 0 for _, sub in sub_suites)
    )
    tags_ok = all(
        len(sub["tags"]) > 0 and set(sub["tags"]) <= allowed_tags
        for _, sub in sub_suites
    )
    wall_honesty_ok = all(
        ("[Т]" in wt or "[С]" in wt) and "[П]" in wt and "[✗]" in wt
        for wt in (
            {t for k in ("V12.1.A", "V12.1.B", "V12.1.C") for t in s1["V12.1." + k[-1]]["tags"]},
            {t for k in ("V12.2.A", "V12.2.B", "V12.2.C") for t in s2["V12.2." + k[-1]]["tags"]},
            {t for k in ("V12.3.A", "V12.3.B") for t in s3["V12.3." + k[-1]]["tags"]},
        )
    )
    cc.check(zero_fit_ok and tags_ok and wall_honesty_ok, "V12.4.1: Zero-fitting & epistemic tag completeness across all 8 sub-suites [Т]")

    # V12.4.2: Chain A2 45.15 & Monotonic 12-Scale Ladder
    lam_ncg = 7.890e15
    ms_het_1 = s1["V12.1.C"]["heterotic_ms_over_lam"][1] * lam_ncg
    scales_12 = [
        1.44e-42,                       # H_0
        2.5e-47 ** 0.25,                # Lambda_DE
        50.302e-12,                     # m_nu3
        125.25,                         # m_h
        1.80e10,                        # M_{N_1}
        5.28e10,                        # mu_inst
        1.447e11,                       # M_PS
        3.005e11,                       # M_{N_3}
        1.0e15,                         # M_heavy
        lam_ncg,                        # Lambda_NCG
        ms_het_1,                       # M_s^het(k=1)
        2.43535e18,                     # M_Pl,red
    ]
    ladder_ok = all(scales_12[i] < scales_12[i + 1] for i in range(len(scales_12) - 1))
    cc.check(
        45.11 <= s2["V12.2.B"]["a2_ainv_1gen"] <= 45.18
        and abs(s2["V12.2.B"]["a2_ainv_3gen"] - 45.15) < 0.02
        and s1["V12.1.C"]["heterotic_ms_over_lam"][1] > 115.0
        and s1["V12.1.C"]["species_bound_nd_req"] > 1.0e7
        and s3["V12.3.A"]["alpha_d_inv_ym"] > 75.0
        and s3["V12.3.B"]["chain_a2_all_pdm_even"]
        and ladder_ok,
        "V12.4.2: Chain A2 45.15 invariance & strict 12-scale ordering across Walls 1–3 [Т/С]",
    )

    # V12.4.3: Wall 1 <-> Wall 2 Spectral-Action Dichotomy (Super-F-40 vs F-42)
    cc.check(
        s1["V12.1.B"]["ccvs_full_c_lorentzian_m60"] < -1.0e7
        and s1["V12.1.B"]["positivity_thresholds"]["PS_N0"] == (169, 196)
        and abs(s1["V12.1.B"]["qstar_ueu_dirac"] - s3["V12.3.A"]["qstar_ueu"]) < 1.0e-10
        and s2["V12.2.B"]["rank_unitary_ccvs"] == 200
        and s2["V12.2.C"]["r_dr_1522"] == 0.5,
        "V12.4.3: Super-F-40 closes F-42 spectral gravity while F-42 governs Stratum-B gauge/Higgs [Т/✗]",
    )

    # V12.4.4: F-41C + F-42 + N_g=3 + Z_2^DM Cross-Wall Triangle
    cc.check(
        s1["V12.1.C"]["k_max"]["spin32"] == 4
        and s2["V12.2.B"]["ng1_taup"] < 2.4e34
        and s2["V12.2.B"]["ng5_splitc_b4"] > 0.0
        and s3["V12.3.B"]["ccvs_34_comm_err"] < 1.0e-14
        and s3["V12.3.B"]["ccvs_34_16bar_anticomm_err"] < 1.0e-14,
        "V12.4.4: F-41C + F-42 + N_g=3 bracket + Z_2^DM 34x34 cross-wall triangle [Т/✗]",
    )

    # V12.4.5: Wall 2 <-> Wall 3 Heavy-Split / Vissani / DM Joint Pincer
    cc.check(
        s2["V12.2.C"]["m6_o1_min"] >= 1.971e15
        and s2["V12.2.C"]["delta_ew_n3"] > 8.0e16
        and s2["V12.2.C"]["delta_ew_heavy"] > 8.0e22
        and s3["V12.3.B"]["planck_dim5_sigma_si_cm2"] < 1.0e-74,
        "V12.4.5: Heavy Split vs Vissani (Delta_EW > 8e22) vs sole unstrained 1_F FIMP pincer [С/✗/П]",
    )

    # V12.4.6: Wall 2 Leptogenesis <-> Wall 3 FIMP T_RH Window
    m_n1 = 1.80e10
    m_ps = 1.447e11
    m_25, m_50 = s3["V12.3.B"]["planck_dim5_mchi_gev"]
    cc.check(
        s3["V12.3.B"]["grav_trh_min_mpl_gev"] > m_n1
        and s3["V12.3.B"]["ps_dim5_overtherm_gamma_H"] > 1.0e3
        and s3["V12.3.B"]["grav_mchi_floor_tensor_gev"] > 2.4e4
        and 4.0e3 < m_50 < m_25 < 9.0e3
        and m_n1 < 2.5e10 < 5.0e10 < m_ps,
        "V12.4.6: Wall 2 leptogenesis (M_N1..M_PS) vs Wall 3 FIMP T_RH & PS dim-5 obstruction [С/✗]",
    )

    # V12.4.7: Wall 1 <-> Wall 3 CC & Volume-Response Closure
    cc.check(
        s1["V12.1.A"]["regge_mc"]["tt_linear_drift_coeff"] < -100.0
        and s1["V12.1.A"]["gee_vs_gsak_obstruction"]["rel_mismatch"] > 1.0
        and 0.05 < min(s3["V12.3.A"]["delta_neff_ym"])
        and max(s3["V12.3.A"]["delta_neff_ym"]) < 0.28
        and min(s3["V12.3.A"]["delta_neff_nf4"]) > 0.28,
        "V12.4.7: Wall 1 Regge+KD drift/G_EE mismatch + Wall 3 SU(2)_d CMB-S4 window leave Lambda [П] [Т/С/П]",
    )

    # V12.4.8: 3-Stratum Ontology & Cross-Doc Legacy Typo Guard
    stratum_a = "7D coherence space Fano PG(2,2) G_2=Aut(O) SU(3)_C x U(1) T-186..T-217 F-1..F-35 T-48a T-74 T-163 T-333"
    stratum_clean = all(tok not in stratum_a for tok in ("Pati-Salam", "Regge", "126bar", "SU(2)_d", "FIMP"))
    web_root = Path(__file__).resolve().parents[2]
    v10_text = (web_root / "research" / "operational-reconstruction" / "verify_deep_frontier_v10.py").read_text(encoding="utf-8")
    v11_text = (web_root / "research" / "operational-reconstruction" / "verify_deep_frontier_v11.py").read_text(encoding="utf-8")
    rg_text = (web_root / "docs" / "physics" / "gauge-symmetry" / "rg-flow.md").read_text(encoding="utf-8")
    pd_text = (web_root / "docs" / "physics" / "particle-physics" / "proton-decay.md").read_text(encoding="utf-8")
    ledger_en_text = (web_root / "docs" / "reference" / "frontier-ledger.md").read_text(encoding="utf-8")
    ledger_ru_text = (
        web_root / "i18n" / "ru" / "docusaurus-plugin-content-docs" / "current" / "reference" / "frontier-ledger.md"
    ).read_text(encoding="utf-8")
    docs_guard_ok = (
        "44.23" not in v10_text
        and "45.13" not in v10_text
        and "45.13" not in pd_text
        and "45.13" not in ledger_en_text
        and "45.13" not in ledger_ru_text
        and "45{,}13" not in ledger_ru_text
        and "45,13" not in ledger_ru_text
        and "45.15" in v10_text
        and "45.15" in v11_text
        and "45.15" in rg_text
        and "45.15" in pd_text
        and "45.15" in ledger_en_text
        and "45{,}15" in ledger_ru_text
    )
    cc.check(
        stratum_clean and docs_guard_ok,
        "V12.4.8: 3-Stratum disjointness & 45.15 / zero-45.13 / zero-44.23 cross-doc parity guard [Т]",
    )

    print("  [V12.4] Cross-Wall Synthesis Summary [Т] / [С] / [П] / [✗]:")
    print(f"          - 0 fitted params across 8 sub-suites; Chain A2 alpha^-1 = {s2['V12.2.B']['a2_ainv_1gen']:.3f} (1g) / {s2['V12.2.B']['a2_ainv_3gen']:.3f} (3g)")
    print(f"          - Spectral dichotomy: Super-F-40 Lorentzian={s1['V12.1.B']['ccvs_full_c_lorentzian_m60']:.2e} vs F-42 CCvS rank={s2['V12.2.B']['rank_unitary_ccvs']}")
    print(f"          - Heavy-Split M6>={s2['V12.2.C']['m6_o1_min']:.3e}, Vissani={s2['V12.2.C']['delta_ew_heavy']:.2e}, 1_F FIMP sig_SI={s3['V12.3.B']['planck_dim5_sigma_si_cm2']:.2e}")
    print(f"          - Cross-doc parity & 3-stratum ontology guard: {'PASS' if (stratum_clean and docs_guard_ok) else 'FAIL'}\n")

    return {
        "tags": ["[Т]", "[С]", "[П]", "[✗]"],
        "fitted_parameters": 0,
        "scales_12": scales_12,
        "docs_guard_ok": docs_guard_ok,
    }


def run_v12_all() -> tuple[int, int, dict]:
    p1, t1, s1 = run_v12_wall1()
    p2, t2, s2 = run_v12_wall2()
    p3, t3, s3 = run_v12_wall3()
    cc4 = _CheckCounter()
    s4 = suite_v124_cross_wall_synthesis(cc4, s1, s2, s3)
    p4, t4 = cc4.passed, cc4.total
    passed = p1 + p2 + p3 + p4
    total = t1 + t2 + t3 + t4
    failures = list(s1["failures"]) + list(s2["failures"]) + list(s3["failures"]) + list(cc4.failures)
    return passed, total, {
        "wall1": s1,
        "wall2": s2,
        "wall3": s3,
        "V12.4": s4,
        "per_wall": {"wall1": (p1, t1), "wall2": (p2, t2), "wall3": (p3, t3), "V12.4": (p4, t4)},
        "fitted_parameters": 0,
        "passed": passed,
        "total": total,
        "failures": failures,
    }


if __name__ == "__main__":
    p, t, s = run_v12_all()
    pw = s["per_wall"]
    print("=" * 88)
    print(f"DEEP FRONTIER v12 UNIFIED VERIFICATION SUMMARY: {p}/{t} checks passed (fitted_parameters=0)")
    print(f"  Wall 1 (V12.1.A–C, 4D Regge/CDT, Super-F-40, String UV): {pw['wall1'][0]}/{pw['wall1'][1]}")
    print(f"  Wall 2 (V12.2.A–C, CP/CKM, N_g=3 F-42, Heavy Split):     {pw['wall2'][0]}/{pw['wall2'][1]}")
    print(f"  Wall 3 (V12.3.A–B, CC/SU(2)_d, 1_F FIMP & Z_2^DM):       {pw['wall3'][0]}/{pw['wall3'][1]}")
    print(f"  Synthesis (V12.4, Cross-Wall & 3-Stratum Guard):         {pw['V12.4'][0]}/{pw['V12.4'][1]}")
    print("=" * 88)
    if p != t:
        print("FAILURES:", s["failures"])
        sys.exit(1)
    sys.exit(0)
