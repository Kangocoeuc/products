products = []
while True:
	name = input('请输入商品名称: ')
	if name == 'q':
		break
	price = input('请输入商品价格: ')
	#p = []
	#p.append(name)
	#p.append(price)
		#p = [name, price]
	products.append([name, price])
print(products)
for p in products:
	print(p[0], '的价格是', p[1])














