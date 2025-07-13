#นาย จิณณะ พันธุมงคล 6806021612053 Sec:C

netPriceProduct = int(input("Enter net price product : "))

priceProduct = netPriceProduct * (100 / 107)
vat = netPriceProduct * (7 / 107)

print()
print("Price product: ", round(priceProduct, 2))
print("Vat product: ", round(vat, 2))