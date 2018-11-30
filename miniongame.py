import itertools

def occurences(sub, string):
    count=start=0
    
    while True:
        start=string.find(sub,start)+1
        if start > 0:
            count +=1
        else:
            return count



def minion_game(string):
    # your code goes here
    vow=['A','E','I','O','U']
    vowstring=[]
    consstring=[]
    kevin = ''
    kscore=0
    sscore=0
    stuart = ''
    for i in string:
        if i in vow:
            vowstring.append(i)
        else:
            consstring.append(i)
    
    vowstring = set(vowstring)
    consstring = set(consstring)

    
    for j in vowstring:
        kevin=j
        # print kevin
        if kevin in string:
            kscore+=string.count(kevin)
            kpos=string.find(kevin)
            for st in range(kpos+1,len(string)):
                kevin+=string[st]
                if kevin in string:
                    kscore+=occurences(kevin, string)

    for k in consstring:
        stuart=k
        # print kevin
        if stuart in string:
            sscore+=string.count(stuart)
            spos=string.find(stuart)
            for st in range(spos+1,len(string)):
                stuart+=string[st]
                if stuart in string:
                    sscore+=occurences(stuart, string)  
    if sscore<kscore:
        print "Kevin",kscore
    else:
        print "Stuart",sscore
    


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
