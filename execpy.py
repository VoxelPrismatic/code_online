from browser import document as doc, alert
stdinp = (doc.getElementById("SYSINP").innerHTML or "return None")
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
stdout = (stdout or "~")
stderr = (stderr or "~")
stdrtn = (stdrtn or None)
doc.getElementById("SYSINP").innerHTML = stdinp.replace('\n','<br>').replace(' ','\u200b ')
doc.getElementById("SYSOUT").innerHTML = stdout.replace('\n','<br>').replace(' ','\u200b ')
doc.getElementById("SYSERR").innerHTML = stderr.replace('\n','<br>').replace(' ','\u200b ')
doc.getElementById("SYSRTN").innerHTML = f'{str(type(stdrtn))[9:-2]} ] {stdrtn}'.replace('\n','<br>').replace(' ','\u200b ')
