from browser import document as doc, alert
stdinp = (doc.getElementById("SYSINP").innerHTML or "A")+" "
args = []
gate = []
for x in range(len(stdinp)-1):
    if stdinp[x] == ' ':
        continue
    if stdinp[x] == '!':
        args.append('not')
    elif stdinp[x] == '+':
        args.append('or')
    elif stdinp[x] == '?':
        args.append('!=')
    else:
        args.append(stdinp[x])
        if stdinp[x+1].lower() in 'abcdefghijklmnopqrstuvwxyz':
            args.append('and')
        gate.append('0')
eq = ' '.join(args)
def next(gate):
    return list(f'{int("".join(gate),2)+1:b}')
doc.getElementById("SYSINP").innerHTML = stdinp
doc.getElementById("SYSOUT").innerHTML = eq
doc.getElementById("SYSERR").innerHTML = "SYNTAX: A!BC+D?E - (A AND NOT B AND C) OR (D XOR E)"
doc.getElementById("SYSRTN").innerHTML = "nani"
