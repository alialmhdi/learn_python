# Write your code here
class CoffeeMachine:
    total_of_water_has = 400
    total_of_milk_has = 540
    total_of_coffee_has = 120
    number_of_cups_has = 9
    money_inside = 550

    def __init__(self, water, milk, coffee, cups, money):
        self.total_of_water_has = water
        self.total_of_milk_has = milk
        self.total_of_coffee_has = coffee
        self.number_of_cups_has = cups
        self.money_inside = money

    def buy(self, order):
        if order == "1":
            self.make_coffee(250, 0, 16, 4)
        elif order == "2":
            self.make_coffee(350, 75, 20, 7)
        elif order == "3":
            self.make_coffee(200, 100, 12, 6)

    def make_coffee(self, water, milk, coffee, money):
        if self.total_of_water_has >= 250:
            if self.total_of_coffee_has >= 16:
                if self.number_of_cups_has >= 1:
                    if milk != 0:
                        if self.total_of_milk_has >= 75:
                            self.total_of_water_has -= water
                            self.total_of_milk_has -= milk
                            self.total_of_coffee_has -= coffee
                            self.number_of_cups_has -= 1
                            self.money_inside += money
                            print("I have enough resources, making you a coffee!")
                        else:
                            print("Sorry, not enough milk!")
                    else:
                        self.total_of_water_has -= water
                        self.total_of_coffee_has -= coffee
                        self.number_of_cups_has -= 1
                        self.money_inside += money
                else:
                    print("Sorry, not enough cups!")
            else:
                print("Sorry, not enough coffee!")
        else:
            print("Sorry, not enough water!")

    def fill_machine(self, water, milk, coffee, cups):
        self.total_of_water_has += water
        self.total_of_milk_has += milk
        self.total_of_coffee_has += coffee
        self.number_of_cups_has += cups

    def money(self):
        print(f"I gave you ${self.money_inside}")
        self.money_inside = 0

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.total_of_water_has} of water")
        print(f"{self.total_of_milk_has} of milk")
        print(f"{self.total_of_coffee_has} of coffee beans")
        print(f"{self.number_of_cups_has} of disposable cups")
        print(f"${self.money_inside} of money")


coffee_bean = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    user_order = input("Write action (buy, fill, take, remaining, exit):")
    if user_order == "buy":
        buy_sub_command = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_bean.buy(buy_sub_command)
    elif user_order == "fill":
        total_of_water_add = int(input("Write how many ml of water do you want to add:"))
        total_of_milk_add = int(input("Write how many ml of milk do you want to add:"))
        total_of_coffee_add = int(input("Write how many grams of coffee beans do you want to add:"))
        number_of_cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        coffee_bean.fill_machine(total_of_water_add, total_of_coffee_add, total_of_milk_add, total_of_coffee_add)
    elif user_order == "take":
        coffee_bean.money()
    elif user_order == "remaining":
        coffee_bean.remaining()
    elif user_order == "exit":
        break
