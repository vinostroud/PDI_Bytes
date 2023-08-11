import copy

items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    items = items.copy()
    items[0]['name'] = 'macbook'
    items[1]['id'] = 4
    items[2]['value'] = 30
    return items[:]

print(duplicate_items(items))
print(items)