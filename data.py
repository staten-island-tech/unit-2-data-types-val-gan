bill = 0
tip = 0
total = 0

bill = float(input('How much is the bill?\n'))
tip = float(input('How much is the tip?\n'))
total = str(bill + tip)

print("Your total is " + total)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) 
 

x = "this is a thing"

#y is a list of the separate words in the x string
y = x.split()

#z is the first element in the list y
z = y[0]

print(y)
print(z)

 
#create a variable for the user input
#use the split function with an empty space to separate the words
#print the length of the list of words

def wordCount():
    sentence = input('Input a sentence.\n')
    list = sentence.split(" ")
    print(list)
    print(len(list))

wordCount() 

def madLibs():
    noun = input('Type a noun\n')
    verb = input('Type a verb\n')
    adjective = input('Type an adjective\n')
    pluralNoun = input('Type a plural noun\n')
    print('Once upon a time, there was a beautiful ' + noun + ' who loved to ' + verb + '.')
    print('This upsetted the kingdom of the ' + pluralNoun + ' because it was banned in their country to ' + verb)
    print('Nonetheless, our ' + noun + ' paid no mind and lived happily ever after')
madLibs() 

def oddOrEven():
    num = int(input('Input an integer\n'))
    if (num%2) == 0:
        print('This is an even number')
    else:
        print('This is an odd number')

oddOrEven() 

def tipPercent():
    text = input("Rate today's service as either bad, okay, good, or great.\n")
    rating = text.casefold()
    print(rating)
    if rating == "bad":
        print("Tip 0%")
    elif rating == "okay":
        print("Tip 15%")
    elif rating == "good":
        print("Tip 20%")
    elif rating == "great":
        print("Tip 25%")

tipPercent() 

def findFactors():
    num = int(input("Input a number to find its factors\n"))
    factors = []
    for i in range (1, num):
        if (num % i) == 0:
            factors.append(i)
        i += 1
    print(factors)

findFactors()
 

def GCF(num1, num2):
    factors1 = []
    factors2 = []

    # factors list for num1
    for i in range (1, num1 + 1):
        if (num1 % i) == 0:
            factors1.append(i)
    # factors list num2
    for i in range (1, num2 + 1):
        if (num2 % i) == 0:
            factors2.append(i)
    #find shorter list to avoid out of range error during loop
    if num1 < num2:
        shorter = factors1
        longer = factors2
    else:
        shorter = factors2
        longer = factors1

    #last items in factor lists
    i = len(shorter) - 1
    n = len(longer) - 1
    while i > -1:
        while n > -1:
            if shorter[i] == longer[n]:
                print(f"GCF: {shorter[i]}")
                quit() #this stops the code at the GCF, otherwise it would run through all of the common factors
            n -= 1
        n = len(longer) - 1
        i -= 1

GCF(2,10)