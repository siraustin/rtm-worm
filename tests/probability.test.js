'use strict';
const assert = require('node:assert/strict');
const { atLeastOne, mount } = require('../assets/probability.js');
assert.equal(atLeastOne(0), 0);
assert.ok(Math.abs(atLeastOne(1) - 1 / 7) < 1e-14);
assert.ok(Math.abs(atLeastOne(7) - (1 - (6 / 7) ** 7)) < 1e-14);
assert.equal((100 * atLeastOne(20)).toFixed(1), '95.4');
for (let k = 1; k <= 100; k++) {
  assert.ok(atLeastOne(k) > atLeastOne(k - 1));
  assert.ok(atLeastOne(k) >= 0 && atLeastOne(k) <= 1);
}
for (const bad of [-1, 101, 0.5, NaN, Infinity, '7', null, undefined]) {
  assert.throws(() => atLeastOne(bad), RangeError);
}
function element(value = '') {
  return { value, hidden: true, textContent: '', handlers: {}, attributes: {},
    addEventListener(name, handler) { this.handlers[name] = handler; },
    setAttribute(name, value) { this.attributes[name] = value; },
    removeAttribute(name) { delete this.attributes[name]; } };
}
const nodes = { trials: element('7'), 'probability-result': element(),
  'probability-controls': element(), 'reset-trials': element() };
mount({ getElementById: id => nodes[id] || null });
assert.equal(nodes['probability-controls'].hidden, false);
assert.match(nodes['probability-result'].textContent, /66\.0%/);
nodes.trials.value = '20'; nodes.trials.handlers.input();
assert.match(nodes['probability-result'].textContent, /95\.4%/);
nodes.trials.value = '100'; nodes.trials.handlers.input();
assert.match(nodes['probability-result'].textContent, />99\.9%/);
assert.doesNotMatch(nodes['probability-result'].textContent, /100\.0%/);
nodes.trials.value = '101'; nodes.trials.handlers.input();
assert.equal(nodes.trials.attributes['aria-invalid'], 'true');
nodes['reset-trials'].handlers.click();
assert.equal(nodes.trials.value, '0');
assert.equal(nodes.trials.attributes['aria-invalid'], undefined);
assert.match(nodes['probability-result'].textContent, /0\.0%/);
mount({ getElementById: () => null });
console.log('PASS: probability endpoints, monotonicity, invalid inputs, DOM update, reset, missing widget.');
