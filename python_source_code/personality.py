#personality/py

#introverted or extroverted checker
def pfunc1():
    #Introverted or Extroverted checker
    while True:
        a=1
        b=2
        ttl=0
    #Chill night or club out
        while True:
                    
            q1=input("\nDo you prefer a chill quiet night or a club nightout for the weekend?\n[a]Quiet Silent\n[b]Club Nightout\n").lower()

            if q1=="a":
                ttl+=a
                break
            elif q1=="b":
                ttl+=b
                break
            elif q1!="a" or q1!="b":
                print("\nInvalid Response")
                         
    #heart of the party or not
        while True:
                    
            q2=input("\nDo you prefer to be the heart of the party?\n[a]No,not really\n[b]Yes,always\n").lower()
            if q2=="a":
                ttl+=a
                break
            elif q2=="b":
                ttl+=b
                break
            elif q2!="a" or q2!="b":
                print("\nInvalid Response")
                        
    #Quarantine easier or not
        while True:
                    
            q3=input("\nDo you find the Covid-19 quarantine easier to handle than most people?\n[a]Yes\n[b]No\n").lower()
            if q3=="a":
                ttl+=a
                break
            elif q3=="b":
                ttl+=b
                break
            elif q3!="a" or q3!="b":
                print("\nInvalid Response")
                        
    #assigns either introverted or extroverted       
        if ttl==5 or ttl==6:
            var="E"
        elif ttl==3 or ttl==4:
            var="I"
   
        return var
        break

#intuitive or observant checker
def pfunc2():
    while True:
        a=1
        b=2
        tt1=0       
    #wonder future or not
        while True:
                    
            q4=input("\nDo you often wonder about the future and possibilities? (like eg.Technology advancements etc)\n[a]Yes\n[b]No\n").lower()

            if q4=="a":
                tt1+=a
                break
            elif q4=="b":
                tt1+=b
                break
            elif q4!="a" or q4!="b":
                print("\nInvalid Response")
                               
        #wonder past or not
        while True:
                    
            q5=input("\nDo you often wonder about the past? (eg.if you have done something differently)\n[a]Yes\n[b]No\n").lower()
            if q5=="a":
                tt1+=a
                break
            elif q5=="b":
                tt1+=b
                break
            elif q5!="a" or q5!="b":
                print("\nInvalid Response")
                        
        #what if
        while True:
                    
            q6=input("\nDo you often wonder of what if situations?\n[a]Yes\n[b]No\n").lower()
            if q6=="a":
                tt1+=a
                break
            elif q6=="b":
                tt1+=b
                break
            elif q6!="a" or q6!="b":
                print("\nInvalid Response")
                        
        #assigns either intituive or observant    
        if tt1==5 or tt1==6:
            var="S"
        elif tt1==3 or tt1==4:
            var="N"

        return var       
        break   

#thinking or feeling checker
def pfunc3():
    while True:
        a=1
        b=2
        ttl=0
                
        #feelings get better off them
        while True:
                    
            q7=input("\nDoes your feelings get the better off you?\n[a]Yes\n[b]No\n").lower()

            if q7=="a":
                ttl+=a
                break
            elif q7=="b":
                ttl+=b
                break
            elif q7!="a" or q7!="b":
                print("\nInvalid Response")
                        
        #follow their heart or brain
        while True:
                    
            q8=input("\nDo you follow your heart or brain\n[a]Heart\n[b]Brain\n").lower()
            if q8=="a":
                ttl+=a
                break
            elif q8=="b":
                ttl+=b
                break
            elif q8!="a" or q8!="b":
                print("\nInvalid Response")
                
                
        #value emotions or rationality
        while True:
                    
            q9=input("\nDo you prefer emotionality or rationality?\n[a]Emotionality\n[b]Rationality\n").lower()
            if q9=="a":
                ttl+=a
                break
            elif q9=="b":
                ttl+=b
                break
            elif q9!="a" or q9!="b":
                print("\nInvalid Response")
                        
        #assigns either intituive or observant    
        if ttl==5 or ttl==6:
            var="T"
        elif ttl==3 or ttl==4:
            var="F"
                    
        return var          
        break

#Judging or Prospecting
def pfunc4():
    while True:
        a=1
        b=2
        ttl=0
        #well planned event or on the spot event
        while True:
                    
            q10=input("\nDo you prefer a well planned vacation or a roughly planned vacation ?\n[a]Well planned vacation\n[b]Roughly planned vacation\n").lower()

            if q10=="a":
                ttl+=a
                break
            elif q10=="b":
                ttl+=b
                break
            elif q10!="a" or q10!="b":
                print("\nInvalid Response")    
                    
        #perform well under pressure
        while True:
                    
            q11=input("\nDo you perform well underpressure?\n[a]No\n[b]Yes\n").lower()
            if q11=="a":
                ttl+=a
                break
            elif q11=="b":
                ttl+=b
                break
            elif q11!="a" or q11!="b":
                print("\nInvalid Response")
                
                
        #easy to stay in one topic or not
        while True:
                    
            q12=input("\nDo you find it easy to stay in one topic or hobby?\n[a]Yes\n[b]No\n").lower()
            if q12=="a":
                ttl+=a
                break
            elif q12=="b":
                ttl+=b
                break
            elif q12!="a" or q12!="b":
                print("\nInvalid Response")
                        
                #assigns either intituive or observant    
        if ttl==5 or ttl==6:
            var="P"
        elif ttl==3 or ttl==4:
            var="J"
                    
        return var
        break

#to give the personality
def pfunc5(a,b,c,d):
    var=a+b+c+d

    return var
   

#check if the user inputted personality is true
def pfunc6():
    list=["intj","intp","entj","entp","infj","infp","enfj","enfp","istj","isfj","estj","esfj","istp","isfp","estp","esfp"]
    while True:
        var=input("\nPlease enter your Personality:\n").lower()

        if var in list:
            print("\nConfirmed! Your Personality is",var,"\nPlease do the other test for more music recommendations.")
            return var
            break
        elif var not in list:
            print("\nInvalid Response. Personality does not exist.\n")





