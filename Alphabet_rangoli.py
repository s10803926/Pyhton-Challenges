def print_rangoli(size):
    entry=1
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',\
            'u','v','w','x','y','z']
    constant=size+(size-1)+2*(size-1)
    for i in range (0,((2*size))):
        str1=''
        str2=''
        if i < size:
            for j in range(0,entry):
                str1+='-'+letters[size-j-1]
            str1+=str1[::-1][1:]
            spaces2add=(constant-(len(str1)))/2
            if i==size-1:
                str1=str1[1:-1]
            for o in range(spaces2add):
                str1='-'+str1+'-'
            entry+=1
            print str1
        elif i==size:
            entry-=1
        else:
            entry-=1
            for k in range(0,entry):
                str2+='-'+letters[size-k-1]
            str2+=str2[::-1][1:]
            spaces2add=(constant-(len(str2)))/2
            if i==0:
                str2=str2[1:-1]
            for o in range(spaces2add):
                str2='-'+str2+'-'
            print str2
        
 if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
    
# takes a input from user 
# number of points to draw the rangoli
