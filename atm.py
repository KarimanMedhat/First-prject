#This is atm project
user = "u"
while user == "u":
    print("Enter the amount that you want to withdraw: ")
    amount = int(input())
    if amount % 1 == 0:
        twoHundreds = (amount // 200)
        print(str(twoHundreds) + "--->" + "200 EG")
        hundred = ((amount % 200) % 200) // 100
        print(str(hundred) + "--->" + "100 EG")
        fifties = (((amount % 200) % 200) % 100) // 50
        print(str(fifties) + "--->" + "50 EG")
        twenties = ((((amount % 200) % 200) % 100) % 50) // 20
        print(str(twenties) + "--->" + "20 EG")
        tens = (((((amount % 200) % 200) % 100) % 50) % 20) // 10
        print(str(tens) + "--->" + "10 EG")
        fifePounds = ((((((amount % 200) % 200) % 100) % 50) % 20) % 10) // 5
        print(str(fifePounds) + "--->" + "5 EG")
        pounds = (((((((amount % 200) % 200) % 100) % 50) % 20) % 10) % 5) // 1
        print(str(pounds) + "--->" + "1 EG")
        print("Thank you. Would you like to do another withdrawal?")
        print("Yes : u")
        print("No : press any key")
        choice = input()
        print("Goodbye")
    else:
        print("The denominations you entered are not available.")
