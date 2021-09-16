def subtractProductAndSum(n):
    strN = list(str(n))

    product = 1
    sum = 0
    for i in strN:
        product = product * int(i)
        sum = sum + int(i)

    result = product - sum
    print(result)


subtractProductAndSum(234)
