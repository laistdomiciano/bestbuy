import pytest
from products import Product

# Test that creating a normal product works.
def test_create_normal_product():
    product = Product("Laptop", 1500, 10)
    assert product.name == "Laptop"
    assert product.price == 1500
    assert product.quantity == 10
    assert product.is_active()


# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", 1500, 10)  # Empty name

    with pytest.raises(ValueError):
        Product("Laptop", -1500, 10)  # Negative price

    with pytest.raises(ValueError):
        Product("Laptop", 1500, -10)  # Negative quantity


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_product_reaches_zero_quantity():
    product = Product("Laptop", 1500, 1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert not product.is_active()


# Test that product purchase modifies the quantity and returns the right output.
def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("Laptop", 1500, 10)
    total_price = product.buy(3)
    assert product.get_quantity() == 7
    assert total_price == 4500


# Test that buying a larger quantity than exists invokes exception.
def test_buying_larger_quantity_than_exists():
    product = Product("Laptop", 1500, 5)
    with pytest.raises(Exception):
        product.buy(10)

def test_buy_with_invalid_quantity():
    product = Product("Laptop", 1500, 5)
    with pytest.raises(ValueError):
        product.buy(0)  # Quantity to buy should be greater than zero
    with pytest.raises(ValueError):
        product.buy(-1)  # Quantity to buy should be greater than zero
