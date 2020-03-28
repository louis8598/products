#記帳軟體
products = []
while True:
    date = input('請輸入今天日期：')
    if name == 'q':
        break
    name = input('請輸入商品名稱：')
    price = input('請輸入商品價格：')
    products.append([date, name, price]) #直接在大清單中創作小清單，讓程式碼更少
print(products)