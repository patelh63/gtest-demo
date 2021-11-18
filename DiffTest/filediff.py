import difflib as dl

with open('example.cpp') as f:
    original_file = f.read()

with open('example_ArithmeticPlusToMinus.cpp') as f:
    mutated_file = f.read()

hd = dl.HtmlDiff()

diffs = hd.make_file(original_file.split("\n"), mutated_file.split("\n"), fromdesc='Source', todesc='Mutant', context=False, numlines=0)

with open('diff.html',"w+") as diff_file:
    diff_file.write(diffs)

