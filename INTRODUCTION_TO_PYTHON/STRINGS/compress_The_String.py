from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(string) :
	# Write your code here.
    pass
    c = ''
    i = 0
    while i in range(len(string)):
        char = string[i]
        count = 0
        while string[i] == char:
            count = count + 1
            i = i + 1
            if i == len(string):
                break
        if count > 1:
            c = c + string[i-1] + str(count)
        else:
            c = c + string[i - 1]
    return c

	


















# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)