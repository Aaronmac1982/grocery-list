def grocery_list():
    """
    Function to manage a grocery shopping list
    """
    items = [] # make a empty list to store grocery items
    
    while True:
        print("\nChoose an action:")
        print("1. Add item")
        print("2. View list")
        print("3. Delete item")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            new_item = input("Enter grocery item: ")
            items.append(new_item)
            print("Item added")
        elif choice == '2':
            if not items:
                print("Your list is empty")
            else:
                print("Grocery list:")
                for item in items:
                    print("- " + item)
        elif choice == '3':
            print("Exiting grocery list.")
            break
        else:
            print("Invalid choice.")
            
#start the grocery list application
grocery_list()