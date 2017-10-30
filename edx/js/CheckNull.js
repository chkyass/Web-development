var testvariable = '';
var isUndefined = (testvariable === undefined);
var isNull = (testvariable === null);
var isEmpty = (testvariable === '');
document.getElementById('isUndefined').innerHTML = isUndefined;
document.getElementById('isNull').innerHTML = isNull;
document.getElementById('isEmpty').innerHTML = isEmpty;