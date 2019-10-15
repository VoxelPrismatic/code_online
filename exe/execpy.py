from browser import document as doc, alert
stdinp = doc.getElementById("SYSINP").innerHTML
stdinp = 'def fn():\n    '+stdinp.replace('\n','\n    ')
stdrtn, stderr, stdout = "", "", ""
old_print = print
def print(*args, sep=' ', end='\n'):
    global stdout
    for arg in args:
        stdout += str(arg) + sep
    stdout += end
tmp = {'__builtins__':__builtins__}
tmp['print'] = print
try: 
    exec(stdinp, tmp)
    stdrtn = tmp['fn']()
except Exception as ex: 
    stderr = str(ex)
doc.getElementById("SYSINP").innerHTML = (stdinp or ";")
doc.getElementById("SYSOUT").innerHTML = (stdout or "~").replace('>', '&gt;').replace('<', '&lt;')
doc.getElementById("SYSERR").innerHTML = (stderr or "~").replace('>', '&gt;').replace('<', '&lt;')
doc.getElementById("SYSRTN").innerHTML = f'{str(type(stdrtn))[8:-2]} ] {stdrtn}'.replace('>', '&gt;').replace('<', '&lt;')
