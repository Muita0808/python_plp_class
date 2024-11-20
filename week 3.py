def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    If the discount is 20% or higher, apply it. Otherwise, return the original price.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.

    Returns:
    float: The final price after applying the discount (or the original price).
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

# Get input from the user
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Output the result
    if discount_percent >= 20:
        print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")
