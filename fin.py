from browser import document
for x in ['SYSLNG','SYSINP','SYSOUT','SYSERR','SYSRTN']:
    itm = document.getElementById(x)
    rep = {'\n':'<br>',
           '\t': '    ',
           ' ': '\x0b \x0b'}
    for r in rep:
        itm.innerHTML = itm.innerHTML.replace(r, rep[r])
document.body.style.backgroundColor = "#112222ff"
document.body.style.color = "#ffffffff"
document.body.style.fontFamily = "Ubuntu Mono"
document.getElementById('SYSDON').innerHTML = "[COMPLETE]"
