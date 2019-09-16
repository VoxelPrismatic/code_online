from browser import document as doc, alert
stdinp = (doc.getElementById("SYSINP").innerHTML or "A")+" "
doc.getElementById("SYSINP").innerHTML = stdinp
args = []
gate = []
lttr = []
for x in range(len(stdinp)-1):
    if stdinp[x] == ' ':
        continue
    if stdinp[x] == '!':
        args.extend(['and','not'])
    elif stdinp[x] == '+':
        args.append('or')
    elif stdinp[x] == '~':
        args.extend(['or','not'])
    elif stdinp[x] == '?':
        args.append('!=')
    else:
        args.append(stdinp[x])
        if stdinp[x+1].lower() in 'abcdefghijklmnopqrstuvwxyz':
            args.append('and')
        gate.append('0')
        lttr.append(stdinp[x])
eq = ' '.join(args)
rep = {' or ': '] OR [',
       'and': 'AND',
       '!=': 'XOR',
       'not':'NOT'}
eq2 = eq
for re in rep:
    eq2 = eq.replace(re,rep[re])
doc.getElementById("SYSRTN").innerHTML = f'[{eq2}]'
def next(gate):
    return list(f'{int("".join(gate),2)+1:b}'.zfill(len(gate)))
def calc(gate):
    st = ""
    eq1 = eq
    for y in range(len(lttr)):
        eq1 = eq1.replace(lttr[y],gate[y])
        st += gate[y] + " "
    st += f"-{int(eval(eq1))}-"
    return st
stdout = ' '.join(lttr) + ' OUT'
stdout += '<br>'+'-'*len(stdout)
while any(g == '0' for g in gate):
    stdout += '<br>'+calc(gate)
    gate = next(gate)
eq1 = eq
stdout += '<br>'+calc(gate)
doc.getElementById("SYSOUT").innerHTML = stdout
doc.getElementById("SYSERR").innerHTML = "SYNTAX: A!BC+D?E~F - [A AND NOT B AND C] OR [D XOR E] OR [NOT F]"