from browser import document, window
document.getElementById("SYSINP").innerHTML = eval(f'"{document.URL.split("?.")[1][5:].replace("%","\\x")}"')
