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

import numpy as np
import scipy

T = get_number()
answers = np.zeros(T)

for t in range(T):
    N = get_number()
    answer = 1
    array = np.array([-1]*360, dtype=int)

    for n in range(N):
        D = get_number()
        
        boundedAngle = D % 180
        if boundedAngle not in array:
            array[boundedAngle] = boundedAngle
            if answer == 1:
                answer += 1
            else:
                answer += 2

    answers[t] = answer

for ans in answers:
    print(int(ans))