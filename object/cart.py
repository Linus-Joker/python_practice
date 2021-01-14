product1 = {
    'id': 1,
    'book': 'book1',
    'price': 100
}

product2 = {
    'id': 2,
    'book': 'book2',
    'price': 200
}


class Cart():
    qty = 0
    i = {}
    items = []
    totalQty = 0
    totalPrice = 0

    def __init__(self, oldCart):
        if oldCart:
            self.i = oldCart.i
            self.items = oldCart.items
            self.totalQty = oldCart.totalQty
            self.totalPrice = oldCart.totalPrice

    # array   items 商品參數
    # string  qty   商品數量
    # string  id    商品編號

    def add(self, items, qty, id):
        storedItem = {
            'qty': 0,
            'price': items['price'],
            'item': items
        }

        # if self.items:
        #     print('items exist.')
        #     print("啥小清單:", self.items)
        if id in self.i:
            print("key is exist.")
            storedItem = self.i[id]['items']
            storedItem['qty'] += qty
            storedItem['price'] += qty * items['price']
            self.i.update({
                id: {
                    'items': storedItem
                }
            })
            self.items = storedItem
            self.totalQty += qty
            self.totalPrice = storedItem['price']
        else:
            storedItem['qty'] = qty
            storedItem['price'] = qty * items['price']
            self.i.update({
                id: {
                    'items': storedItem
                }
            })
            self.items = storedItem
            self.totalQty += qty
            self.totalPrice += storedItem['price']


book = Cart(None)
book.add(product1, 2, 1)
print("購物車產品清單:", book.items)
print("購物車總數量:", book.totalQty)
print("購物車總價格:", book.totalPrice)
print(book.i)
print("-----------------------------")


product = Cart(book)
product.add(product1, 1, 1)
print("購物車產品清單:", product.items)
print("購物車總數量:", product.totalQty)
print("購物車總價格:", product.totalPrice)
print(product.i)
print("-----------------------------")

p = Cart(product)
p.add(product2, 2, 2)
print("購物車產品清單:", p.items)
print("購物車總數量:", p.totalQty)
print("購物車總價格:", p.totalPrice)
print(p.i)
print("-----------------------------")
