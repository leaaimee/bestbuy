import store
import products

def start(store_instance):

    def list_products()-> None:
        """Displays all products currently available in the store"""
        product_list = store_instance.get_all_products()
        for product in product_list:
            print(product.show())


    def show_total() -> None:
        """Prints the total quantity of all items available in the store"""
        print(f"Total quantity in store: {store_instance.get_total_quantity()} Items")

    def make_order() -> None:
        """Allows the user to select products and quantities to purchase"""
        shopping_list = []
        product_list = store_instance.get_all_products()  # This ensures product_list is defined

        for i, product in enumerate(product_list, 1):
            print(f"{i}. {product.show()}")

        while True:
            try:
                user_choice = input("Choose a product by number (or type 'done' to finish): ")
                if user_choice.lower() == "done":
                    break
                product_index = int(user_choice) - 1

                if product_index < 0 or product_index >= len(product_list):
                    print("Invalid choice. Please select a valid product number.")
                    continue

                quantity = int(input("Enter quantity: "))

                product_list[product_index].buy(quantity)
                shopping_list.append((product_list[product_index], quantity))
            except ValueError as ve:
                print(f"Error: {ve}")
            except (IndexError, ValueError):
                print("Invalid choice. Please try again.")

        total_price = store_instance.order(shopping_list)
        print(f"Total order cost: ${total_price:.2f}")


    def quit_program() -> str:
        """Ends the program with a farewell message"""
        print("Thank you for visiting! Goodbye ")
        return "quit"

    menu_options = {
        "1": list_products,
        "2": show_total,
        "3": make_order,
        "4": quit_program
    }

    while True:
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        action = menu_options.get(choice)
        if action:
            result = action()
            if result == "quit":
                break
        else:
            print("Invalid choice. Please try again")


def main() -> None:

    product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                     products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                     products.Product("Google Pixel 7", price=500, quantity=250)
                   ]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()