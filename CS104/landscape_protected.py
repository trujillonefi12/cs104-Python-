import math


credentials = {}

fh = open("authorized_users.txt", "r")

data = fh.readline()

information = data.split(",")


credentials["username"] = information[0]
credentials["password"] = information[1]
credentials["lvl"] = information[2]

authorized = False


while authorized == False:

    promptUsername = input("User Name: ")
    promptPass = input("Password: ")

    if (
        promptUsername == credentials["username"]
        and promptPass == credentials["password"]
    ):
        authorized = True
    else:
        print("Invalid credentials, please try again.")


##
# try:
#    file = open('Macintosh HD/Users/nefijeremiastrujilloarita/Downloads/authorized_users.txt', 'r')
# except FileNotFoundError:
#    print('Error: The file "authorized_users.txt" was not found.')
# authorize = False

lenght1 = int(input("What is the length of the front section? "))

width1 = int(input("What is the width of the front section? "))

lenght2 = int(input("What is the length of the rear section? "))

width2 = int(input("What is the width of the rear section? "))

lenghtl3 = int(input("What is the length of the left section? "))

widthl3 = int(input("What is the width of the left section? "))

lenghtw4 = int(input("What is the length of the right section? "))

widhtw4 = int(input("What is the width of the right section? "))


area = (
    (lenght1 * width1)
    + (lenght2 * width2)
    + (lenghtl3 * widthl3)
    + (lenghtw4 * widhtw4)
)

bagsNeeded = math.ceil(area / 2000)

costOfFertilizer = bagsNeeded * 27

hoursofWorkNeeded = math.ceil(area / 2500)

costofLabor = hoursofWorkNeeded * 20

nitrogen = (area / 2000) * 1

potassium = (area / 2000) * 0.125

totalCost = costOfFertilizer + costofLabor


print(
    f"Your application has a total area of {area} sq. feet. That will require {bagsNeeded} bags of fertilizer "
    f"${costOfFertilizer}. Our technicians will require {hoursofWorkNeeded} hours to finish the job and "
    f"the labor cost will be ${costofLabor}. The total cost to the company will be ${totalCost}. The application will result "
    f"in {nitrogen} pounds of nitrogen and {potassium} pounds of potassium being added to the soil."
)
