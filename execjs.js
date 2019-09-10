var url = document.URL+"";
var tokens = url.split("?.");
var code = "";
for (token of tokens) {
    if (token.search("code=")==0) {
        code += token.slice(5)+"";
    }
}
var sysinp = document.createElement("DIV");
var sysout = document.createElement("DIV");
var sysrtn = document.createElement("DIV");
var syserr = document.createElement("DIV");
sysinp.style.color = "#ff00ffff";
sysout.style.color = "#00ffffff";
sysrtn.style.color = "#00ff00ff";
syserr.style.color = "#ff0000ff";
var stderr = "";
var stdout = "";
var stdinp = decodeURIComponent(code)+"";
var stdrtn;
(function(){
    oldLog = console.log;
    console.log = function(...args){ 
        for (arg of args) { stdout += arg+""; }
        stdout += "\n";};})();
try { 
    stdrtn = eval("(function(){"+stdinp+";})();");
} catch(ex) { 
    stderr = ex.message; 
}
var txtinp = document.createTextNode(stdinp || "'?.code=' tag not found;");
var txtout = document.createTextNode(stdout.replace('\n', '<br>.') || "*~");
var txtrtn = document.createTextNode((typeof stdrtn)+" ] "+stdrtn);
var txterr = document.createTextNode(stderr || "*~");
sysinp.appendChild(txtinp);
sysout.appendChild(txtout);
sysrtn.appendChild(txtrtn);
syserr.appendChild(txterr);
document.body.appendChild(sysinp);
document.body.appendChild(sysout);
document.body.appendChild(syserr);
document.body.appendChild(sysrtn);
