from io import StringIO
from urllib.parse import unquote
from traceback import format_exc as fex
from textwrap import indent
from browser import document as doc, alert
from contextlib import redirect_stdout as rdout
url = str(doc.URL)
code = ""
tokens = url.split("?.")
for token in tokens:
    if token.startswith('code='):
        code = token[5:]
stdinp = unquote(code)
if not stdinp: stdinp = "pass"
temp_dict = {}
out = StringIO()
exec('def fn():\n'+indent(stdinp, "     "), temp_dict)
stdrtn, stdout, stderr = "", "", ""
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
    stdout = str(out.getvalue()).replace('\n','<br />\u200b');
except Exception as exc: 
    stderr = str(ex)+'<br />'+str(fex()).replace('\n', '<br />\u200b').replace(' ','\u200b \u200b')
txtinp = doc.createTextNode(stdinp or "'?.code=' tag not found;")
txtout = doc.createTextNode(stdout or "*~")
txtrtn = doc.createTextNode((str(type(stdrtn)).split("'")[1])+" ] "+str(stdrtn))
txterr = doc.createTextNode(stderr or "*~")
sysinp.append(txtinp)
sysout.append(txtout)
sysrtn.append(txtrtn)
syserr.append(txterr)
doc.body.append(sysinp)
doc.body.append(sysout)
doc.body.append(syserr)
doc.body.append(sysrtn)
