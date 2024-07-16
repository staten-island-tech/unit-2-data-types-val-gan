def hungerBar():
    maxPoints = int(input("How many hunger points are available?\n"))
    apples = int(input("How many apples will be eaten?\n"))
    seconds = int(input("How many seconds will pass?\n"))
    finalPoints = 0
    if apples < maxPoints:
        finalPoints = apples - seconds
    elif apples > maxPoints:
        finalPoints = maxPoints - seconds
    #finalPoints cannot be negative
    if finalPoints < 0:
        finalPoints = 0
    print(f"You have {finalPoints} remaining hunger points")
    
hungerBar()