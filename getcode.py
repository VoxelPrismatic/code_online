from browser import document
document.getElementById("SYSINP").innerHTML = eval(f'"{document.URL.split("?.")[1][5:].replace("%","\\x")}"')
script = document.createElement("SCRIPT")
script.src = "launch.js"
document.body.appendChild(script)
