#second form of calculating to bring Dollars or Liras to Istanbul
print("Dollars Or Liras!")
dollarValue=float(input("How Much is a Dollar?"))
liraValue=float(input("how much is a Lira?"))
exchangeRate=float(input("What is the Exchange rate?"))

def USDorTL(TLval,exRate):
    trTLval=exRate*TLval
    return trTLval

if USDorTL(liraValue,exchangeRate)<dollarValue:
    print("Bring Liras!")
else:
    print("Bring Dollars!")

input("Pres ENTER to Exit!")
