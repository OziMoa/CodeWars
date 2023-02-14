"""DESCRIPTION:
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
"""


from itertools import permutations
def next_bigger(n):
    strr = str(n)
    list = [int(i) for i in strr]
    if len(list) == 1:
        return -1
    elif len(strr) == 2:
            if strr < strr[::-1]:
                return int(strr[::-1])
            else:
                return -1
    elif list == [list[0]]*len(list):
        return -1
    elif list == sorted(list, reverse=True):
        return -1
    else:
        for ord in range(1, len(strr)+1):
            front = ''.join(strr[:-ord])
            end = sorted([''.join(i) for i in permutations(strr[-ord:], ord)])
            for j in end:
                newnum = ''.join(front)+''.join(j)
                if int(newnum) > n :
                    return int(newnum)
