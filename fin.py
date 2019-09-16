from browser import document
for x in ['SYSLNG','SYSINP','SYSOUT','SYSERR','SYSRTN']:
    itm = document.getElementById(x)
    itm.innerHTML = itm.innerHTML.replace('\n','<br>').replace(' ','\u200b \u200b')
