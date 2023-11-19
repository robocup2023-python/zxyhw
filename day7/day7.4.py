with open('text.txt','r')as f1:
    with open('copy_text.txt','r')as f2:
        l1,l2=f1.readline(),f2.readline()
        line=0
        while(l1 or l2):
            line+=1
            if l1!=l2:
                print(line)
            l1,l2=f1.readline(),f2.readline()