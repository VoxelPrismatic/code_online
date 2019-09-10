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
exec('def fn():\n'+textwrap.indent(stdinp, "     "), temp_dict)
stdrtn, stdout, stderr, stdinp = "", "", "", ""
sysinp = doc.createElement("DIV")
sysout = doc.createElement("DIV")
syserr = doc.createElement("DIV")
sysrtn = doc.createElement("DIV")
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
txtinp = doc.createTextNode(stdinp or "'?.code=' tag not found;")
txtout = doc.createTextNode(stdout or "*~")
txtrtn = doc.createTextNode((str(type(stdrtn)).split("'")[1])+" ] "+stdrtn)
txterr = soc.createTextNode(stderr or "*~")
sysinp.append(txtinp)
sysout.append(txtout)
sysrtn.append(txtrtn)
syserr.append(txterr)
doc.body.append(sysinp)
doc.body.append(sysout)
doc.body.append(syserr)
doc.body.append(sysrtn)
