/* INIT */
var url = decodeURIComponent(document.URL+"")+"";
var stdinp = document.getElementById("SYSINP").innerHTML
var lang = url.split("?.lang=")[1];
var javakw = ["java"];
var cppkw = ["cpp", "c++"];
var pykw = ["py", "python"];
var jskw = ["js", "javascript"];
var rbkw = ["rb", "ruby"];
var swiftkw = ["swift", "sft", "sw"];
var truthkw = ['tr', 'truth'];

/* LOADER */
var executor = document.createElement("SCRIPT");
function write(a, b, c, d) {
  document.getElementById("SYSLNG").innerHTML = a;
  document.getElementById("SYSOUT").innerHTML = b;
  document.getElementById("SYSERR").innerHTML = c;
  document.getElementById("SYSRTN").innerHTML = d;
}
function create(typ, src, lng) {
  executor.type = typ;
  executor.src = src;
  document.getElementById("SYSLNG").innerHTML = lng;
  document.body.appendChild(executor)
}
// NO CODE
if (stdinp == "") {
  write("LANG ] *.*", "~", "'?.code=' tag not provided in URL", "code_online/?.code=<s>...</s>?.lang=<s>...</s>");
} 
//JS
else if (jskw.indexOf(lang) > -1) {
  create("text/javascript","exe/execjs.js","LANG ] *.JS");
}
//PY
else if (pykw.indexOf(lang) > -1) {
  create("text/python","exe/execpy.py","LANG ] *.PY");
}
else if (truthkw.indexOf(lang) > -1) {
  create("text/python","exe/exectruth.py","LANG ] *.BIN");
}
//??
else {
  write("LANG ] *.*", "Supported languages: 'js', 'javascript', 'py', 'python', 'tr', 'truth",
        "'?.lang=' tag not provided in URL", "code_online/?.code=<s>...</s>?.lang=<s>...</s>");
}
