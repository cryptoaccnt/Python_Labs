balance = 2250
interestRate = .045
term = 120


x = 1
while x < term + 1:
    interest = balance * interestRate/12
    balance = balance + interest
    print("Month", x, "\t Interest:  $ %.2f" "\t Balance:  $ %.2f" %(interest, balance))
    x = x + 1

