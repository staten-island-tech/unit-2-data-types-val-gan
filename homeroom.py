#program 1
def homeroom1():
    lastName = input("Input your last name to find your homeroom\n")
    firstInitial = lastName[0]
    homeroom = 0
    if firstInitial.upper() == "A":
        homeroom = 101
    elif firstInitial.upper() == "B":
        homeroom = 102
    else:
        homeroom = 103
    print(f"You are in homeroom {homeroom}")

homeroom1()

#program 2
def homeroom2():
    lastName = input("Input your last name to find your homeroom\n")
    firstInitial = str(lastName[0])
    homeroom = 0
    initialsList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    loopCount = 0
    for i in initialsList:
        if firstInitial.upper() == i:
            if loopCount < 7:
                homeroom = 101
                break
            elif loopCount < 16:
                homeroom = 102
                break
            else:
                homeroom = 103
                break
        loopCount += 1
    print(f"You are in homeroom {homeroom}")

homeroom2()