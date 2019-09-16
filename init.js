var url = decodeURIComponent(document.URL+"")+"";
var tokens = url.split("?.");
var lang = "";
var stdinp = "";
for (token of tokens) {
  if (token.search("lang=")==0) {
    lang += token.slice(5)+"".toLowerCase();
  } else if (token.search("code=")==0) {
    stdinp += token.slice(5)+"";
  }
}
var javakw = ["java"];
var cppkw = ["cpp", "c++"];
var pykw = ["py", "python"];
var jskw = ["js", "javascript"];
var rbkw = ["rb", "ruby"];
var swiftkw = ["swift", "sft", "sw"];
var truthkw = ['tr', 'truth'];

/*GEN SITE*/
var syslng = document.createElement('DIV');
var sysinp = document.createElement('DIV');
var sysout = document.createElement('DIV');
var syserr = document.createElement('DIV');
var sysrtn = document.createElement('DIV');
var txtlng = document.createTextNode('~');
var txtinp = document.createTextNode(`${stdinp}`);
var txtout = document.createTextNode('~');
var txterr = document.createTextNode('~');
var txtrtn = document.createTextNode('~');
syslng.id = 'SYSLNG';
sysinp.id = 'SYSINP';
sysout.id = 'SYSOUT';
syserr.id = 'SYSERR';
sysrtn.id = 'SYSRTN';
syslng.style.color = "#ffffffff";
sysinp.style.color = "#ff00ffff";
sysout.style.color = "#00ffffff";
syserr.style.color = "#ff0000ff";
sysrtn.style.color = "#00ff00ff";
syslng.appendChild(txtlng);
sysinp.appendChild(txtinp);
sysout.appendChild(txtout);
syserr.appendChild(txterr);
sysrtn.appendChild(txtrtn);
document.body.appendChild(syslng);
document.body.appendChild(sysinp);
document.body.appendChild(sysout);
document.body.appendChild(syserr);
document.body.appendChild(sysrtn);
