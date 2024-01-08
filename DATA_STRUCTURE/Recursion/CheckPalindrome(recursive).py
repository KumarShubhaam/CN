def isPalindrome(string: str) -> bool:
    pass
    si = 0
    ei = len(string)-1
    if si == ei or si > ei:
        return True
    output = isPalindrome(string[si+1:ei])
    if output == True:
        if string[si] != string[ei]:
            return False
        else:
            return True
    else:
        return False
    

if isPalindrome("skdpnyegmd"):
    print('true')
else:
    print('false')