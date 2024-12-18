# Step 1: Create the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply the discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # No discount, return the original price
        return price

# Step 2: Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Calculate and print the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price != price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
