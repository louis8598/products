#記帳軟體
products = []
while True:
    date = input('請輸入日期：')
    if date == 'q':
        break
    name = input('請輸入商品名稱：')
    price = input('請輸入商品價格：')
    price = int(price) #轉換為數值
    products.append([date, name, price]) #直接在大清單中創作小清單，讓程式碼更少
print(products)

for p in products: #列出細項
    print('這項商品是在', p[0],'買的，商品名稱是', p[1], '商品價格為', p[2],'元。') #利用p[0]列出清單中的第一項目達成目的，後面以此列推。

with open('記帳本.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + ',' + str(p[2]) + '\n') #使用CSV檔案，必須用逗號分隔，才會分開存取
                                                       #由於把價格轉為數值，但是+號的合併只能是字串
                                                       #所以又要把p[1]轉換為字串才能合併
