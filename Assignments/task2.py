menu = {
        'vadapav':30,
        'bhel':70,
        'dabeli':20
    }
status = True
while status:
    
    for k,v in menu.items():
        print(f"{k} = {v}")
    oder = input("enter your oder: ").lower()
    qty = input("Enter no of quantity: ")
    while True:
        if qty.isdigit():
            qty = int(qty)
            break
        else:
            qty = input("Enter no of quantity: ")
    if oder in menu:
        i = menu[oder]
        total = qty*i
        print(f"Your total amount is {total}")
    else:
        print("Food not available")
    again = input("Do you want to add another food y/n: ").lower()
    if again =='y':
        continue
    else:
        status = False