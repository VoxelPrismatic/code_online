from browser import document
for x in ['SYSLNG','SYSINP','SYSOUT','SYSERR','SYSRTN']:
    itm = document.getElementById(x)
    rep = {'\n':'<br>',
           '\t': '    ',
           ' ': ' \u200b',
           '>': '&gt;',
           '<': '&lt;'}
    for r in rep:
        itm.innerHTML = itm.innerHTML.replace(r, rep[r])
document.body.style.backgroundColor = "#112222ff"
document.body.style.color = "#ffffffff"
document.body.style.fontFamily = "Ubuntu Mono"
document.getElementById('SYSLOD').innerHTML = "[COMPLETE]"
