import csv
import math

data = []

class User:
    def __init__(self, id, monthlyIncome, monthlyCardPayment, carPayment, 
                 loanPayment, homeAppVal, downPayment, loanAmount, mortgage, credit):
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
        data = []
    
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

def createUser(data):
    id = len(data) + 1
    print("Welcome! Your ID # is [" + id + "]")
    monthlyIncome = float(input("Please enter monthly income: "))
    monthlyCardPayment = float(input("Please enter your monthly card payment: "))
    carPayment = float(input("Please enter your monthly car payment: "))
    loanPayment = float(input("Please enter your monthly loan payment: "))
    homeAppVal = float(input("Please enter your home appraisal value: "))
    downPayment = float(input("Please enter your monthly down payment: "))
    loanAmount = float(input("Please enter the loan amount you are taking on your house: "))
    mortgage = float(input("Please enter your monthly mortgage: "))
    credit = int(input("Please enter your credit score: "))
    Buyer = User(id, monthlyIncome, monthlyCardPayment, carPayment, loanPayment, 
                 homeAppVal, downPayment, loanAmount, mortgage, credit)
    return Buyer
    
def lookupUserSample(data):
    u = int(input("Enter authentication ID: ")) - 1
    Buyer = User(int(data[u][0]),float(data[u][1]),float(data[u][2]),float(data[u][3]),float(data[u][4]),
                float(data[u][5]),float(data[u][6]),float(data[u][7]),float(data[u][8]),int(data[u][9]))
    return Buyer

def readFile(data, file):
    file = "HackUTD-2023-HomeBuyerInfo.csv"
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rowIndex = 0
        for row in spamreader:
            if (rowIndex != 0):
                data.append((row[0]).split(','))
            rowIndex += 1

def runCounter(data, file):
    file = "HackUTD-2023-HomeBuyerInfo.csv"
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rowIndex = 0
        for row in spamreader:
            if (rowIndex != 0):
                data.append((row[0]).split(','))
            rowIndex += 1
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    for u in range(10000):
        Buyer = User(int(data[u][0]),float(data[u][1]),float(data[u][2]),float(data[u][3]),float(data[u][4]),
                    float(data[u][5]),float(data[u][6]),float(data[u][7]),float(data[u][8]),int(data[u][9]))
        # run different counters
        counter1 += 1
        counter2 += 1
        counter3 += 1
        counter4 += 1
        del Buyer
    counters = [counter1, counter2, counter3, counter4]

    return counters

useSampleInput = False
askUser = ""
while (askUser != "Y" or askUser != "N"):
    askUser = input("View samples? [Y/N]: ")
    if (askUser == "Y"):
        useSampleInput = True
        readFile(data, "HackUTD-2023-HomeBuyerInfo.csv")
        Buyer = lookupUserSample(data)
        break
    elif (askUser == "N"):
        useSampleInput = False
        Buyer = createUser()
        break
    else:
        print("Please enter valid input!")


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

    