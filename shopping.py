
import boto3
s3 = boto3.resource("s3")
my_bucket = s3.Bucket("shopping-system-sprint-project")

f = open("products.dat") #Opens the products data file
file = f.readlines() 
cartdict = dict() 
products = dict() 
products_list = [] 
cart = []   

subtotal = 0 
hst_rate = 0.15 #hst rate

for line in file:    
    l = line.split(":")   
    name = l[0]  
    cost = float(l[1]) 
    quantity = int(l[2]) 
    products[name] = {"name" : name, "cost" : cost, "quantity" : quantity}
    products_list.append(products[name]) 

print("HELLO, WELCOME TO THE MOS EISLEY CANTINA, BUY SOMETHING OR GET OUT : ")
for i in products_list:
    print(i)
while True: #loop for continuous inputs
    print("What would you like to purchase? ")
    for product in products:  # Displays the inventory of items drawn from the products.dat file
        print(product)
    while True:
        choice = input("What do you want to purchase? ") #Prompts the user for input on what they would like to purchase
        if choice not in products:
           print("{} is an unrecognized item. Please try again.".format(choice))
        else:
            break
    
    if choice.lower() == "carrots":
        quantity_purchased = int(input("How many would you like to buy? "))
        if products_list[0]["quantity"] < 0 or products_list[0]["quantity"] < quantity_purchased:
            print("Quantity is invalid!" )
        item_total = quantity_purchased * products_list[0]["cost"]
        total_cost = input("your total for this product is ${} is this okay? ('y' or 'n')".format(item_total))
        if total_cost.lower() == "y":
            products_list[0]["quantity"] = products_list[0]["quantity"] - quantity_purchased
            cartdict[choice] = {"choice" : choice, "quantity" : quantity_purchased, "subtotal" : item_total}
            cart.append(cartdict[choice])
            subtotal += item_total
    
    if choice.lower() == "bananas":
        quantity_purchased = int(input("How many would you like to buy? "))
        if products_list[1]["quantity"] < 0 or products_list[1]["quantity"] < quantity_purchased:
            print("Quantity is invalid!" )
        item_total = quantity_purchased * products_list[1]["cost"]
        total_cost = input("your total for this product is ${} is this okay? ('y' or 'n')".format(item_total))
        if total_cost.lower() == "y":
            products_list[1]["quantity"] = products_list[1]["quantity"] - quantity_purchased
            cartdict[choice] = {"choice" : choice, "quantity" : quantity_purchased, "subtotal" : item_total}
            cart.append(cartdict[choice])
            subtotal += item_total
        
    if choice.lower() == "frozen pizza": 
        quantity_purchased = int(input("How many would you like to buy? "))
        if products_list[2]["quantity"] < 0 or products_list[2]["quantity"] < quantity_purchased:
            print("Quantity is invalid!" )
        item_total = quantity_purchased * products_list[2]["cost"]
        total_cost = input("your total for this product is ${} is this okay? ('y' or 'n')".format(item_total))
        if total_cost.lower() == "y":
            products_list[2]["quantity"] = products_list[2]["quantity"] - quantity_purchased
            cartdict[choice] = {"choice" : choice, "quantity" : quantity_purchased, "subtotal" : item_total}
            cart.append(cartdict[choice])
            subtotal += item_total
    
    if choice.lower() == "juice":
        quantity_purchased = int(input("How many would you like to buy? "))
        if products_list[3]["quantity"] < 0 or products_list[3]["quantity"] < quantity_purchased:
            print("Quantity is invalid!" )
        item_total = quantity_purchased * products_list[3]["cost"]
        total_cost = input("your total for this product is ${:.2f} is this okay? ('y' or 'n')".format(item_total))
        if total_cost.lower() == "y":
            products_list[3]["quantity"] = products_list[3]["quantity"] - quantity_purchased
            cartdict[choice] = {"choice" : choice, "quantity" : quantity_purchased, "subtotal" : item_total}
            cart.append(cartdict[choice])
            subtotal += item_total
        
    if choice.lower() == "enchanted golden apples":
        quantity_purchased = int(input("How many would you like to buy? "))
        if products_list[4]["quantity"] < 0 or products_list[4]["quantity"] < quantity_purchased:
            print("Quantity is invalid!" )
        item_total = quantity_purchased * products_list[4]["cost"]
        total_cost = input("your total for this product is ${:.2f} is this okay?('y' or 'n')".format(item_total))
        if total_cost.lower() == "y":
            products_list[4]["quantity"] = products_list[4]["quantity"] - quantity_purchased
            cartdict[choice] = {"choice" : choice, "quantity" : quantity_purchased, "subtotal" : item_total}
            cart.append(cartdict[choice])
            subtotal += item_total
            
    if choice.lower() == "blue milk": 
        quantity_purchased = int(input("How many would you like to buy? "))
        if products_list[5]["quantity"] < 0 or products_list[5]["quantity"] < quantity_purchased:
            print("Quantity is invalid!")
        item_total = quantity_purchased * products_list[5]["cost"]
        total_cost = input("your total for this product is ${} is this okay? ('y' or 'n')".format(item_total))
        if total_cost.lower() == "y":
            products_list[5]["quantity"] = products_list[5]["quantity"] - quantity_purchased
            cartdict[choice] = {"choice" : choice, "quantity" : quantity_purchased, "subtotal" : item_total}
            cart.append(cartdict[choice])
            subtotal += item_total
            
    if choice.lower() == "rankor steak":
        quantity_purchased = int(input("How many would you like to buy? "))
        if products_list[6]["quantity"] < 0 or products_list[6]["quantity"] < quantity_purchased:
            print("Quantity is invalid!" )
        item_total = quantity_purchased * products_list[6]["cost"]
        total_cost = input("your total for this product is ${} is this okay ('y' or 'n')".format(item_total))
        if total_cost.lower() == "y":
            products_list[6]["quantity"] = products_list[6]["quantity"] - quantity_purchased
            cartdict[choice] = {"choice" : choice, "quantity" : quantity_purchased, "subtotal" : item_total}
            cart.append(cartdict[choice])
            subtotal += item_total
            
    hst = subtotal * hst_rate 
    total = subtotal + hst 
    
    #Continue statement to prompt the user if they want to continue adding to their shopping list
    cont = "" #initializes the cont variable
    if total_cost =='n':
        cont = input("Would you like to continue shopping?(y or n): ")
    if total_cost =='y':
        cont = input("Would you like to continue shopping?(y or n): ")
    if cont.lower() == 'y':
        continue
    else:
        #When 'n' is selected, the receipt is shown here
        print("Here is your receipt ")
        print("The items you wish to purchase: ")
        for cart_item in cart: #displays the items in the current shopping list
            print(cart_item)
        
        print("Your subtotal is: ${:.2f}\n".format(subtotal))
        print("HST: ${:.2f}\n".format(hst))
        print("Your total after tax is ${:.2f}\n".format(total))
        
        #saves a copy of the receipt in a file called receipt.txt for records.
        r = open("receipt.txt","w")
        r.write("Here is your receipt!'\n")
        for cart_item in cart:
            r.write("{}\n".format(cart_item))
        r.write("SUBTOTAL:     ${:.2f}\n".format(subtotal))
        r.write("TAX:          ${:.2f}\n".format(hst))
        r.write("TOTAL:        ${:.2f}\n".format(total))
        
        my_bucket.upload_file("receipt.txt", "Receipt_upload.txt")
        break
