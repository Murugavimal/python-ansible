
from Rbi import RBI

class SBI(RBI):
    def kyc(self):
        print("KYC done at SBI")
    def deposit(self):
        print("deposited in SBI")
    def withdraw(self):
        print("withdraw in SBI")


sbi= SBI()
sbi.deposit()
sbi.kyc()
sbi.withdraw()

