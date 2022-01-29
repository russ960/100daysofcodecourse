MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cash_drawer = 0.00
machine_on = True

def resource_check(beverage_type, resources_available):
    """Takes in the beverage type and current resources and return a dictionary containing a message and success flag."""
    output_message = {"success":True, "message":""}
    
    water_needs = MENU[beverage_type]['ingredients']['water']
    if water_needs > resources_available['water']:
        output_message["message"] += "There is not enough water.  "
        output_message["success"] = False
    
    if beverage_type != 'espresso':
        milk_needs = MENU[beverage_type]['ingredients']['milk']
        if milk_needs > resources_available['milk']:
            output_message["message"] += "There is not enough milk.  "
            output_message["success"] = False
    
    coffee_needs = MENU[beverage_type]['ingredients']['coffee']
    if coffee_needs > resources_available['coffee']:
        output_message["message"] += "There is not enough coffee."
        output_message["success"] = False
    return output_message

def payment_check(beverage_type, payment_amount):
    """Takes in the beverage type and payment amount.  Returns a dictionary with success flag, message 
    and refund amount."""
    payment_amount_required = MENU[beverage_type]['cost']
    if payment_amount_required > payment_amount:
        return {'success':False, 'message':"Sorry that's not enough money. Money refunded."}
    elif payment_amount_required <= payment_amount:
        difference = payment_amount - payment_amount_required
        return {'success':True, 'message':f"Here is ${difference:.2f} in change.", 'refund':difference}

while machine_on:
    money_inserted = 0.00
    user_request_type = input("​What would you like? (espresso/latte/cappuccino): ")
    if user_request_type == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${cash_drawer:.2f}")
    elif user_request_type == 'off':
        print("Turning off machine.")
        machine_on = False
    else:
        print("Please insert coins.")
        money_inserted += int(input("How many quarters?: ")) * .25
        money_inserted += int(input("How many dimes?: ")) * .10
        money_inserted += int(input("How many nickels?: ")) * .05
        money_inserted += int(input("How many pennies?: ")) * .01

        payment_check_output = payment_check(user_request_type, money_inserted)
        resource_check_output = resource_check(user_request_type,resources)
        if payment_check_output["success"] == False:
            print(payment_check_output["message"])
        elif resource_check_output["success"] == False:
            print(resource_check_output["message"])
        else:
            cash_drawer += (money_inserted - payment_check_output["refund"])
            if user_request_type != 'espresso':
                resources["milk"] -= MENU[user_request_type]["ingredients"]["milk"]
            resources["water"] -= MENU[user_request_type]["ingredients"]["water"]
            resources["coffee"] -= MENU[user_request_type]["ingredients"]["coffee"]
            print(payment_check_output["message"])
            print(f"Here is your {user_request_type} ☕️. Enjoy!")


