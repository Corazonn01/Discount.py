# Discount.py
def get_real_price(price, discount):
    discount_percentage = (discount/100) * price
    total_price = price - discount_percentage 
    return total_price 

input_price = int(input("Type a price without discount: "))
get_discount = int(input("Type a discount for an item: "))

final_price = get_real_price(input_price, get_discount)
print(f"The price of the item after a {get_discount}% discount is: {final_price}")
