print("APR Calculator")
print("How much money is owed for a loan of $1k with 5%APR over 10 years")
years = 10
loan = 1000
loanOG = loan
APR = .05
for i in range(years):
    loan += loan * APR
    print("Year " + str(i + 1) + " is" + f'{loan: .2f}')

print()
print("You paid " + f'{(loan - loanOG): .2f}' + " in interest!")
