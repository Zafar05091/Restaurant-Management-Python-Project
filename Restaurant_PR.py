#First, we will creat a menu for our Restaurant Project using Dictionary 

menu = {
    'Pizza': 150,
    'Burger': 100,
    'Coffee': 80,
    'Pasta': 120,
    'Salad': 80,
    'Meal box': 450,
    'French fries': 130,
    'Cup cake': 180,
    'Lawa cake': 200,
    'Ice-cream with extra cream': 200
}

print("Welcome To Al-Falza Restaurant")
print("Dishesh:\tDeserts:\nPizza: 150\tcup cake: 100\nBurger: 100\tLawa cake: 200\nCoffee: 80\tIce-cream with extra cream: 200\nPasta: 120\nSalad: 80\nMeal box: 450\nFrench fries: 130")

# Now we will creat a variable name Total order in which whatever customer adds, its total amount will be added

Order_total = 0
Dish_1 =input("Enter the name of Dish you want to order: ")

# We will use the Membership operator to check weather the dish selected by the user is on our menu or not

if Dish_1 in menu:
    Order_total += menu[Dish_1]
    print(f"Your Dish '{Dish_1}' has benn added to your order")
else:
    print(f"Ordered Dish '{Dish_1}' is not available Yet!")

Another_order = input("Do you want to add Another Dish/Deserts in your order? (Yes/No): ")
if Another_order == "No":
    print("Thank You For Order")
if Another_order == "Yes":
    print("Pizza: 150\tDeserts:\nBurger: 100\tcup cake: 100\nCoffee: 80\tLawa cake: 200\nPasta: 120\tIce-cream with extra cream: 200\nSalad: 80\nMeal box: 450\nFrench fries: 130")
    Dish_2_Deserts = input("Enter the name of second dish or Desert: ")
    if Dish_2_Deserts in menu:
        Order_total += menu[Dish_2_Deserts]
        print(f"Your Dish/Desert '{Dish_2_Deserts}' has been added to your order")
        print("Thank You For Order")
    else:
        print("Ordered Dish '{Dish_2_Deserts}' is not available! Sorry..!")

print(f"The Total Amount to Pay is: {Order_total}")

