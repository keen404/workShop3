#นาย จิณณะ พันธุมงคล 6806021612053 Sec:C

number = int(input("Enter integer number : "))

oneThousand = number//1000
number = number - (oneThousand*1000)

oneHundred = number//100
number = number - (oneHundred*100)

ten = number//10
number = number - (ten*10)

print(oneThousand)
print(oneHundred)
print(ten)
print(number)

