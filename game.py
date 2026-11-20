while True:
    health=100
    print("================================")
    print("     THE MYSTERY ADVENTURE")
    print("================================")

    player_name = input("Enter your name: ")

    print("Welcome", player_name)
    print("You wake up in a mysterious forest.")
    print("There are two paths in front of you.")

    print("1. Go left")
    print("2. Go right")

    choice = input("Choose your path (1 or 2): ")

    if choice == "1":
        print("You found a treasure chest!")

    elif choice == "2":
        print("Oh no! You found a dangerous tiger!")
        print("1. Fight the Tiger!")
        print("2. Run Away!")
        action = input("Choose your action (1 or 2): ")
        if action == "1":
            print("The Tiger is attacking!")
            while health > 0:
                print("The Tiger attacked you!")
                health-=20
                print("Your health: ",health)
                if health <= 0:
                    print("Game Over!")
                    break
                print("1. Fight Again!")
                print("2. Run Away!")
                action = input("Choose your action (1 or 2): ")
                if action == "1":
                    print("The Tiger is attacking again!")
                elif action == "2":
                    print("You're Escaped fromt the Tiger and your Health is:",health)
                    break
                else :
                    print("Invalid choice!Tiger attacks again!")



        elif action == "2":
            print("You escaped the Tiger!")
        else:
            print("Invalid answer. Try again.")


    else:
        print("Invalid choice!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "no":
        print("Thanks for playing!")
        break

