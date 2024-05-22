from products import Product
from store import Store

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)


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