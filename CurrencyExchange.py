print("Currency Exchange Application")
def Currency_Exchange(_rate,_euro):
    _dollars=_euro*_rate
    return _dollars
_r=input("Enter the Amount of Euros: ")
_e=input("Enter the Exchnage Rate: ")
_amount=Currency_Exchange(float(_r),float(_e))
print("You have",_r,"Euros equal to",_amount,"Dollars.")
