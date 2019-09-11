from browser import document as doc, alert
stdinp = doc.getElementById("CODE").innerHTML
stdinp = '\n'.join('   '+line for line in stdinp.splitlines())
global stdout
stdrtn, stderr, stdout = "", "", ""
sysout = doc.createElement("DIV")
syserr = doc.createElement("DIV")
sysrtn = doc.createElement("DIV")
sysout.style.color = "#00ffffff"
sysrtn.style.color = "#00ff00ff"
syserr.style.color = "#ff0000ff"
old_print = print
def print(*args, sep=' ', end='\n'):
    doc.write('w')
    for arg in args:
        stdout += f'{arg}{sep}'
    stdout+=str(end)
    doc.write(stdout)
tmp = {}
exec('def fn():\n'+stdinp, tmp)
try: 
    stdrtn = tmp['fn']()
except Exception as ex: 
    stderr = str(ex)
txtrtn = doc.createTextNode((str(type(stdrtn)).split("'")[1])+" ] "+str(stdrtn))
txterr = doc.createTextNode(stderr or "~")
sysrtn.append(txtrtn)
syserr.append(txterr)
doc.body.append(syserr)
doc.body.append(sysrtn)
