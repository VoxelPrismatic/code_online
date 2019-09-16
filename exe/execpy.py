from browser import document as doc, alert
stdinp = (doc.getElementById("SYSINP").innerHTML or "return None")
stdinp = 'def fn():\n    '+stdinp.replace('\n','\n\t')
stdrtn, stderr, stdout = "", "", ""
old_print = print
def print(*args, sep=' ', end='\n'):
    global stdout
    stdout += sep.join(args) + end
tmp = {'__builtins__':__builtins__}
tmp['print'] = print
try: 
    exec(stdinp, tmp)
    stdrtn = tmp['fn']()
except Exception as ex: 
    stderr = str(ex)
stdout = (stdout or "~")
stderr = (stderr or "~")
stdrtn = (stdrtn or None)
doc.getElementById("SYSINP").innerHTML = stdinp
doc.getElementById("SYSOUT").innerHTML = stdout
doc.getElementById("SYSERR").innerHTML = stderr
doc.getElementById("SYSRTN").innerHTML = f'{str(type(stdrtn))[8:-2]} ] {stdrtn}'
