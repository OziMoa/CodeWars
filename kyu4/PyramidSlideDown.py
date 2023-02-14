"""DESCRIPTION:
Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function that takes a pyramid representation as an argument and returns its largest 'slide down'. For example:

* With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
* Your function should return `23`.
By the way...
My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.
"""

def longest_slide_down(pyramid):
    # TODO: write some code...
    pyramid[0][0] = [pyramid[0][0]]
    
    for i in range(1, len(pyramid)):
        for j in range(len(pyramid[i])):
            
            if j == 0:
                last_list = pyramid[i-1][j]
                
            elif j == len(pyramid[i])-1:
                last_list = pyramid[i-1][j-1]
                
            else:
                last_list = pyramid[i-1][j]+pyramid[i-1][j-1]
                
            new_list = []
            last = max(last_list)
            new_list.append(last + pyramid[i][j])
            pyramid[i][j] = new_list
    
    total = []
    
    for i in pyramid:
        for j in i:
            for k in j:
                total.append(k)

    return max(total)
