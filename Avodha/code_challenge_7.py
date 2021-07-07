products = {"shoe":180,"shirt":750,"tshirt":90}

Search = input('Enter the product name to search:')

for i in products:
    if i == Search:
        print(products[i])