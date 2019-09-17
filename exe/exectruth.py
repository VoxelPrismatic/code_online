from browser import document as doc, alert
stdinp = (doc.getElementById("SYSINP").innerHTML or "A")+" "
doc.getElementById("SYSINP").innerHTML = stdinp
args = []
gate = []
lttr = []
rep = {'&': 'and',
       '+': 'or',
       '~': 'or not',
       '*': '==',
       '?': '!=',
       '$': 'and not',
       '[': '(',
       ']': ')',
       '(': '(',
       ')': ')',
       ':': '(',
       ';': ')'}
for x in range(len(stdinp)-1):
    if stdinp[x] == ' ':
        continue
    if stdinp[x] == '!':
        if len(args) and args[-1].lower() in 'abcdefghijklmnopqrstuvwxyz':
            args.append('and')
        args.append('not')
    elif stdinp[x] == '~':
        args.insert(-1, '?n')
        args.append('or not')
    elif stdinp[x] == '$':
        args.insert(-1, '?n')
        args.append('and not')
    elif stdinp[x] in list(rep):
        args.append(rep[stdinp[x]])
    else:
        args.append(stdinp[x])
        if stdinp[x+1].lower() in 'abcdefghijklmnopqrstuvwxyz':
            args.append('and')
        if stdinp[x].upper() not in lttr:
            gate.append('0')
            lttr.append(stdinp[x].upper())
eq = ' '.join(args).replace('?n ?n','not').replace('?n','not') #Prevents 'not not' when smth like A~B~C
rep = {' or ': '] OR [',
       'and': 'AND',
       ' != ': '-XOR-',
       'not ':'NOT-',
       ' == ': '-XNOR-',
       '(': '[',
       ')': ']'}
eq2 = eq 
for re in rep:
    eq2 = eq2.replace(re,rep[re])
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
stdout += '\n'+'-'*len(stdout)
while any(g == '0' for g in gate):
    stdout += '\n'+calc(gate)
    gate = next(gate)
eq1 = eq
stdout += '\n'+calc(gate)
doc.getElementById("SYSOUT").innerHTML = stdout
doc.getElementById("SYSERR").innerHTML = """\
A&B ---- A AND B
AB ----- A AND B
A+B ---- A OR B
A?B ---- A XOR B
A*B ---- A XNOR B
A$B ---- NOT A AND NOT B
A~B ---- NOT A OR NOT B
A[B+C] - A AND [B OR C]
A(B+C) - A AND [B OR C]
A:B+C; - A AND [B OR C]
"""
