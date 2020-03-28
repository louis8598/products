#記帳軟體
products = []
while True:
    date = input('請輸入今天日期：')
    if name == 'q':
        break
    name = input('請輸入商品名稱：')
    price = input('請輸入商品價格：')
    acc = []
    acc = [date, name, price] #清單中裝著date name price三樣東西，這樣就不用寫acc.append(),這是簡潔寫法
    products.append(acc)
print(products)