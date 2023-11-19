with open('text.txt','r+') as f:
    f.seek(0,0)
    print(f.read())
    f.seek(0,0)
    f.write('python')
    f.seek(0,2)
    f.write('python')
    f.close()