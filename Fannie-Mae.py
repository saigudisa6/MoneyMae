import math

class User:
    def __init__(self, id, monthlyIncome, monthlyCardPayment, carPayment, loanPayment, homeAppVal, downPayment, loanAmount, mortgage, credit):
        self.id = id
        self.monthlyIncome = monthlyIncome
        self.monthlyCardPayment = monthlyCardPayment
        self.carPayment = carPayment
        self.loanPayment = loanPayment
        self.homeAppVal = homeAppVal
        self.downPayment = downPayment
        self.loanAmount = loanAmount
        self.mortgage = mortgage
        self.credit = credit
    
    def evalCreditScore(self):
        if (self.credit >= 640):
            return True # good
        else:
            return False # not good
    
    def calcPMI(self):
        return self.homeAppVal * 0.01

    def calcLTV(self):
        return ((self.loanAmount) / self.homeAppVal) * 100
    
    

def evalLTV(LTV):
    if (LTV < 80):
        return True # good
    if (LTV >= 80):
        return False # cause for concern
        
def evalFEDTI(FEDTI):
    if (FEDTI <= 28):
        return True # good
    else:
        return False # not good
        
def calcMonthlyDebt(carPayment, loanPayment, mortgage, monthlyCardPayment, PMI):
    monthlyDebt = carPayment + loanPayment + mortgage + PMI + monthlyCardPayment
    return monthlyDebt
    
def calcDTI(monthlyDebt, monthlyIncome):
    return (math.floor(monthlyDebt / monthlyIncome * 100))

def calcFEDTI(mortgage, monthlyIncome, PMI):
    return ((mortgage + PMI) / monthlyIncome * 100)




Buyer = User(1,3103.00,317.00,374.00,250.00,268468.00,32216.16,236251.84,1127.90,778)
# validate creditScore
checkScore = Buyer.evalCreditScore()
if (checkScore == False):
    print('Your credit score is low, you should improve it.')
else:
    print('Your credit score is good!')

# validate LTV
LTV = Buyer.calcLTV()
percLTV = evalLTV(LTV)
if (percLTV == False):
    PMI = Buyer.calcPMI()
    print('Your LTV is high, so you will need to get PMI')
else:
    PMI = 0
    print('Your LTV is good!')

# validate DTI
monthlyDebt = calcMonthlyDebt(Buyer.carPayment, Buyer.loanPayment, Buyer.mortgage, Buyer.monthlyCardPayment, PMI)
DTI = calcDTI(monthlyDebt, Buyer.monthlyIncome)

if (DTI <= 36):
    print('DTI is good')
else:
    print('DTI is bad')
    
# validate FEDTI

FEDTI = calcFEDTI(Buyer.mortgage, Buyer.monthlyIncome, PMI)
percFEDTI = evalFEDTI(FEDTI)

if (percFEDTI == False):
    print('FEDTI is bad')
else:
    print('FEDTI is good')