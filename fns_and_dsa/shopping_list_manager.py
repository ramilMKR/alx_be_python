def display_menu():
    print("Shopping List Manager")
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
            shopping_list.append(item)

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found in the shopping list.")

        elif choice == 3:
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
