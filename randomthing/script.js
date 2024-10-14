function temp(){
  var c = document.getElementById("celsius").value;
  var f = (c * 9/5) + 32;
  document.getElementById("fahrenheit").value = f;
}

function weight(){
  var kg = document.getElementById("kilo").value;
  var pd = kg * 2.2;
  document.getElementById("pounds").value = pd;
}

function distance(){
  var km = document.getElementById('km').value;
  var m = km * 0.62137;
  document.getElementById("miles").value = m;
}