#mohamad farhan bin ismail
#20ddt19f1085

#soalan1a
squ = range(0 , 11)

for x in squ:
    square = x**2
    print("The square of ",str(x)," is: ",str(square))
#soalan1b
print("The total of even number from 0 to 10 is ",str(square))

#soalan2
while True:
    name = input("Please enter your username: ")
    if name.isalpha():
        break
    print("your username must all contain alphabetical only")

def validate():
    while True:
        password = input("Please enter the password: ")
        if len(password) < 5:
            print("your Make sure your password is at lest 5 letters")
        elif not password.isdigit():
            print("your password need to contain at least numeric only")
        else:
            print("password seems fine")
            break

validate()

#soalan3

carprice = 103300
tenPer = 0.1 * carprice


downpay = int(input("Please inter your Downpayment: "))
years = int(input("Please inter your loan period in year: "))

if downpay >= tenPer:
    loanAmount = carprice - downpay
    totalInterest = ((2.7/100) * loanAmount * years)
    monthlyInstall = ((loanAmount + totalInterest) / (years * 12))
    print("you need to pay RM ",float(monthlyInstall),"as your monthly installment.")
else:
    print("you are no eligible for a bank loan")