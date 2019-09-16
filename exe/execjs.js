var stderr = "~";
var stdout = "~";
var stdrtn = null;
var stdinp = document.getElementById("SYSINP").innerHTML;
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
document.getElementById("SYSINP").innerHTML = "(function(){\n"+stdinp.replace('\n','\n    ')+"\n;})();";
document.getElementById("SYSOUT").innerHTML = stdout;
document.getElementById("SYSERR").innerHTML = stderr;
document.getElementById("SYSRTN").innerHTML = (typeof stdrtn)+" ] "+stdrtn;

