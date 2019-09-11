/* LOADER */
var executor = document.createElement("SCRIPT");
// NO CODE
if (stdinp == "") {
  document.getElementById("SYSLNG").innerHTML = "LANG ] *.*";
  document.getElementById("SYSOUT").innerHTML = "~";
  document.getElementById("SYSERR").innerHTML = "'?.code=' tag not provided in URL";
  document.getElementById("SYSRTN").innerHTML = "? ] ?";
} 
//JS
else if (jskw.indexOf(lang) > -1) {
  executor.type = "text/javascript";
  executor.src = "exe/execjs.js";
  document.getElementById("SYSLNG").innerHTML = "LANG ] *.JS";
  document.body.appendChild(executor);
}
//PY
else if (pykw.indexOf(lang) > -1) {
  executor.type = "text/python";
  executor.src = "exe/execpy.py";
  document.getElementById("SYSLNG").innerHTML = "LANG ] *.PY";
  document.body.appendChild(executor);
}
//??
else {
  document.getElementById("SYSLNG").innerHTML = "LANG ] *.*";
  document.getElementById("SYSOUT").innerHTML = "Supported languages: 'js', 'javascript', 'py', 'python'";
  document.getElementById("SYSERR").innerHTML = "'?.lang=' tag not provided in URL";
  document.getElementById("SYSRTN").innerHTML = "? ] ?";
}
