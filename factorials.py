def fact_while(n):
    #4
    total = 1 # 12
    while n > 0:
        total = total * n
        n -= 1

    print(total)

#def fact_while(5):
def fact(n):
    # base case n ==1
    # return n
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


    # 4 * fact(3)