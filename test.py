def sum_of_digits(n: int) -> int:
    # write your code here
    s = 0
    n = abs(n)
    while ((n*10)//10 != 0):
        s = s + (n%10)
        n = n//10
    return s 

print(sum_of_digits(12345))
print(sum_of_digits(98765))
print(sum_of_digits(10 ** 1000 - 1))
print(sum_of_digits(-12345))
