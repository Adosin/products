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



 
