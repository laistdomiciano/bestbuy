from products import Product, NonStockedProduct, LimitedProduct
from store import Store


# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250),
                 NonStockedProduct("Windows License", price=125),
                 LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = Store(product_list)


def list_products():
    """List all the products"""
    products = best_buy.get_all_products()
    for index, product in enumerate(products):
        print(f"{index + 1}. {product.show()}")


def show_total_amount():
    """Show total amount of products"""
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")


def make_order():
    """Input user's oders"""
    print("When you want to finish order, enter empty text.")
    order_list = []
    products = best_buy.get_all_products()

    while True:
        list_products()  # Display the list of products
        user_choice = input("Enter the product number you want to buy (or press Enter to finish): ")

        if user_choice == "":
            break

        try:
            product_index = int(user_choice) - 1
            if product_index < 0 or product_index >= len(products):
                print("Invalid product number. Please try again.")
                continue

            quantity = int(input(f"Enter the quantity for {products[product_index].name}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero. Please try again.")
                continue

            order_list.append((products[product_index], quantity))
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    try:
        total_price = best_buy.order(order_list)
        print(f"Order cost: {total_price} dollars.")
    except Exception as e:
        print(f"Order failed: {e}")


def quit():
    """Exit the program"""
    print("Exiting the store menu.")
    exit()


def start():
    menu = ["List all products in store", "Show total amount in store", "Make an order", "Quit"]
    my_menu = {
        1: list_products,
        2: show_total_amount,
        3: make_order,
        4: quit
    }

    while True:
        print("Store Menu")
        print("----------")
        for index, item in enumerate(menu):
            print(index + 1, item)
        user_choice = int(input("Please choose a number: \n"))
        if user_choice in my_menu:
            my_menu[user_choice]()
        else:
            print("Invalid option, please try again.\n")


def main():
    start()


if __name__ == "__main__":
    main()

