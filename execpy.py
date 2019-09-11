#from urllib.parse import unquote
from traceback import format_exc as fex
from browser import document as doc, alert
url = str(doc.URL)
code = ""
tokens = url.split("?.")
for token in tokens:
    if token.startswith('code='):
        code = token[5:]
skipA = False
skipB = False
stdinp = ""
for x in range(len(code)):
    if skipA: continue
    elif skipB: continue
    elif '%' in code[x:x+3]:
        skipA, skipB = True, True
        stdinp += eval(f'"\\u00{code[x+1:x+2]}"')
    else:
        stdinp += code[x]
if not stdinp: stdinp = "pass"
stdinp = '\n'.join('   '+line for line in stdinp.splitlines())
stdrtn, stderr, stdout = "", "", ""
sysinp = doc.createElement("DIV")
sysout = doc.createElement("DIV")
syserr = doc.createElement("DIV")
sysrtn = doc.createElement("DIV")
sysinp.style.color = "#ff00ffff"
sysout.style.color = "#00ffffff"
sysrtn.style.color = "#00ff00ff"
syserr.style.color = "#ff0000ff"
old_print = print
def print(*args, sep=' ', end='\n'):
    global stdout
    for arg in args:
        stdout += f'{arg}{sep}'
    stdout+=str(end)
tmp = {}
exec('def fn():\n'+stdinp, tmp)
try: 
    stdrtn = tmp['fn']()
except Exception as exc: 
    stderr = str(exc)+'<br />'+str(fex()).replace('\n', '<br />\u200b').replace(' ','\u200b \u200b')
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
