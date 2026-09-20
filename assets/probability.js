/* An independent-trial illustration, NOT worm emulation or host telemetry. */
(function (root) {
  'use strict';
  var MAX_TRIALS = 100;
  function atLeastOne(k) {
    if (!Number.isInteger(k) || k < 0 || k > MAX_TRIALS) {
      throw new RangeError('Trials must be an integer from 0 to 100.');
    }
    return -Math.expm1(k * Math.log1p(-1 / 7));
  }
  function mount(doc) {
    var input = doc.getElementById('trials');
    var result = doc.getElementById('probability-result');
    if (!input || !result) return;
    var controls = doc.getElementById('probability-controls');
    function render() {
      var k = Number(input.value);
      if (!Number.isInteger(k) || k < 0 || k > MAX_TRIALS) {
        input.setAttribute('aria-invalid', 'true');
        result.textContent = 'Choose a whole number from 0 to 100.';
        return;
      }
      input.removeAttribute('aria-invalid');
      var percent = 100 * atLeastOne(k);
      var display = percent >= 99.95 ? '>99.9' : percent.toFixed(1);
      result.textContent = k + ' trials: ' + display +
        '% chance of at least one event; ' + (k / 7).toFixed(2) +
        ' expected events. Neither number predicts an outage.';
    }
    input.addEventListener('input', render);
    doc.getElementById('reset-trials').addEventListener('click', function () {
      input.value = '0';
      render();
    });
    controls.hidden = false;
    render();
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { atLeastOne: atLeastOne, mount: mount };
  }
  if (root && root.document) mount(root.document);
})(typeof window !== 'undefined' ? window : null);
