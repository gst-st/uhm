import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const source = await readFile(new URL('./model.ts', import.meta.url), 'utf8');
const compiled = ts.transpileModule(source, {compilerOptions: {module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022}}).outputText;
const {BASIS, FANO_LINES, FREQUENCIES, illustrativeState, pairReadout} = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString('base64')}`);
const near = (actual, expected, tolerance = 1e-12) => assert.ok(Math.abs(actual - expected) < tolerance, `${actual} ≠ ${expected}`);

test('the oriented Fano triples cover each unordered basis pair exactly once', () => {
  assert.deepEqual(BASIS, ['A', 'S', 'D', 'L', 'E', 'U', 'O']);
  const pairs = [];
  for (const [a, b, c] of FANO_LINES) {
    assert.equal(new Set([a, b, c]).size, 3);
    for (const [i, j] of [[a, b], [b, c], [c, a]]) pairs.push([i, j].sort((x, y) => x - y).join(','));
  }
  assert.equal(pairs.length, 21);
  assert.equal(new Set(pairs).size, 21);
  for (let i = 1; i <= 7; i++) assert.equal(FANO_LINES.filter((line) => line.includes(i)).length, 3);
});

test('all sampled matrices are Hermitian, trace one, and positive semidefinite', () => {
  for (const strength of [0, .01, .25, .5, .75, .99, 1]) {
    for (const time of [0, .5, 8, 250]) {
      const {matrix, phases, eigenvalues} = illustrativeState(strength, time);
      near(matrix.reduce((trace, row, i) => trace + row[i].re, 0), 1);
      assert.ok(eigenvalues.every((value) => value >= 0));
      near(eigenvalues.reduce((sum, value) => sum + value, 0), 1);
      for (let i = 0; i < 7; i++) {
        let real = 0; let imaginary = 0;
        for (let j = 0; j < 7; j++) {
          near(matrix[i][j].re, matrix[j][i].re);
          near(matrix[i][j].im, -matrix[j][i].im);
          // The rank-one part is exactly s ψψ†; the residual is (1−s)I/7.
          near(matrix[i][j].re - strength / 7 * Math.cos(phases[i] - phases[j]), i === j ? (1 - strength) / 7 : 0);
          near(matrix[i][j].im - strength / 7 * Math.sin(phases[i] - phases[j]), 0);
          real += matrix[i][j].re * Math.cos(phases[j]) - matrix[i][j].im * Math.sin(phases[j]);
          imaginary += matrix[i][j].re * Math.sin(phases[j]) + matrix[i][j].im * Math.cos(phases[j]);
        }
        near(real, eigenvalues[0] * Math.cos(phases[i]));
        near(imaginary, eigenvalues[0] * Math.sin(phases[i]));
      }
    }
  }
});

test('displayed invariants equal direct matrix computations throughout the slider', () => {
  for (let k = 0; k <= 100; k++) {
    const state = illustrativeState(k / 100, 3.7);
    const purity = state.matrix.flat().reduce((sum, z) => sum + z.re ** 2 + z.im ** 2, 0);
    const diagonal = state.matrix.reduce((sum, row, i) => sum + row[i].re ** 2, 0);
    near(state.purity, purity);
    near(state.integration, (purity - diagonal) / diagonal);
    near(state.reflection, 1 / (7 * purity));
    near(state.integration, 7 * state.purity - 1);
    assert.equal(state.inSelectedWindow, state.purity > 2 / 7 && state.purity <= 3 / 7);
  }
  assert.equal(illustrativeState(0).inSelectedWindow, false);
  assert.equal(illustrativeState(.5).inSelectedWindow, true);
  assert.equal(illustrativeState(1).inSelectedWindow, false);
});

test('phase evolution is the stated diagonal unitary conjugation and preserves invariants', () => {
  const start = illustrativeState(.53, 0);
  const time = 3.7;
  const end = illustrativeState(.53, time);
  for (let i = 0; i < 7; i++) for (let j = 0; j < 7; j++) {
    const phase = -(FREQUENCIES[i] - FREQUENCIES[j]) * time;
    const z = start.matrix[i][j];
    near(end.matrix[i][j].re, z.re * Math.cos(phase) - z.im * Math.sin(phase));
    near(end.matrix[i][j].im, z.re * Math.sin(phase) + z.im * Math.cos(phase));
  }
  near(start.purity, end.purity);
  near(start.integration, end.integration);
  near(start.reflection, end.reflection);
});

test('invalid slider states and times are rejected', () => {
  for (const value of [-1, 1.01, NaN, Infinity]) assert.throws(() => illustrativeState(value), RangeError);
  for (const value of [NaN, Infinity, -Infinity]) assert.throws(() => illustrativeState(.5, value), RangeError);
});

test('both readout settings form a complete projective measurement with the stated imaginary sign', () => {
  const multiply = (a, b) => ({re: a.re * b.re - a.im * b.im, im: a.re * b.im + a.im * b.re});
  const conjugate = (a) => ({re: a.re, im: -a.im});
  const expectation = (matrix, vector) => {
    const result = {re: 0, im: 0};
    for (let i = 0; i < 7; i++) for (let j = 0; j < 7; j++) {
      const term = multiply(multiply(conjugate(vector[i]), matrix[i][j]), vector[j]);
      result.re += term.re; result.im += term.im;
    }
    near(result.im, 0);
    return result.re;
  };
  for (const setting of ['real', 'imaginary']) {
    const plus = Array.from({length: 7}, () => ({re: 0, im: 0}));
    const minus = Array.from({length: 7}, () => ({re: 0, im: 0}));
    plus[0] = minus[0] = {re: 1 / Math.sqrt(2), im: 0};
    plus[1] = setting === 'real' ? {re: 1 / Math.sqrt(2), im: 0} : {re: 0, im: -1 / Math.sqrt(2)};
    minus[1] = {re: -plus[1].re, im: -plus[1].im};
    // Π+ + Π− + Πrest = I, and the two rank-one effects are orthogonal.
    let overlap = {re: 0, im: 0};
    for (let i = 0; i < 7; i++) {
      const term = multiply(conjugate(plus[i]), minus[i]);
      overlap.re += term.re; overlap.im += term.im;
      for (let j = 0; j < 7; j++) {
        const first = multiply(plus[i], conjugate(plus[j]));
        const second = multiply(minus[i], conjugate(minus[j]));
        near(first.re + second.re + (i === j && i > 1 ? 1 : 0), i === j ? 1 : 0);
        near(first.im + second.im, 0);
      }
    }
    near(overlap.re, 0); near(overlap.im, 0);
    for (let k = 0; k <= 100; k++) for (const time of [0, 3.7, 21]) {
      const {matrix} = illustrativeState(k / 100, time);
      const probabilities = pairReadout(matrix, setting);
      near(probabilities.plus, expectation(matrix, plus));
      near(probabilities.minus, expectation(matrix, minus));
      near(probabilities.rest, 5 / 7);
      near(probabilities.plus + probabilities.minus + probabilities.rest, 1);
      assert.ok([probabilities.plus, probabilities.minus, probabilities.rest].every((p) => p >= 0 && p <= 1));
    }
  }
});
