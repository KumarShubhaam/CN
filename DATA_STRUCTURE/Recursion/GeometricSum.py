def geometricSum(k):
    if 1/(2**k) == 1:
        return 1
    s = geometricSum(k-1)
    s = s + 1/(2**k)
    return s

n = int(input())
print("{:.5f}".format(geometricSum(n)))