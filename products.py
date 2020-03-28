#記帳軟體
products = []
while True:
    date = input('請輸入今天日期：')
    if date == 'q':
        break
    name = input('請輸入商品名稱：')
    price = input('請輸入商品價格：')
    products.append([date, name, price]) #直接在大清單中創作小清單，讓程式碼更少
print(products)

for p in products: #列出細項
    print('這項商品是在', p[0],'買的，商品名稱是', p[1], '商品價格為', p[2],'元。') #利用p[0]列出清單中的第一項目達成目的，後面以此列推。

with open('記帳本.txt', 'w') as f:
    for p in products:
        f.write(p[0] + ':' + p[1] + ',' + p[2] + '\n')