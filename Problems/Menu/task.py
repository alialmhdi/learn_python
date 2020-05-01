order = input()
pizza = ["Margarita", "Four Seasons", "Neapoletana", "Vegetarian", "Spicy"]
salad = ["Caesar salad", "Green salad", "Tuna salad", "Fruit salad"]
soup = ["Chicken soup", "Ramen", "Tomato soup", "Mushroom cream soup"]
if order == "pizza":
    print("Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy")
elif order == "salad":
    print("Caesar salad, Green salad, Tuna salad, Fruit salad")
elif order == "soup":
    print("Chicken soup, Ramen, Tomato soup, Mushroom cream soup")
else:
    print("Sorry, we don't have it in the menu")
