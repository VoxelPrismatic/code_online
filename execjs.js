var sysout = document.createElement("DIV");
var sysrtn = document.createElement("DIV");
var syserr = document.createElement("DIV");
sysout.style.color = "#00ffffff";
sysrtn.style.color = "#00ff00ff";
syserr.style.color = "#ff0000ff";
var stderr = "";
var stdout = "";
var stdrtn;
var stdinp = document.getElementById("CODE").inmerHTML;
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
var txtout = document.createTextNode(stdout.replace('\n', '<br>.') || "*~");
var txtrtn = document.createTextNode((typeof stdrtn)+" ] "+stdrtn);
var txterr = document.createTextNode(stderr || "*~");
sysout.appendChild(txtout);
sysrtn.appendChild(txtrtn);
syserr.appendChild(txterr);
document.body.appendChild(sysout);
document.body.appendChild(syserr);
document.body.appendChild(sysrtn);
