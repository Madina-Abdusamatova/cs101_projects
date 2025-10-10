# Assignment Description
# Create a shopping cart program that calculates the final price with discount rules and membership status.

# Requirements:

# Collect: 3 items (name, price, quantity), customer info
item1=input("Enter 1st item: ")
price1=float(input("Enter its price: "))
quantity1=int(input("How many are you buying? "))
item2=input("Enter 2nd item: ")
price2=float(input("Enter its price: "))
quantity2=int(input("How many are you buying? "))
item3=input("Enter 3rd item: ")
price3=float(input("Enter its price: "))
quantity3=int(input("How many are you buying? "))
total_previous_purchases=float(input("Enter the total amount of your previous purchases: "))

subtotal=price1*quantity1 + price2*quantity2 + price3*quantity3

# Calculate: Subtotal, discounts (using boolean arithmetic), tax, shipping
# Display: Itemized receipt with all calculations
# Submit: GitHub repository
# Key Technique - Boolean Arithmetic:

# # Use True=1, False=0 to control calculations
# is_member = True  # or False
# discount = is_member * 0.10 * subtotal  # 10% if member, 0% if not
# Important: Display ALL eligibility checks and metrics as True/False values. No if/else statements needed.

# Variant 1.1: Electronics Store
# Scenario: You’re building a checkout system for an electronics store.

# Specific Requirements:

# Collect: Item name, price, and quantity for 3 electronics items
# Get customer information: Name, is_member (yes/no), total_previous_purchases (in sum)
name=input("Enter your name: ")
is_member=input("Are you a member?(Yes/No) ")

# Discount Rules: Calculate eligibility and amounts for each discount type:
# Member discount: 10% off subtotal (eligible if customer is a member)
member_discount_eligibility = is_member == 'yes'
discount=member_discount_eligibility*0.10*subtotal
total_after_membership_discount= subtotal-discount
# Bulk discount: 5% off (eligible if total items > 5)

bulk_discount_eligibility= (quantity1+quantity2+quantity3)>5
bulk_discount=bulk_discount_eligibility*0.05*total_after_membership_discount
total_after_bulk_discount=total_after_membership_discount-bulk_discount
loyalty_discount_eligibility= total_previous_purchases>= 1000000
loyalty_discount=loyalty_discount_eligibility*0.03*total_after_bulk_discount
total_after_loyalty_discount=total_after_bulk_discount-loyalty_discount
tax_rate=0.12*total_after_loyalty_discount
shipping= (total_after_loyalty_discount <= 500000)*25000
final_price=tax_rate+shipping+total_after_loyalty_discount

# Customer name and membership status
# Itemized list of all 3 purchases (item, quantity, price, total)
# Subtotal before discountsgit
# Each discount type with:
# Eligibility status (True/False)
# Discount amount (will be 0 if not eligible)
# Total discounts applied
# Subtotal after discounts
# Tax amount
# Shipping cost with free shipping status (True/False)
# Final total
# # Total amount saved

print(f"Customer name: {name}")
print(f"Membership status: {is_member}")
print("Items bought:")
print(f"{item1}, {price1} sum, {quantity1}")
print(f"{item2}, {price2} sum, {quantity2}")
print(f"{item3}, {price3} sum, {quantity3}")
print(f"Mebership discount eligibility: {member_discount_eligibility}")
print(f"Bulk discount eligibility: {bulk_discount_eligibility}")
print(f"Loyalty discount eligibility: {loyalty_discount_eligibility}")
print(f"Discounts amount: {(bulk_discount+discount+loyalty_discount):.2f} sum")
print(f"Total discounts applied: {member_discount_eligibility+bulk_discount_eligibility+loyalty_discount_eligibility}")
print(f"Subtotal after discounts applied: {total_after_loyalty_discount:.2f} sum")
print(f"Tax amount: {tax_rate:.2f} sum")
print(f"Shipping amount: {shipping} sum")
print(f"Final total: {final_price} sum")
print(f"Total amount saved: {((subtotal+shipping+tax_rate)-final_price):.2f}")
# Member discount: 10% off subtotal (eligible if customer is a member)

# Loyalty discount: 3% off (eligible if total_previous_purchases >= 1000000)
# All discounts stack - apply them sequentially using boolean arithmetic
# Other Calculations:

# Tax rate: 12% applied to subtotal after all discounts
# Shipping: 25000 sum (but 0 if subtotal > 500000)
# Calculate using: shipping = (subtotal <= 500000) * 25000
# Output must show:

