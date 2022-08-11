#PRATICAL3
#hii

print("Enter the Purchase amount:")
amount=int(input("Enter the Purchase amount:"))
if amount <= 1000:
    discount=int(1000*5)/100
    print("Discount amount:",discount)
elif amount >= 10000:
    discount=int(1000*10)/100
    print("Discount amount:",discount)
else:
    print("No discount for you")
