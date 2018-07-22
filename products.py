products =[] 
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

for p in products:
	print(p) 

for p in products:
	print(p[0], '的價格是', p[1]) 

# 字串的加法 'abc' + '123' = 'abc123' 等於合併
# 字串的乘法 'abc' * 3 = 'abcabcabc' 
# price 轉進來是字串，由於要寫入，不可以轉為整數(數值)
# 寫入只能為 '字串'
# 程式說明 轉整數 price = int(price)
# 程式說明 轉字串 price = str(price)

print('-----------------') 
with open('products.csv', 'w', encoding='utf-8') as f: # 當作 f 檔案
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') 

 
