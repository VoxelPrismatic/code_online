var stderr = "";
var stdout = "";
var stdrtn = null;
var stdinp = (document.getElementById("SYSINP").innerHTML || "return null;");
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
stderr = (stderr || "~");
stdout = (stdout || "~");
document.getElementById("SYSINP").innerHTML = (stdinp.replace('\n','<br>')).replace(' ','\u200b ');
document.getElementById("SYSOUT").innerHTML = (stdout.replace('\n','<br>')).replace(' ','\u200b ');
document.getElementById("SYSERR").innerHTML = (stderr.replace('\n','<br>')).replace(' ','\u200b ');
document.getElementById("SYSRTN").innerHTML = (((typeof stdrtn)+" ] "+stdrtn).replace('\n','<br>')).replace(' ','\u200b ');

