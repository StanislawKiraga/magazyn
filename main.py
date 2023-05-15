import csv


items = [
    {
    'name': 'milk',
    'quantity': 120,
    'unit': 'l',
    'unit_price': 2.3,
    },
    {
    'name': 'sugar',
    'quantity': 1000,
    'unit': 'kg',
    'unit_price': 3,
    },
    {
    'name': 'flour',
    'quantity': 12000,
    'unit': 'kg',
    'unit_price': 1.2,
    },
    {
    'name': 'coffee',
    'quantity': 25,
    'unit': 'kg',
    'unit_price': 40,
    }
]

sold_items = []

def menu():
    print(20 * '*', 'WAREHOUSE MANAGER', 20 * '*')
    while True:   
        action = input('What would you like to do?')
        if action == 'exit':
            print('Exiting... Bye!')
            break
        if action == 'show':
            get_items()
        if action == 'add':
            add_item(name=input('Item name:'), 
                     quantity=float(input('Item quantity:')),
                     unit_name=input('Item unit of measure:'), 
                     unit_price=float(input('Item price in PLN:')))
            print('Successfully add item!')
        if action == 'sell':
            sell_item(name=input('Item name:'),
                      quantity=float(input('Quantity to sell:')))
            print(items)
            export_items_to_csv()
            export_sales_to_csv()
            get_items()
        if action == 'show sold':
            get_sold_items()
        if action == 'show costs':
            print(get_costs())
        if action == 'show income':
            print(get_income())
        if action == 'show revenue':
            print(get_revenue())
        if action == 'save':
            export_items_to_csv()
            export_sales_to_csv()
            print('Successfully exported data to magazyn.csv and sales.csv.')
        if action == 'load':
            load_items_from_csv()
            
            
def get_items():
    print("{:<10} {:<10} {:<6} {:<16}".format("Name", "Quantity", "Unit", "Unit Price (PLN)"))
    print("{:<10} {:<10} {:<6} {:<16}".format("_______", "____", "____", "___________"))
    for item in items:
        print("{:<10} {:<10} {:<6} {:<16}".format(item['name'].capitalize(), item['quantity'], item['unit'], item['unit_price']))

def get_sold_items():
    print("{:<10} {:<10} {:<6} {:<16}".format("Name", "Quantity", "Unit", "Unit Price (PLN)"))
    print("{:<10} {:<10} {:<6} {:<16}".format("_______", "____", "____", "___________"))
    for item in sold_items:
        print("{:<10} {:<10} {:<6} {:<16}".format(item['name'].capitalize(), item['quantity'], item['unit'], item['unit_price']))
    

def add_item(name, unit_name, quantity, unit_price):
    item = {
        'name': name,
        'quantity': quantity,
        'unit': unit_name,
        'unit_price': unit_price
    }
    items.append(item)
        
def sell_item(name, quantity):
    for item in items:
        q = float(item['quantity'])
        if item['name'] == name:
            if q >= quantity:
                item['quantity'] = q - quantity
                print('Successfully sold', quantity, item['unit'], 'of', item['name'],'.')

                item = {
                    'name': name,
                    'quantity': quantity,
                    'unit': item['unit'],
                    'unit_price': item['unit_price']
                }
                sold_items.append(item)
            else:
                print('Insufficient quantity of ', item['name'], 'in stock.')
                
def get_costs():
    costs = [(item['unit_price'] * item['quantity']) for item in items]
    return f'{sum(costs):.2f}'

def get_income():
    income = [(item['unit_price'] * item['quantity']) for item in sold_items]
    return f'{sum(income):.2f}'

def get_revenue():
    print('Revenue breakdown (PLN)')
    print(f'Income: {get_income()}')
    print(f'Costs: {get_costs()}')
    revenue = float(get_income()) - float(get_costs())
    print('-' * 25)
    return f'Revenue: {revenue} PLN'

def export_items_to_csv():
    with open('magazyn.csv', 'w') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in items:
            writer.writerow({'name': item['name'],
                             'quantity': item['quantity'],
                             'unit': item['unit'],
                             'unit_price': item['unit_price']})
        

def export_sales_to_csv():
    with open('sales.csv', 'w') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in sold_items:
            writer.writerow({'name': item['name'],
                             'quantity': item['quantity'],
                             'unit': item['unit'],
                             'unit_price': item['unit_price']})
        
def load_items_from_csv():
    items.clear()
    with open('magazyn.csv') as csvfile: 
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {
                'name': row['name'],
                'quantity': row['quantity'],
                'unit': row['unit'],
                'unit_price': row['unit_price']
            }
            items.append(item)
        print('Successfully loaded data from magazyn.csv.')

if __name__ == '__main__':   
    load_items_from_csv()
    menu()
    
    