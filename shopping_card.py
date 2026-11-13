customer_name=input("Enter customer name:")

product_name1=input("Enter product name:")

product_price1=float(input("Enter product price:"))

product_name2=input("Enter product name:")
product_price2=float(input("Enter product price:"))

product_name3=input("Enter product name:")
product_price3=float(input("Enter product price:"))

Subtotal=product_price1+product_price2+product_price3

if(Subtotal>=5000):
    Discount_rate = "20"
elif Subtotal>=3000: 
    Discount_rate ="10"
else:
    Discount_rate="0"

Discount=Subtotal*Discount_rate/100

Total=Subtotal-Discount

print(f"customer_name:{customer_name}")

print(f"products:{product_price1},{product_price2},{product_price3}")

print(f"Subtotal:{Subtotal}")
print(f"Discount({Discount_rate}%):{Discount}")

print(f"Total:{Total}")
