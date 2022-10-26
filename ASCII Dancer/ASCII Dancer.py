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


# list of commands

# [left/right] 
#   hand to head
#   hand to hip
#   hand to start
#   leg in
#   leg out
# turn      - swaps forward and backward

# say [words]


def printGuy(guy):
    for col in guy:
        st = ""
        for item in col:
            st += item
        print(st)
        

flip = {"(": ")",
        ")": "(",
        "\\": "/",
        "/": "\\",
        ">": "<",
        "<": ">",
        " ": " ",
        "o": "o",
        "|": "|",
}

testCases = get_number()
for tc in range(testCases):
    guy =  [[" ", "o", " "],
            ["/", "|", "\\"],
            ["/", " ", "\\"]]
    cmdList = []
    cmdCount = get_number()
    
    isFlipped = True
    
    
    for cm in range(cmdCount):
        cmdList.append(input())
        
    
    for command in cmdList:
        # read command
        # change guy
        if 'say' in command:
            
            print(command[4:])
            
        elif 'turn' in command:
            
            isFlipped = not isFlipped
            
            guy[0][0], guy[0][2] = flip[guy[0][2]], flip[guy[0][0]]
            guy[1][0], guy[1][2] = flip[guy[1][2]], flip[guy[1][0]]
            guy[2][0], guy[2][2] = flip[guy[2][2]], flip[guy[2][0]]
            
            printGuy(guy)
            
        else:
            # movement
            if 'leg' in command:
                
                if 'in' in command:
                    if ('left' in command) ^ isFlipped:
                        guy[2][0] = "<"
                    elif ('right' in command) ^ isFlipped:
                        guy[2][2] = ">"
                elif 'out' in command:
                    if ('left' in command) ^ isFlipped:
                        guy[2][0] = "/"
                    elif ('right' in command) ^ isFlipped:
                        guy[2][2] = "\\"
                        
            elif 'hand' in command:
                
                if 'head' in command:
                    if ('left' in command) ^ isFlipped:
                        guy[0][0] = "("
                        guy[1][0] = " "
                    elif ('right' in command) ^ isFlipped:
                        guy[0][2] = ")"
                        guy[1][2] = " "
                        
                elif 'hip' in command:
                    if ('left' in command) ^ isFlipped:
                        guy[0][0] = " "
                        guy[1][0] = "<"
                    elif ('right' in command) ^ isFlipped:
                        guy[0][2] = " "
                        guy[1][2] = ">"
                
                elif 'start' in command:
                    if ('left' in command) ^ isFlipped:
                        guy[0][0] = " "
                        guy[1][0] = "/"
                    elif ('right' in command) ^ isFlipped:
                        guy[0][2] = " "
                        guy[1][2] = "\\"
                
            printGuy(guy)
            # print guy
        
        
        
        

    

# res = a + b
# print(res)