import textwrap
from browser import document as doc, alert
import traceback, io
from contextlib import redirect_stdout as rdout
url = str(doc.URL)
code = ""
tokens = url.split("?.")
for token in tokens:
    if token.startswith('code='):
        code = token[5:]
temp_dict = {}
out = io.StringIO()
expr('def fn():\n'+textwrap.indent(stdinp, "     "), temp_dict)
stdrtn, stdout, stderr, stdinp = "", "", "", ""
sysinp = document.createElement("DIV")
sysout = document.createElement("DIV")
syserr = document.createElement("DIV")
sysrtn = document.createElement("DIV")
sysinp.style.color = "#ff00ffff"
sysout.style.color = "#00ffffff"
sysrtn.style.color = "#00ff00ff"
syserr.style.color = "#ff0000ff"
try: 
    with rdout(out): 
        stdrtn = temp_dict['fn']()
    stdout = str(out.get_value()).replace('\n','<br >');
except Exception as exc: 
    stderr = str(ex)+'<br >'+' \u200b'.join(str(traceback.format_exc()).replace('\n').split())
txtinp = document.createTextNode(stdinp or "'?.code=' tag not found;")
txtout = document.createTextNode(stdout or "*~")
txtrtn = document.createTextNode((str(type(stdrtn)).split("'")[1])+" ] "+stdrtn)
txterr = document.createTextNode(stderr or "*~")
sysinp.append(txtinp)
sysout.append(txtout)
sysrtn.append(txtrtn)
syserr.append(txterr);
document.body.append(sysinp)
document.body.append(sysout)
document.body.append(syserr)
document.body.append(sysrtn)
