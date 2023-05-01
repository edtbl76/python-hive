#!/usr/bin/env python3

# Checkpoint 1
# Example Structure
tables = {
    1: {
        'name': 'Chioma',
        'vip_status': False,
        'order': {
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes'
        }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}
print(tables)


# Checkpoint 2
def assign_food_items(**order_items):
    print(order_items)
    # Checkpoint 3
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    # Checkpoint 4
    print(food)
    print(drinks)


# Checkpoint 5
# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

