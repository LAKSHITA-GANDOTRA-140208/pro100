class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    
    def cashWidhrawl(self):
      print("your cash is withdrawed")
    
    def balanceEnquiry(self):
       print("check your balance")

object=Atm("xxx","xxx")
object.cashWidhrawl()
object.balanceEnquiry()
    