# to open/create a new html file in the write mode
f = open('Mutation Testing.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>C++ Mutation Testing</h2>

<p>Read Me File:</p>
<p>Mutation Test: <a href="diff.html">Results</a></p>
<p>Mutants Used:<a href="Mutants Used.html">Mutants</a></p>
<p>Gcovr:</p>
</body>
</html>
"""
#writing the code into the file
f.write(html_template)

# close the file
f.close()

f = open('Mutants Used.html', 'w')
html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Mutants Used:</h2>
<p>Key: </p>
<p> 0 : Mutant was not used </p>
<p> 1 : Mutant was used </p>
<div><p><object data="../../gtest-demo/mutator/config.ini"></object></p></div>
<p></p>
<a href="Mutation Testing.html">Back</a></p>
<script src="config.ini"></script>
</body>
</html>
"""
f.write(html_template)
f.close()
