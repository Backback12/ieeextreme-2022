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

#Number of Test Cases
t = get_number()

#Test Case Loop
for _ in range(t):

    dict = {}
    events = int(input())

    for _ in range(events):

        line = input().split(" ")
        payee = line[0]
        paid = int(line[1])
        payer = line[2]

        if payee not in dict:
            dict[payee] = 0
            
        
        dict[payee] -= paid

     

    for i in range(paid):
        if line[2+i] not in dict:

            dict[line[2+i]] = 0
        
        dict[line[2+i]] += 1
    
    dinnersNeeded = 0
    daysNeeded = 0

    for key in dict.keys():

        if (dict[key] > 0):
            dinnersNeeded += dict[key]

        if (dict[key] < daysNeeded):
            daysNeeded = dict[key]

    print(str(dinnersNeeded) + " " + str(abs(daysNeeded)))

    #Number of Meals

    
    

    

