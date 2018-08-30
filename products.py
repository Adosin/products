import os # operating system

# 讀取檔案
def read_file(filename): # 投幣口改用 filename 參數
    products = [] 
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 繼續
            name, price = line.strip().split(',')
            products.append([name, price]) 
    return products  # 回傳給 products

# 讓使用者輸入
def user_input(products):  # products 當投幣口
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ') 
		# 1. p = [] # 第1種寫法, 建立 2維 dimension
		# 1. p.append(name)  # 第1種寫法
		# 1. p.append(price) # 第1種寫法
		# 2. p = [name, price]  # 第2種寫法
		# 1. products.append(p)  # 塞入大清單(陣列)
        products.append([name, price])
    print(products)  
    return products # 回傳給 products

# 印出所有購買紀錄
def print_products(products):  # products 當投幣口
    for p in products:
        print(p[0], '的價格是', p[1]) # 單純列印不需要回傳

# 字串的加法 'abc' + '123' = 'abc123' 等於合併
# 字串的乘法 'abc' * 3 = 'abcabcabc' 
# price 轉進來是字串，由於要寫入，不可以轉為整數(數值)
# 寫入只能為 '字串'
# 程式說明 轉整數 price = int(price)
# 程式說明 轉字串 price = str(price)

# 寫入檔案
def write_file(filename, products): # 投幣口 filename 跟 products 
       print('-----------------') 
       with open(filename, 'w', encoding='utf-8') as f: # 當作 f 檔案
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') 

# read_file()  # 可以輸入不同的 filename
# 有 return 就可以把 function 的執行結果存下來

# 以下是主程式
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  # 檢查檔案在不在, 只要檢查一次
        print('Yeah! 找到檔案')
        products = read_file(filename) 
    else:
        print('找不到檔案.....')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)  

main() 
