#main py file (Ongaku.py)
import Zodiac
import personality
import recommendation
import musicplaylist
from tkinter import *
#1st variable for zodiac sign (user's zodiac sign)
while True:
    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome To Ongaku Music Recommendation Program (version 1.0.0)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        checker1=input("Are u continuing user or a new user ?\n[a]New User\n[b]Continuing User\n").lower()
        
        if checker1=="a":
            zod1="none"
            day=0
            month=0
            menu_check=0
            username="none"
            email_check=0
            email="none"
            email_reason="none"
            iecheck=""
            nscheck=""
            tfcheck=""
            jpcheck=""
            total=0
            pvalue="none"
            g1="none"
            g2="none"
            g3="none"
            g4="none"
            g5="none"
            g6="none"
            g7="none"
            g8="none"
            g9="none"
            g10="none"
            g11="none"
            g12="none"
            zmusic="none"
            pmusic="none"
            totalie=0
            totalns=0
            totaltf=0
            totaljp=0
            break
        elif checker1=="b":
            txt1=open("storage.txt","r")
            txthold=txt1.read()
            txthold=txthold.split("///")
            email=txthold[0]
            username=txthold[1]
            email_reason=txthold[2]
            zod1=txthold[3]
            pvalue=txthold[4]
            zmusic=txthold[5]
            pmusic=txthold[6]
            txt1.close()
            day=0
            month=0
            menu_check=0
            email_check=0
            iecheck=""
            nscheck=""
            tfcheck=""
            jpcheck=""
            total=0
            g1="none"
            g2="none"
            g3="none"
            g4="none"
            g5="none"
            g6="none"
            g7="none"
            g8="none"
            g9="none"
            g10="none"
            g11="none"
            g12="none"
            totalie=0
            totalns=0
            totaltf=0
            totaljp=0
            break
            
        
        else:
            print("\nInvalid response")
    
        
    while True:
        
        
        
        #This is the inital user interface due for GUI design
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome To Ongaku Music Recommendation Program (version 1.0.0)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("")
        while True:
            
        #This is the variable to store their username (Use this as the username in the txt file receipt later)
            username=input("\nWhat is your desired username(a chance to change if you are a continuing user)?\n").lower()

            if username=="":
                print("Username cannot be left empty.")
            elif username!="":
                break

        while True:
            #This is to check if they want to give their contact
            email_check=input("\nWould you like to give us your contact detail (Email) for further contact(a chance to change if you are a continuing user)?\n[Y]es or [N]o\n").lower()

            if email_check=="y":
                #email 

                while True:
                    email=input("\nWhat is your email(a chance to change if you are a continuing user)? (Only accepts:Gmail,Yahoo mail or hotmailor Swinburne Email)\n")

                    if ("@gmail.com" or "@yahoo.com" or "@hotmail.com" or "@swinburne.edu.my" or "students.swinburne.edu.my") in email:
                        break
                    
                    elif ("@gmail.com" or "@yahoo.com" or "@hotmail.com" or "@swinburne.edu.my" or "students.swinburne.edu.my") not in email:
                        print("Invalid Email Address. Must be the accepted emails.")                    
                break 
            
            elif email_check=="n":
                #asking why not
                email_reason=input("\nPlease provide a reason(a chance to change if you are a continuing user):\n")

                if email_reason=="":
                    print("Reason can not be left empty")
                elif email_reason!="":
                    break

            elif email_check!="y" and email_check!="n":
                print("\nInvalid Response. Please reply either [Y]es or [N]o\n")
              
                
        
        
        #This is the menu checker for which test do they want first
        while  True:
            menu_check=input("\nWhich test would you like to do ?\n[Z]odiac Test\nZ[o]diac Info\n[P]ersonality Test\n[G]enre Test\n[F]inal Recommendation\n\n[D]eveloper Mode(Access to storage)\n[Q]uit\n").lower()

            if menu_check=="z": #Zodiac Option
                while True:
                    a=input("Do you know your zodiac?\n[Y]es or [N]o\n").lower()

                    if a=="y":
                        #a function to user input your known zodiac
                        zod1=Zodiac.zfunc4()

                        break
                    elif a=="n":
                        print("\nWe will begin your Zodiac Test now\n")


                        #a function to check the day
                        day=Zodiac.zfunc2()

                        #a function to check if the month exists
                        month=Zodiac.zfunc3()                   

                        #zodiac checker function
                        zod1=Zodiac.zfunc1(month,day)
                        
                        print("\nConfirmed! Your Zodiac sign is :",zod1,"\nPlease do the other test for more music recommendations.")                                

                        break
                    
                    elif a!="y" and a!="n":
                        print("Invalid response")
                        
                    break
            elif menu_check=="p": #Personality Option

                while True:
                    b=input("Do you know your personality (based on 16 personality theory?\n[Y]es\n[N]o\n").lower()

                    if b=="y":
                        
                        pvalue=personality.pfunc6()
                        print("\nConfirmed! Your Personality is",pvalue,"Please do the other tests for more music recommendations.")
                        break

                    elif b=="n":
                        
                        #Introverted or Extroverted checker
                        iecheck=personality.pfunc1()

                        #intuitive or observant checker
                        nscheck=personality.pfunc2()            

                        #thinking or feeling checker
                        tfcheck=personality.pfunc3()
                
                        #Judging or Prospecting checker
                        jpcheck=personality.pfunc4()

                        #actual personality       
                        pvalue=personality.pfunc5(iecheck,nscheck,tfcheck,jpcheck).lower()

                        print("\nConfirmed! Your Personality is",pvalue,"Please do the other tests for more music recommendations.")
                        break

                    elif b!="y" and b!="n":
                        print("Invalid response")
                    
                    break

                
            elif menu_check=="g": #Genre Option
                while True:
                    while True:
                        c=input("Which Genre do you want to get a recommendation?\n[a]R&B\n[b]Pop\n[c]Rap\n[d]HipHop\n[e]Blues\n[f]Rock & Roll\n[g]EDM\n[h]alternative\n[i]Indie\n[j]Country\n[k]Soul\n[l]Japanese songs\n\n[Q]Back to menu\n").lower()
                        
                        if c=="a":
                            #R&B
                            g1=recommendation.rfunc1()
                            print("Confirmed! Genre recommendation recorded.")
                        
                        elif c=="b":
                            #Pop
                            g2=recommendation.rfunc2()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="c":
                            #Rap
                            g3=recommendation.rfunc3()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="d":
                            #HipHop
                            g4=recommendation.rfunc4()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="e":
                            #Blues
                            g5=recommendation.rfunc5()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="f":
                            #Rock n Roll
                            g6=recommendation.rfunc6()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="g":
                            #EDM
                            g7=recommendation.rfunc7()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="h":
                            #alternative
                            g8=recommendation.rfunc8()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="i":
                            #indie
                            g9=recommendation.rfunc9()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="j":
                            #country
                            g10=recommendation.rfunc10()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="k":
                            #Soul
                            g11=recommendation.rfunc11()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="l":
                            #Japanese songs
                            g12=recommendation.rfunc12()
                            print("Confirmed! Genre recommendation recorded.")
                            
                        elif c=="q":
                            #back to menu
                            break
                        
                        else:
                            print("Invalid response")
                        
                    break
            elif menu_check=="f":
                while True:
                    while True:
                        d=input("\nWhich results for Music Recommendation do you want to check?\n[a]Zodiac\n[b]Personality\n[c]Genre\n\n[q]Back to menu\n").lower()

                        if d=="a":
                            #zodiac music final
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Music Recommnedation as a",zod1,"is:")
                            zmusic=musicplaylist.mfunc1(zod1)
                            print(zmusic)
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")  
                            
                        elif d=="b":
                            #16 personality final
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Music Recommnedation as a",pvalue,"is:")
                            pmusic=musicplaylist.mfunc2(pvalue)
                            print(pmusic)
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                            
                        elif d=="c":
                            #Genre recommendation final
                            if g1=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("R&B Genre recommendation test was not attempted.\nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g1!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g1)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g2=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Pop Genre recommendation test was not attempted.\nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g2!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g2)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g3=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Rap Genre recommendation test was not attempted.\nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g3!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g3)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g4=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Hip Hop Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g4!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g4)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g5=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Blues Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g5!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g5)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g6=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Rock & Roll Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g6!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g6)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g7=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("EDM Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g7!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g7)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g8=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Alternative Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g8!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g8)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g9=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Indie Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g9!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g9)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g10=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Country Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g10!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Country Test:",g10)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g11=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Soul Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g11!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g11)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                            if g12=="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Japanese Songs Genre recommendation test was not attempted. \nPlease do the test to have this recommendation")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            elif g12!="none":
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Genre Test:",g12)
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

           
                        elif d=="q":
                            #back to main menu
                            break
                        
                        else:
                            #error message
                            print("Invalid Response")
                            
                    break

                
            elif menu_check=="d":
                while True:
                    e=input("\nEnter developer access code: \n")

                    if e=="error404":
                        txtrd=open("storage.txt","r")
                        print("\nLast User Entry")
                        print("--------------------------------------------------------------------")
                        print(txtrd.read())
                        print("--------------------------------------------------------------------")
                        txtrd.close()
                        break
                    
                    else:
                        print("Wrong access code.")
                        break

            elif menu_check=="q":
                txtwr=open("storage.txt","w")
                txtactual="\n"+email+"///"+username+"///"+email_reason+"///"+zod1+"///"+pvalue+"///"+zmusic+"///"+pmusic+"\n"
                txtwr.write(txtactual)
                txtwr.close()
                
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Thank You for using Ongaku Music Recommendation Program version 1.0.0.\nPlease come again.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

            elif menu_check=="o":
                while True:
                    f=input("Are u sure you want this option?\n(This option will cause you to manually close the window to go back to the menu)\n[a]Yes,I agree with the terms & conditions\n[b]No,I dont agree.Back to menu\n")   

                    if f=="a":
                        def click():
                            entered_text = textentry.get()
                            output.delete(0.0, END)
                            try:
                                definition = my_zodiac[entered_text.lower()]
                            except:
                                definition = "Invalid Response.Zodiac does not exist."
                            output.insert(END,definition)

                        window = Tk()
                        window.title("Zodiac Information")
                        window.configure(background="black")

                        photo1 = PhotoImage(file="zod.gif")
                        Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=W)

                        Label (window, text = "Enter the zodiac name: ", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

                        textentry = Entry(window, width=20, bg="white")
                        textentry.grid(row=2, column=0, sticky=W)

                        Button(window, text="Submit", width=6, command=click) .grid(row=3, column=0, sticky=W)

                        Label (window, text = "Details: ", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

                        output = Text(window, width=40, height=6, wrap=WORD, background="White")
                        output.grid(row=5, column=0, columnspan=2,sticky=W)

                        my_zodiac = {
                            'aries':'Date: 21 March –20 April',
                            'taurus':'Date: 21 April - 20 May',
                            'gemini':'Date: 21 May - 20 June',
                            'cancer': 'Date: 21 June - 22 July',
                            'leo': 'Date: 23 July - 22 August',
                            'virgo':'Date: 16 Sept - 15 Oct',
                            'libra':'Date: 16 Oct - 14 Nov',
                            'scorpio':'Date: 15 Nov - 14 Dec',
                            'sagittarius':'Date: 15 Dec - Jan 13',
                            'capricorn':'Date: 14 Jan - 12 Feb',
                            'aquarius':'Date: 13 Feb - 12 Mar',
                            'pisces':'Date: 13 March - 12 April'
                            }
                        window.mainloop()
                        break
 
                    elif f=="b":
                        break
                    else:
                        print("\nInvalid Response\n")
                    break
                
            elif menu_check!="z" and menu_check!="p" and menu_check!="a":
                print("Invalid Response")
                
        break
    break
                
                
