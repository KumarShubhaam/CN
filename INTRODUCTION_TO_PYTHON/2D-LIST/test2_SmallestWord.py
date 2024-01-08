def minlen(s):
    li = s.split()
    min = len(s)
    for ele in li:
        l = len(ele)
        if l < min:
            min = l
        
    print(min)



s = input()
minlen(s)