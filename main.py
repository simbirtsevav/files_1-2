def book(file):

    cook_book = {}
    with open(file, "rt", encoding='utf8') as file_obj:
        for cook in file_obj:
            ingridient_list = []
            dish = cook.strip()
            count = int(file_obj.readline())
            for i in range(count):
                ingridient = file_obj.readline().split('|')
                ingridient_dict = {}
                ingridient_dict['ingridient_name'] = ingridient[0]
                ingridient_dict['quantity'] = int(ingridient[1])
                ingridient_dict['measure'] = ingridient[2].strip()
                ingridient_list.append(ingridient_dict)
                # print('ЛИСТ', ingridient_list)
                cook_book[dish] = ingridient_list
            emty_line = file_obj.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):

    dish_dict = {}
    cook_book = book('recipes.txt')
    for dish in dishes:
        if dish not in cook_book:
            print(f'Блюда {dish} в поваренной книге не найдено. ')
            return
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] not in dish_dict:
                dish_dict[ingridient['ingridient_name']] =({'measure': ingridient['measure'],
                                                            'quantity': int(ingridient['quantity'])*person_count})
            else:
                count = ((dish_dict[ingridient['ingridient_name']]['quantity'] +
                          int(ingridient['quantity']) * person_count))
                dish_dict[ingridient['ingridient_name']] = {'measure': ingridient['measure'],
                                                            'quantity': count}
                print('Список покупок: ', dish_dict)
print(book('recipes.txt'))
get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Утка по-пекински'], 2)