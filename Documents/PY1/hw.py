def make_cook_book():
	cook_book = {}

	with open('cook_book.txt') as f:
		for line in f:
			dish = line.strip().lower()
			cook_book[dish] = []
			ingr_num = int(f.readline().strip())
			for i in range(ingr_num):
				s = f.readline().strip().split('|')
				cook_book[dish].append(dict(ingridient_name = s[0].strip(), quantity = int(s[1].strip()), measure = s[2].strip()))
			f.readline()
	return cook_book

def get_shop_list_by_dishes(dishes, person_count):
	cook_book = make_cook_book()
	shop_list = {}
	for dish in dishes:
		for ingridient in cook_book[dish]:
			new_shop_list_item = dict(ingridient)
			new_shop_list_item['quantity'] *= person_count
			if new_shop_list_item['ingridient_name'] not in shop_list:
				shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
			else:
				shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
	return shop_list

def print_shop_list(shop_list):
	for shop_list_item in shop_list.values():
		print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
	person_count = int(input('Введите количество человек: '))
	dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
	shop_list = get_shop_list_by_dishes(dishes, person_count)
	print_shop_list(shop_list)

create_shop_list()