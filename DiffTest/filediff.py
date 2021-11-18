import difflib as dl

with open('example.cpp') as f:
    original_file = f.read()

with open('example_ArithmeticPlusToMinus.cpp') as f:
    mutated_file = f.read()

diffs = dl.HtmlDiff().make_file(original_file, mutated_file, fromdesc='Source', todesc='ArithmeticPlusToMinus', context=True, numlines=1)

with open('diff.html',"w+") as diff_file:
    diff_file.write(diffs)

