# WRITE YOUR FUNCTIONS HERE

# returns the name of the pet shop
def   get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

#it gives back the total cash amount
def get_total_cash(pet_shop_cash):
    return pet_shop_cash["admin"]["total_cash"]

# it adds or remove cash from the shop
def add_or_remove_cash(pet_shop_cash, amount):
    pet_shop_cash["admin"]["total_cash"] = pet_shop_cash["admin"]["total_cash"] + amount


#it reterns the number of pets that have been sold
def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]

# it change the amount of the sold pets
def increase_pets_sold(sold_pets,pets):
    sold_pets["admin"]["pets_sold"] +=  pets

#it returns the stock
def get_stock_count(pets_in_stock):
    return len(pets_in_stock["pets"])

#it gives back a list of pets that have a specific breed
def get_pets_by_breed(pets_in_stock,pet_breed):
    pets_found = []
    for pet in pets_in_stock["pets"]:
        if pet["breed"] == pet_breed:
            pets_found.append(pet)

    return pets_found

#it finds pets in stock by the name
def find_pet_by_name(pets_in_stock, pet_name):
    for pet in pets_in_stock["pets"]:
        if pet["name"] is pet_name:
            return pet
        
#it removes a pet from the stock by giving the name
def remove_pet_by_name(pets_in_stock,pet_name):
    for pet in pets_in_stock["pets"]:
        if pet["name"] == pet_name:
            pets_in_stock["pets"].remove(pet)

# it adds a pet in the stock list
def add_pet_to_stock(pets_in_stock, new_pet):
    pets_in_stock["pets"].append(new_pet)

#it gives back a customer cash
def get_customer_cash(customer):
    return customer["cash"]

#it removes the amount of money that they spend from their badget
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

#it gives back the number of pets the customer owns
def get_customer_pet_count(customer):
    return len(customer["pets"])

#it adds a pet to a customer
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

#it checks if the customer can afford to buy the pet
def customer_can_afford_pet(customer,new_pet):
    return customer["cash"] >= new_pet["price"]

# last answer was from solutions
def sell_pet_to_customer(pet_shop,new_pet,customer):
    if new_pet != None and customer_can_afford_pet(customer,new_pet):
        remove_pet_by_name(pet_shop,new_pet["name"])
        add_pet_to_customer(customer,new_pet)
        remove_customer_cash(customer,new_pet["price"])
        add_or_remove_cash(pet_shop,new_pet["price"])
        increase_pets_sold(pet_shop,1)  