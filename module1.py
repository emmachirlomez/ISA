def main(variable):
    a = 0  #R1
    b = 10 #R2
    c = 1  #R3
    d = 9  #R4              #'abcdefghijklmnopqrstuvwxyz'
    f = 6  #R6
    g = 13 #R7
#both JEQ and JR produce the next line
    while d != 0:
        e = variable[a] #R5
        variable[b] = e 
        d = d - c   
        a = a + c
        b = b + c
#JEQ produces the next
    g = 20 #R7
    h = 17 #R8
    i = 20 #R9
    j = 26 #R10 
    while d == 0:
        a = 10 #R1
        b = 11 #R2
        d = 1  #R3
        while b >= g :
            e = variable[a]   #R5
            f = varriable[b]  #R6   
            if e >= f:    #if reg_1 > current_counter then use if, else use while in position reg_1
                variable[a] = f
                variable[b] = e
                d = 0               
            a = a + c
            b = b + c
    return variable