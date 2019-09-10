(function(){
                    oldLog = console.log;
                    console.log = function(...args){ 
                        for (arg of args) { stdout += arg+""; }
                        stdout += "\n";
                    };})();
                try { 
                    stdrtn = eval("(function(){"+stdinp+";})();"); 
                } catch(ex) { 
                    stderr = ex.message; 
                }
                var txtinp = document.createTextNode(stdinp || "'?.code=' tag not found;");
                var txtout = document.createTextNode(stdout.replace('\n', '<br >') || "*~");
                var txtrtn = document.createTextNode((typeof stdrtn)+" ] "+stdrtn);
                var txterr = document.createTextNode(stderr || "*~");
                sysinp.appendChild(txtinp);
                sysout.appendChild(txtout);
                sysrtn.appendChild(txtrtn);
                syserr.appendChild(txterr);
                document.body.appendChild(sysinp);
                document.body.appendChild(sysout);
                document.body.appendChild(syserr);
                document.body.appendChild(sysrtn);
