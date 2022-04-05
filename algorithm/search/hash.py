nums = [78, 33, 6, 11, 2, 44, 35, 27, 80]
# nums = [11]
hash_table = [None] * 10


def takeRemainder(num):
    n = num % 10
    return n


def add(nums):
    for i in range(len(nums)):
        index = takeRemainder(nums[i])
        hash_table[index] = nums[i]
    # print(hash_table)


def search(data):

    index = takeRemainder(data)
    if hash_table[index] == data:
        print(hash_table[index])
    else:
        print("Value No exist.")


add(nums)
search(78)
