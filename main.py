import random


options = ["R", "S", "P"]

cpu_choice = random.choice(options)
player_choice = input("""Choose one of "R", "S" or "P" """)

while cpu_choice != player_choice:
    if player_choice not in options:
        print("Invalid choice")
        player_choice = input("""Choose one of "R", "S" or "P" """)
    elif player_choice != cpu_choice:
        print("CPU", (cpu_choice), " :Player", (player_choice))
    elif player_choice == cpu_choice:
        print("Congratulation! you win.")
    pass

