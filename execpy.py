from browser import document as doc, alert
stdinp = doc.getElementById("SYSINP").innerHTML or "return None"
stdinp = '\n'.join('   '+line for line in stdinp.splitlines())
stdrtn, stderr, stdout = "", "", ""
old_print = print
def print(*args, sep=' ', end='\n'):
    global stdout
    for arg in args:
        stdout += f'{arg}{sep}'
    stdout+=str(end)
tmp = {'__builtins__':__builtins__}
tmp['print'] = print
exec('def fn():\n'+stdinp, tmp)
try: 
    stdrtn = tmp['fn']()
except Exception as ex: 
    stderr = str(ex)
sysout = (sysout or "~")
syserr = (syserr or "~")
sysRTN = (sysout or "~")
doc.getElementById("SYSINP") = sysinp.replace('\n','<br>').replace(' ','\u200b')
doc.getElementById("SYSOUT") = sysout.replace('\n','<br>').replace(' ','\u200b')
doc.getElementById("SYSERR") = syserr.replace('\n','<br>').replace(' ','\u200b')
doc.getElementById("SYSRTN") = sysinp.replace('\n','<br>').replace(' ','\u200b')
