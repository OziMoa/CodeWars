"""Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted)."""

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False 
    elif abs(a-b) < c < a+b and abs(a-c) < b < a+c  and abs(b-c) < a < b+c :
        return True
    else: 
        return False
