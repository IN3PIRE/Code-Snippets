import random

def print_slow(text):
    """Prints text one character at a time, simulating typing."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def intro():
    """Presents the game's introduction."""
    print_slow("You awaken in a dense forest, sunlight filtering through the canopy.")
    print_slow("A chill wind whispers secrets through the trees, carrying the scent of pine and earth.")
    print_slow("You remember nothing... except the faint glimmer of a distant tower.")

def choose_path():
    """Presents the first choice to the player."""
    print_slow("\nYou stand at a fork in the path.  One path leads north, toward the distant tower.")
    print_slow("The other path winds south, deeper into the forest.")
    while True:
        choice = input("Which path will you take? (North/South): ").lower()
        if choice in ("north", "south"):
            return choice
        else:
            print_slow("Invalid choice. Please enter 'North' or 'South'.")

def north_path():
    """The path leading to the tower."""
    print_slow("\nYou follow the path north, the tower growing larger with each step.")
    print_slow("As you approach, you hear a faint humming, like an ancient song.")
    print_slow("You reach the tower's entrance, an imposing oak door carved with strange symbols.")
    print_slow("Before you can touch the door, a figure emerges from the shadows...")

def south_path():
    """The path leading deeper into the forest."""
    print_slow("\nYou venture south, the forest thickening around you.")
    print_slow("The air grows heavy with the scent of damp earth and decaying leaves.")
    print_slow("You come across a clearing, where a lone figure sits beneath a gnarled tree.")
    print_slow("The figure is shrouded in darkness, its face hidden in the shadows.")
    print_slow("The figure raises its head, and you see...")

def main():
    """The main game loop."""
    intro()
    path_choice = choose_path()
    if path_choice == "north":
        north_path()
    elif path_choice == "south":
        south_path()

if __name__ == "__main__":
    main()
