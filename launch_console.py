def main():
    print("Welcome to the Launch Console!")
    name = input("What's your name? ")
    print(f"Hi, {name}!")

    # 3: Menu list
    menu = ["1. About me", "2. My goals", "3. Favorite hobby", "4. Exit"]

    running = True
    while running:
        print("\n--- MENU ---")
        for option in menu:
            print(option)

        choice = input("Pick an option: ")

        if choice == "1":
            print("\nAbout Me: I am a developer learning Python and building projects!")
        elif choice == "2":
            print("\nMy Goals: Ship my first real project and master Git.")
        elif choice == "3":
            print("\nFavorite Hobby: I love coding, gaming, and exploring new tech.")
        elif choice == "3" or choice == "4":
            print("\nGoodbye!")
            running = False
        elif choice == "4":
            print("\nPlease pick a valid option.")

if __name__ == "__main__":
    main()
