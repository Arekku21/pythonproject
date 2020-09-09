#Zodiac.py

#function for returning zodiac sign
def zfunc1(var,var2):
    if var=="april":
        a="aries" if (var2 < 20) else "taurus"
                        
    elif var=="may":
        a="taurus" if (var2 < 21) else "gemini"
                        
    elif var=="june":
        a="gemini" if (var2 < 21) else "cancer"
                        
    elif var=="july":
        a="cancer" if (var2 < 23) else "leo"
                        
    elif var=="august":
        a="leo" if (var2 < 23) else "virgo"
                        
    elif var=="september":
        a="virgo" if (var2 < 23) else "libra"
                        
    elif var=="october":
        a="libra" if (var2< 23) else "scorpio"
                        
    elif var=="november":
        a="scorpio" if (var2 < 22) else "sagittarius"
                        
    elif var=="december":
        a="sagittarius" if (var2 < 22) else "capricorn"
                        
    elif var=="january":
        a="capricorn" if (var2 < 20) else "aquarius"
                        
    elif var=="february":
        a="aquarius" if (var2 < 19) else "pisces"
                        
    elif var=="march":
        a="pisces" if (var2 < 21) else "aries"
    return a

#day format checker
def zfunc2():
    while True:
        var=input("Please input your birthday: \n")
    #isnumeric checks if all charaters in a variable are numeric chracters  
        if var.isnumeric()==True:
            var=int(var)
    #a nested if to check day is allowed
            if var<32:
                return var
                break
            else:
                print("Your inputted birth-day is invalid.Please try again")

        elif var.isnumeric()==False:
            print("\nYour inputted birth-day is invalid.Please try again\n")

#month format checker
def zfunc3():
    list=["january","february","march","april","may","june","july","august","september","october","november","december"]
    while True:
        var=input("\nPlease input your birthmonth: \n").lower()
        if var in list:
            return var
            break
        elif var not in list:
            print("\nYour inputted birth-month is invalid.Please Try Again.\n")

#zodiac checker for user inputed zodiac
def zfunc4():
    list=["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
    while True:
        var=input("\nPlease enter your zodiac sign: \n").lower()

        if var in list:
            print("\nConfirmed! Your Zodiac Sign is",var,"\nPlease do the other test for more music recommendations.")
            return var
            break
        elif var not in list:
            print("\nInvalid Response. Zodiac does not exist.\n")

            
