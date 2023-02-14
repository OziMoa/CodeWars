"""Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime""""


def divisors(integer):
    divlist=[]
    for i in range(2, integer+1):
        if integer % i == 0:
            divlist.append(i)
        else: 
            continue 
    if len(divlist)==1:
        return f"{divlist[0]} is prime"
    else: 
        return divlist[:-1]
        
    pass
