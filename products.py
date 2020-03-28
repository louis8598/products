#記帳軟體
products = []
while True:
    date = input('請輸入今天日期：')
    if name == 'q':
        break
    name = input('請輸入商品名稱：')
    price = input('請輸入商品價格：')
    acc = []
    acc.append(date)
    acc.append(name)
    acc.append(price)
    products.append(acc)
print(products)