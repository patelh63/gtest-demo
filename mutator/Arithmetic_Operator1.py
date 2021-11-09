import re
import readline
#mutate * to /

#Where file.txt is the file you want to mutate
file = open('AO1.cpp', 'a+')

#Where file1.txt is a copy of the file thats being mutated
with open('AO1.cpp', 'r') as input:
    with open('AO1_ArithmeticOperator.cpp', 'w') as output:
        for line in input:
            output.write(re.sub('[*]([^/*%+-])', '/', line))
            file.close()
#a;slkdjf;alskjdf;alskjdf;laskjf