# def subtractProductAndSum(n):
#     strN = list(str(n))

#     product = 1
#     sum = 0
#     for i in strN:
#         product = product * int(i)
#         sum = sum + int(i)

#     result = product - sum
#     print(result)

# eval 執行字串的表達式，並返回表達式的值
# 我想應該是可以做字串類型的加減乘除??
# join的意思是將數字拆掉後配上運算符號
def subtractProductAndSum(n):
    return eval('*'.join(str(n))) - eval('+'.join(str(n)))


# print(subtractProductAndSum(234))

print(eval('3*3'))
