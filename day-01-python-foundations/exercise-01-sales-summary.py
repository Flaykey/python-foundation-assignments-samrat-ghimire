product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

gross_price = unit_price * quantity_sold
discount = discount_percentage * gross_price
final_sale = gross_price -  discount

print(f"Product: {product_name}\nGross: NPR {gross_price }\nDiscount: NPR {discount}\nFinal Sales: NPR {final_sale}")