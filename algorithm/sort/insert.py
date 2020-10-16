def insert_sort(num_list):
    """
    :param num_list: a list want to sort
    """
    num_list_length = len(num_list)
    for i in range(1, num_list_length):
        insert_value = num_list[i]
        j = i - 1
        while j >= 0:
            if num_list[j] > insert_value:
                num_list[j + 1] = num_list[j]
                num_list[j] = insert_value
            j -= 1

    return num_list


if __name__ == '__main__':
    num_list = [20, 9, 100, 0, 55, 3, 11]
    print('插入排序前：{}'.format(num_list))
    print('插入排序後：{}'.format(insert_sort(num_list)))
