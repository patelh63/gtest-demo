# to open/create a new html file in the write mode
f = open('Mutation Testing.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>C++ Mutation Testing</h2>

<p>Read Me File:<a href="../../PorcupinesMutator/README.md">README</a></p>
<p>Mutation Test: <a href="diff.html">Results</a></p>
<p>Mutants Used:<a href="../../PorcupinesMutator/config.ini">Mutants</a></p>
<p>Gcovr:</p>
</body>
</html>
"""
#writing the code into the file
f.write(html_template)

# close the file
f.close()
