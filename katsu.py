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


print("Enjoy your katsu curry from Katsu Curry Creations! Arigatou gozaimashita!")
