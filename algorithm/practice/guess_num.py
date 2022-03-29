class Gross_num:

    # 私有屬性
    __answer = 0

    # :param int min
    # :param int max
    # :return string
    def gross_num(self, min, max):
        answer = 30
        x = input("請輸入你要猜的數字: ")
        try:
            num = self.check_num(x)
        except ValueError:
            print("請輸入數字!")
        else:
            result = self.right(num, answer)

            if result == 1:
                print("num is right.")
            else:
                print("num is wrong.")
                print("猜錯囉，在猜一次.")
                self.angin(num, min, max, answer)

    # :param int x
    # :return int num
    def check_num(self, x):
        num = int(x)

        return num

    # :param int num
    # :param int answer
    # :return int
    def right(self, num, answer):
        if(num == answer):
            return 1

    def angin(self, num, min, max, answer):
        if(num > answer):
            max = num
        else:
            min = num

        print("現在的最小數字:", min)
        print("現在的最大數字:", max)
        print("------------------------")
        self.gross_num(min, max)


g = Gross_num()
g.gross_num(1, 99)
