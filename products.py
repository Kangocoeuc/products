import os  # operation system

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,价格' in line:
                continue
            parts = line.strip().split(',')
            if len(parts) == 2:
                name, price = parts
                products.append([name, price])
            else:
                print(f"跳过无效行: {line}")
    return products

def user_input(products):
    while True:
        name = input('请输入商品名称: ')
        if name == 'q':
            break
        price = input('请输入商品价格: ')
        try:
            price = int(price)
        except ValueError:
            print("请输入有效的价格，必须是整数。")
            continue
        products.append([name, price])
    return products

def print_products(products):
    for p in products:
        print(p[0], '的价格是', p[1])

def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,价格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    products = []
    if os.path.isfile(filename):
        print('找到档案')
        products = read_file(filename)
    else:
        print('找不到档案.....')

    products = user_input(products)
    print_products(products)
    write_file(filename, products)

if __name__ == '__main__':
    main()
