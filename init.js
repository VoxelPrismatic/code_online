var url = decodeURIComponent(document.URL+"")+"";
var tokens = url.split("?.");
var lang = "";
var stdinp = "";
for (token of tokens) {
  if (token.search("lang=")==0) {
    lang += token.slice(5)+"".toLowerCase();
  } else if (token.search("code=")==0) {
    stdinp += token.slice(5)+"";
  }
}
var javakw = ["java"];
var cppkw = ["cpp", "c++"];
var pykw = ["py", "python"];
var jskw = ["js", "javascript"];
var rbkw = ["rb", "ruby"];
var swiftkw = ["swift", "sft", "sw"];
var truthkw = ['tr', 'truth'];
document.getElementById('SYSINP').innerHTML = eval(`"${sysinp}"`);
