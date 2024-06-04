import math


def findFactorsandSqrt(numberX):

    if numberX % 2 == 0:
        print(f"{numberX} is an EVEN NUMBER !")

    sqrtX = math.isqrt(numberX)

    if sqrtX * sqrtX != numberX:
        print(f"{numberX} does not have a perfect square root.")

    else:
        print(f"{numberX} has a perfect root which is {sqrtX}")

    factors = []

    for i in range(1, math.isqrt(numberX) + 1): # 35 4.666 = 5 6
        if numberX % i == 0:
            factors.append(i)
            if i != numberX:
                factors.append(numberX // i)

        factors.sort()

    print(f"The factors of {numberX} are {factors}")


done = False


while done == False:

    numberX = int(input("Please enter a whole number: "))
    input(f"\nThe number you entered is {numberX}")
    findFactorsandSqrt(numberX)
    user_response = (
        input("Do you want to enter another number? (yes/no): ").strip().lower()
    )
    if user_response != "yes":
        done = True
