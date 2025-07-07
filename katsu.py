def katsu_curry_creations():
    print("Irasshaimase! This is Katsu Curry Creations.")

    while True:
        response = input("Would you like to take a seat? (yes/no): ").strip().lower()
        if response == "no":
            print("No worries! Hope to see you again soon.")
            return
        elif response == "yes":
            break
        else:
            print("Sorry, I didn't understand that.")

     while True:
        size = input("Great! What size katsu curry would you like? (small/medium/large): ").strip().lower()
        if size in ["small", "medium", "large"]:
            print(f"You've selected a {size} katsu curry. Great choice!")
            break
        else:
            print("Sorry, please choose from small, medium, or large.")

    toppings_list = ["extra chicken", "cheese", "egg", "spring onions", "spicy mayo"]
    print("\nHere are our available toppings:")
    for i, topping in enumerate(toppings_list, 1):
        print(f"{i}. {topping.title()}")

    print("You can choose multiple toppings separated by commas (e.g., 1,3,5) or press Enter to skip.")



print("Enjoy your katsu curry from Katsu Curry Creations! Arigatou gozaimashita!")
