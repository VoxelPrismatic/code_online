from browser import document
for x in ['SYSLNG','SYSINP','SYSOUT','SYSERR','SYSRTN']:
    itm = document.getElementById(x)
    itm.innerHTML = itm.innerHTML.replace('\n','<br>').replace(' ','\u200b \u200b')
document.body.style.backgroundColor = "#112222ff"
document.body.style.color = "#ffffffff"
document.body.style.fontFamily = "Ubuntu Mono"
