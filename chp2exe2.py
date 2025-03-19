price_of_item = 100

VAT = (price_of_item)*(15/100)
message = "VAT of item:"

total = (price_of_item) + VAT
message2 = "Total price:"

#f ensures that there is no space between the R and the price
print(message, f"R{VAT}")
print(message2, f"R{total}")
