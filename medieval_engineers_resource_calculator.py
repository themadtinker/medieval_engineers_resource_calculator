from collections import Counter

items = dict()


def create_tables():
    global items
    items['sticks'] = {'log': (1/15)}
    items['timber'] = {'log': (1/4)}
    items['planks'] = {'timber': (1/4)}
    items['metal parts'] = {'iron ingot': (1/10)}
    items['large chest'] = {'planks': 8, 'metal parts': 4}
    items['seeder'] = {'large chest': 1, 'timber': 10, 'metal parts': 18}
    items['plow'] = {'sticks': 15, 'timber': 4, 'metal parts': 60}
    items['harvester'] = {'large chest': 1, 'timber': 10, 'metal parts': 16}
    items['farm unit'] = {'harvester': 1, 'plow': 1, 'seeder': 1}


def get_components(item_name, item_count):
    if len(item_name) > 0 and item_name in items.keys():
        temp_item = dict(items[item_name])  # create a local copy of the item
        for component in temp_item:
            temp_item[component] *= item_count
            new_components = get_components(component, temp_item[component])
            if len(new_components) > 0:
                temp_item[component] = 0
            temp_item = dict(Counter(temp_item) + Counter(new_components))
        return temp_item
    else:
        return dict()


if __name__ == '__main__':
    create_tables()
    a = get_components('farm unit', 1)
    print(a)
