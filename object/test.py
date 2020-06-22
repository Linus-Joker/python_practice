class Calculation():

    def rate(self, name, price, dividend):
        rate = format(round((dividend/price) * 100, 2))
        print(name, rate, '%')


cal = Calculation()
price = float(input('請輸入價格:'))
dividend = float(input('請輸入股利:'))
cal.rate('此股的殖利率為', price, dividend)
