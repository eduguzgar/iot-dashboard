/* Random */

function randomNumber(min, max, decimalPlaces) {
  var rand =
    Math.random() < 0.5
      ? (1 - Math.random()) * (max - min) + min
      : Math.random() * (max - min) + min; // could be min or max or anything in between
  var power = Math.pow(10, decimalPlaces);
  return Math.floor(rand * power) / power;
}

function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

/* Values */

function avg(array) {
  var sum = 0;
  for (var i = 0; i < array.length; i++) {
    if (!isNaN(array[i]) && array[i]) {
      sum += parseFloat(array[i]);
    }
  }
  return sum / array.length;
}

function min(array) {
  var min = parseFloat(array[0]);
  for (var i = 1; i < array.length; i++) {
    if (!isNaN(array[i]) && array[i]) {
      if (array[i] < min) {
        min = parseFloat(array[i]);
      }
    }
  }
  return min;
}

function max(array) {
  var max = parseFloat(array[0]);
  for (var i = 1; i < array.length; i++) {
    if (!isNaN(array[i]) && array[i]) {
      if (array[i] > max) {
        max = parseFloat(array[i]);
      }
    }
  }
  return max;
}