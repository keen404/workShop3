#นาย จิณณะ พันธุมงคล 6806021612053 Sec:C

amount = int(input("Enter amount : "))
rate = float(input("Enter rate : ")) / 100
year = int(input("Enter year : "))

futureValue = amount * (1 + rate) ** year

print("Future value =", futureValue)
