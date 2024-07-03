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
        choice = input("Enter your choice: ")

        if choice == '1':
             itemAdd = input("Add the element you want to put in your shopping list: ")
             shopping_list.append(itemAdd)  
        elif choice == '2':
            itemRemove = input("Enter the item to add: ")
            if len(shopping_list) == 0:
                print("The list is empty")
                continue
            elif itemRemove not in shopping_list:
                print("The element doesn't exisist in shopping_list")
                continue 
            else:
                shopping_list.remove(itemRemove)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()