if __name__ == '__main__':
    s = input()
    li = list(s)
    print(li)
    for i in range(5):
        for w in li:
            if w.isalnum():
                print(True)
                break
        else:
            print(False)

        for w in li:        
            if w.isalpha():
                print(True)
                break
        else:
            print(False)

        for w in li:        
            if w.isdigit():
                print(True)
                break
        else:
            print(False)

        for w in li:        
            if w.islower():
                print(True)
                break
        else:
            print(False)

        for w in li:        
            if w.isupper():
                print(True)
                break
        else:
            print(False)

                
            
                
        
        
