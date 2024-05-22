from products import Product
from store import Store


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(f"Total quantity in store: {store.get_total_quantity()}")

    order_cost = store.order([(products[0], 1), (products[1], 2)])
    print(f"Order cost: {order_cost} dollars.")


if __name__ == "__main__":
    main()