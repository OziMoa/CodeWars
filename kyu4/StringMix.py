""" DESCRIPTION:
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh" """

def mix(s1, s2):
    # your code
    # splitting
    ls1 = []
    ls2 = []
    numel1 = {}
    numel2 = {}
    for i in s1:
        ls1.append(i)
    for j in s2:
        ls2.append(j)

    for i in ls1:
        if i.isalpha():
            if not i.isupper():
                numel1[i] = ls1.count(i)

    for j in ls2:
        if j.isalpha():
            if not j.isupper():
                numel2[j] = ls2.count(j)
    exlist=[]
    for it in numel1:
        if numel1[it] <= 1:
            exlist.append(it)
    for i in exlist:
        numel1.pop(i)
    exlist = []
    for it in numel2:
        if numel2[it] <= 1:
            exlist.append(it)
    for i in exlist:
        numel2.pop(i)
    finlist = []
    numnum=0
    ind=0
    for o in sorted(numel1):
        if o in sorted(numel2):
            if numel1[o] < numel2[o]:
                if numel2[o]>numnum:
                    finlist.insert(ind,f'2:{numel2[o]*o}')
            elif numel1[o] == numel2[o]:
                finlist.append(f'=:{numel1[o]*o}')
            else:
                finlist.append(f'1:{numel1[o]*o}')
        else:
            finlist.append(f'1:{numel1[o]*o}')
    for o in sorted(numel2):
        if o not in numel1:
            finlist.append(f'2:{numel2[o] * o}')

    def custom_key(elems):
        return -len(elems), elems.lower()

    finlist= sorted(finlist, key=custom_key)

    return '/'.join(finlist)


print(mix("Are they here", "yes, they are here"))
