def numberOfPar(previous,d,mode):
    if(mode == "("):
        if(previous > d):
            return 0
        else:
            return (d-previous)
    elif(mode == ")"):
        if(previous > d):
            return previous - d
        else:
            return 0
            
for t in range(int(input())):
    s = input()
    newS = ''
    previous = 0
    for d in s:
        d = int(d)
        newS+= ")"*numberOfPar(previous,d,")")+"(" * numberOfPar(previous, d, "(")+str(d) 
        previous = d
    newS+=")"*d
    print('Case #{}:'.format(t+1),newS)