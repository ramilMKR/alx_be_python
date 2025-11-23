def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid choice. Please enter a number (1-4).")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("No item entered. Nothing was added.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if not item:
                print("No item entered.")
            else:
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed.")
                else:
                    print(f"Item '{item}' not found in the shopping list.")

        elif choice == 3:
            print("\nCurrent Shopping List:")
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
