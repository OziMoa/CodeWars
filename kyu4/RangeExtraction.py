"""DESCRIPTION:
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""


def solution(args):
    # your code here
    smollist = []
    start = end = args[0]
    
    for i in args[1:] + [""]:
        if i != end + 1: 
            if start == end:
                smollist.append ( str(start) )
            elif start + 1== end :
                smollist.extend([str(start), str(end)])
            else:
                smollist.append(str(start) + "-" + str(end))
            start = i 
        end = i 

    return ",".join(smollist)
