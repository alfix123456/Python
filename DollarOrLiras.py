##This Program Gets Dollar and Lira Values and decides which one is better to Bring to Istanbul
print("Dollars or Liras for Istanbul!!!!")
_TotalMoney=float(input("How Much Money Do You have? :"))
_dollarValue=float(input("How much is a Dollar? :"))
_liraValue=float(input("How Much is a Lira? : "))
_LiraExchangeRate=float(input("What Is the Exchange rate for Dollar in Istanbul? :"))

def LiraOrDollar(totalmoney,dollarvalue,liravalue,liraexchange):
    liraCount=totalmoney/liravalue
    dollarCount=totalmoney/dollarvalue
    totalvalueinIstanbul=dollarCount*liraexchange*liravalue
    difference=totalvalueinIstanbul-totalmoney
    return difference

_Difference=LiraOrDollar(_TotalMoney,_dollarValue,_liraValue,_LiraExchangeRate)

if _Difference<0:
    print("You Will Loose",int(_Difference),"If you take Dollar to ISTANBUL!")
else:
    print("You Will earn",int(_Difference),"if you take Dollars to ISTANBUL!")

input("Pres ENTER to Exit!")

##End Of Program
