#accounts[i][j]
#i: amount of money per one customer (COLUMN). add together all values within i to get total
#j: which bank (ROW)

def maxBankAccount(accounts):
    totalsList = []
    for i in accounts:
        total = 0
        for n in i:
            total += n
        totalsList.append(total)
    print(totalsList)
    max = 0
    maxAccount = 0
    i = 0
    while i != len(totalsList)-1:
        if totalsList[i] > totalsList[i+1]:
            max = totalsList[i]
            maxAccount = i+1
        elif totalsList[i+1] > max:
            max = totalsList[i+1]
            maxAccount = i+2
        i += 1

    print(f"Customer #{maxAccount} (index {i}) is the wealthiest, with a value of {max} in their account.")

maxBankAccount(([1,5,9,10], [7,3,2], [3,5,20]))
        