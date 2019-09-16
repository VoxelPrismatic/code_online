from browser import document as doc, alert
stdinp = (doc.getElementById("SYSINP").innerHTML or "A")
args = []
gate = []
for x in stdinp:
    if x == ' ':
        continue
    if x == '!':
        args.append('not')
    elif x == '+':
        args.append('or')
    elif x == '?':
        args.append('!=')
    else:
        args.append(x)
        gate.append(False)
eq = ' '.join(args)
doc.getElementById("SYSINP").innerHTML = stdinp
doc.getElementById("SYSOUT").innerHTML = eq
doc.getElementById("SYSERR").innerHTML = "SYNTAX: A!BC+D?E - (A AND NOT B AND C) OR (D XOR E)"
doc.getElementById("SYSRTN").innerHTML = f''
