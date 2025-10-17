# Context: You’re creating a rental calculator for a book rental service.

# Categories (membership types):

# student - $2.00 per book
# book_count = int(input("How many books are you getting? "))
# if membership_type== "student":
#     total=book_count*2.00
# elif membership_type=="regular":
#     total=book_count*4.00
# elif membership_type=="premium":
#     total=book_count*6.00
total=0
subtotal=0
print("=== Book Rental System ===")
print("Enter membership type: student, regular, or premium")
print("Type 'done' when finished selecting books")

while True:
    membership_type=input("\nEnter your membership type: ")
    if membership_type== "student":
        subtotal+=2.00
        print("Price: $2.00")
        print(f"Current total: ${subtotal:.2f}")
    elif membership_type== "regular":
        subtotal+=4.00
        print("Price: $4.00")
        print(f"Current total: ${subtotal:.2f}")
    elif membership_type== "premium":
        subtotal+=6.00
        print("Price: $6.00")
        print(f"Current total: ${subtotal:.2f}")
    elif membership_type=="done":
        break
    else:
        print("Please enter the correct command!")
if subtotal>14:
    bulk_discount=2.50
    total=subtotal-bulk_discount
else:
    bulk_discount=0
    total=subtotal
print("\n=== Rental Summary ===")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Bulk discount: -${bulk_discount:.2f}")
print(f"Final total:${total:.2f}")



# regular - $4.00 per book
# premium - $6.00 per book (includes newest releases)
# Stop word: done

# Special offer: If the total is $15.00 or more, apply a $2.50 bulk rental discount.

# Sample interaction:

# === Book Rental System ===
# Enter membership type: student, regular, or premium
# Type 'done' when finished selecting books

# Enter membership type: student
# Price: $2.00
# Current total: $2.00

# Enter membership type: student
# Price: $2.00
# Current total: $4.00

# Enter membership type: regular
# Price: $4.00
# Current total: $8.00

# Enter membership type: premium
# Price: $6.00
# Current total: $14.00

# Enter membership type: student
# Price: $2.00
# Current total: $16.00

# Enter membership type: done

# === Rental Summary ===
# Subtotal: $16.00
# Bulk Rental Discount: -$2.50
# Final Total: $13.50
# Thank you for your rental!