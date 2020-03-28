#記帳軟體
#讀取檔案 #就是先讀取檔案後，把讀取的內容先裝進清單
#後續輸入新的內容，才不會全部洗掉，這就是讀取的作用
products = [] #將product抓上來當清單
with open('記帳本.csv', 'r') as f: #不同作業系統會有編碼問題，建議還是要加入編碼utf-8，可是如果是中文作業系統加入這個可能會出現錯誤代碼
    for line in f:
        date, name, price  = line.strip().split(',')
        #記得要先用strip將\n或空格去掉，不然csv會出現在\n在裡面，
        #然後再用split切割檔案，並利用逗號做為區隔，這個會有一個順序(由左而右)
        #先在新增功能，與下面一樣，不要重複寫入，而是將data,name,price三個已知名稱分別寫入，也是一個簡寫法
print(s)

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

with open('記帳本.csv', 'w', encoding='utf-8') as f: #有時候會出現亂碼，所以要告訴他，我要使用什麼編碼，大部分建議使用utf-8，它是世界共通的編碼
    f.write('日期,商品名稱,價格\n') #要寫入每一行的index索引，只要在迴圈前將標題名稱寫入即可，這樣他就不會一直重複，也能在最上面
    for p in products:
        f.write(p[0] + ',' + p[1] + ',' + str(p[2]) + '\n') #使用CSV檔案，必須用逗號分隔，才會分開存取
                                                       #由於把價格轉為數值，但是+號的合併只能是字串
                                                       #所以又要把p[1]轉換為字串才能合併
