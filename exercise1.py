#นาย จิณณะ พันธุมงคล 6806021612053 Sec:C
#Workshop 3_1

withDrawMoney = int(input("Enter number money withdraw : "))

oneThousandBaht = withDrawMoney//1000
withDrawMoney = withDrawMoney - (oneThousandBaht*1000)

fiveHundredBaht = withDrawMoney//500
withDrawMoney = withDrawMoney - (fiveHundredBaht*500)

oneHundredBaht = withDrawMoney//100
withDrawMoney = withDrawMoney - (oneHundredBaht*100)

print("Cash B1000:", oneThousandBaht)
print("Cash B500:", fiveHundredBaht)
print("Cash B100:", oneHundredBaht)

