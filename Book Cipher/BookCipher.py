# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy
import math

phraseCount = get_number()
xmlCount = get_number()
row, col = get_word().split(",")
row, col = int(row), int(col)

lex = get_word()

cypherGrid = ""

phrases = []
for _ in range(phraseCount):
    phrases.append(input().strip())  # read phrase input


lines = ""
for _ in range(xmlCount):
   line = input().strip()
   if '<p>' in line:
        line = line.replace('<p>', '').replace('</p>', '')
        lines += line
       
cypherGrid = lines.ljust(row*col, "你")
cypherGrid = cypherGrid[0:row*col]



if 'lex' == 'S':
    for phrase in phrases:
        output = ""
        
        for letter in phrase:
            pos = 0
            
            while letter != cypherGrid[pos] or pos >= len(cypherGrid):
                pos += 1
                if (letter == cypherGrid[pos]):
                    output += str(math.floor(pos/col)) + "," + str(pos%col) + ","
                    
            if pos >= len(cypherGrid):
                # not found in cypherGrid
                output = "0"
                break
        
        if output != "0":
            output = output[:-1]
            
        print(output)
    
    
