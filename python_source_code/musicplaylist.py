#final recommendation (musicplaylist.py)
import random

#zodiac final music recommendation
def mfunc1(a):
    list1=["Jeremy Zucher - always I'll care","Harry Styles - Adore you","FINNEAS - Let's Fall in Love for the Night","Yuna - Crush","the surfaces - Sunday Best","Lewis Capaldi - Before yoo go","Honne - Location Unknown(w/Georgia)","Conan Gray - Maniac","1975 - Somebody Else","LANY - Mean It(w/Lauv)",]
    list2=["Billy Eilish - everything i wanted","Lana del Ray - Happiness is a Butterfly","Troy Sivan - Strawherries & Cigarettes","Florence+the machine - Dog Days Are Over","Sia - Eye of the needle","The Killers - Mr.Brightside","Bjork - It's Oh so Quiet","Lorde - Royals","Melanie Martinez - Play Date","Halsey - Without Me"]
    list3=["Miles Davis - So What","John Coltrane - Blue World","Loius Armstrong - What a Wonderful World","Thelonious Monk - Don't Blame Me","Duke Ellington - It Don't Mean A Thing","Billy Holiday - Summertime","Bill Evans - My foolish heart","Charlie Parker - All the things you are","Dave Brubeck - Take Five"]
    list4=["Peterpan - Menghapus Jejakmu","Eraserheads - Ang Huling El Bimbo","Despacito - Luis Fonsi(w/Daddy Yankee)","Meng Ran - Shao Nian","Edith Piaf - La Vie en Rose","Blackpink - Stay","Shuta Sueyoshi - HACK","","Arash - Broken Angel(ft.Helena)","t.A.T.u - Belly Plaschik"]
    list5=["Rich Brian - 100 Degrees","A boogie Wit da Hoodie - Swervin(ft.6ix9ine)","Doja Cat - Cybersex","Lil Wayne - How to love","Tyga - Ayy Macarena)","Travis Scott - Sicko Mode","G-Eazy - Me,Myself & i(w/Bebe RExha)","Wiz Khalifa - See you again(ft.Charlie Puth)","Juice WRLD - Lucid Dreams","21 Savage - a lot"]
    list6=["Taylor Swift - Mean","Dolly Parton - 9 to 5","Kenny Rogers - Island in the Stream","Cassadee Pope - Wasting All These Years","LeAnn Rimes - How Do I live","Kacey Musgraves - Rainbow","Rascal Flatts - Life is A Highway","Carry Underwood - Do you hear what I hear","Brad Paisley - She's Everything","Tim Mcgraw - Humble And Kind"]
    list7=["Beethoven - Fur Elise","Mozart - Allegro","Chopin - Nocturines NO. 9","Claude Debussy - La mer","Bach - Air on the G String","Handel - Water Music","Vivaldi - The Four Seasons","Mahler - Sympony No. 5","Wagner - Ride of the Valkeryries","Haden - Trumpet Concerto"]
    list8=["Ariana Grande - into you","Taylor Swift - You need to calm down","Lady Gaga - Rain on Me","Britney Spears - Give me more","Katy Perry - California girl","Zara Larson - All the time","Bazzi - IFLY","Rihanna - Work","Lauv - Never Not"]
    list9=["Faith Fiance - Tell NoBody","SZA - Love Galore (ft.Travis Scott)","Jhene Aiko - Triggered","Summer Walker - Come Thru","Frank Ocean - White Ferari","Kehlani - Everybody Business","Mariah Carey - Fantasy","Beyonce - Dangerously in love","Victoria Monet - Dive"]
    list10=["Zedd - Happy Now","David Guetta - Titanium(ft.Sia)","Alan Walker - Faded","Avicii - Wake Me Up","Marshmello - Silence(ft.Khalid)","Kygo - Stargazing(w/Justin Jesso)","Jonas Blue - Fast Car(w/Dakato)","Calvin Harris - This is what you came for","Cheat Codes - No Promises(w/Demi Lovato)","Martin Garrix - Scared to Be Lonely(w/Dua Lipa)"]    
    list11=["Westlife - My Love","Trademark - Only love","NSYNC - ByeByeBye","Maroon 5 - She will be played","Taylor Swift - Love Story","Katy Perry - The one who got away","Mariah Carey - Touch my body","Coldplay - Viva La Vida","S Club 7 - Never had a dream come true","One Direction - One Thing"]
    list12=["Green Day - Wake me Up in September","My Chemical Romance - Helena","Evenescence - Bring Me To Life","Bon Jovi - Always","Prince - Purple Rain","Michael Learns to Rock - You Took My Heart Away","Aerosmith - I Don't Want to Miss a Thing","Paramore - Still into you","Coldplay - Fix You","Panic! at the disco - Into the Unknown",]
    
    a=a.lower()

    if a=="pisces":
        var="Indie-"+list1[random.randrange(0,10)]
        return var
    elif a=="aquarius":
        var="Alternative-"+list2[random.randrange(0,10)]
        return var
    elif a=="capricorn":
        var="Jazz-"+list3[random.randrange(0,10)]
        return var
    elif a=="sagittarius":
        var="World Music-"+list4[random.randrange(0,10)]
        return var
    elif a=="scorpio":
        var="HipHop-"+list5[random.randrange(0,10)]
        return var
    elif a=="libra":
        var="Country-"+list6[random.randrange(0,10)]
        return var
    elif a=="virgo":
        var="Classical-"+list7[random.randrange(0,10)]
        return var
    elif a=="leo":
        var="Pop-"+list8[random.randrange(0,10)]
        return var
    elif a=="cancer":
        var="R&B-"+list9[random.randrange(0,10)]
        return var
    elif a=="gemini":
        var="EDM-"+list10[random.randrange(0,10)]
        return var
    elif a=="taurus":
        var="Classics-"+list11[random.randrange(0,10)]
        return var
    elif a=="aries":
        var="Rock-"+list12[random.randrange(0,10)]
        return var
    elif a=="none":
        var="Zodiac Test was not attempted. Please do the test to have this recommendation"
        return var
    else:
        print("Invalid Response")

    
#personality final music recommendation
def mfunc2(a):
    list1=["Green Day - Wake me Up in September","My Chemical Romance - Helena","Evenescence - Bring Me To Life","Bon Jovi - Always","Prince - Purple Rain","Michael Learns to Rock - You Took My Heart Away","Aerosmith - I Don't Want to Miss a Thing","Paramore - Still into you","Coldplay - Fix You","Panic! at the disco - Into the Unknown",]
    list2=["Billy Eilish - everything i wanted","Lana del Ray - Happiness is a Butterfly","Troy Sivan - Strawherries & Cigarettes","Florence+the machine - Dog Days Are Over","Sia - Eye of the needle","The Killers - Mr.Brightside","Bjork - It's Oh so Quiet","Lorde - Royals","Melanie Martinez - Play Date","Halsey - Without Me"]
    list3=["Taylor Swift - Mean","Dolly Parton - 9 to 5","Kenny Rogers - Island in the Stream","Cassadee Pope - Wasting All These Years","LeAnn Rimes - How Do I live","Kacey Musgraves - Rainbow","Rascal Flatts - Life is A Highway","Carry Underwood - Do you hear what I hear","Brad Paisley - She's Everything","Tim Mcgraw - Humble And Kind"]
    list4=["Zedd - Happy Now","David Guetta - Titanium(ft.Sia)","Alan Walker - Faded","Avicii - Wake Me Up","Marshmello - Silence(ft.Khalid)","Kygo - Stargazing(w/Justin Jesso)","Jonas Blue - Fast Car(w/Dakato)","Calvin Harris - This is what you came for","Cheat Codes - No Promises(w/Demi Lovato)","Martin Garrix - Scared to Be Lonely(w/Dua Lipa)"]

    if (a=="intj" or a=="intp" or a=="entj" or a=="entp"):
        var="Analysts(intj,intp,entj,entp) 80% likes Rock-\n"+list1[random.randrange(0,10)]
        return var
    elif (a=="infj" or a=="infp" or a=="enfj" or a=="enfp"):
        var="Diplomats(infj,infp,enfj,enfp) 85% likes Alternative-\n"+list2[random.randrange(0,10)]
        return var
    elif (a=="istj" or a=="isfj" or a=="estj" or a=="esfj"):
        var="Sentinels(istj,isfj,estj,esfj) 64% likes Country-\n"+list3[random.randrange(0,10)]
        return var
    elif (a=="istp" or a=="isfp" or a=="estp" or a=="esfp"):
        var="Explorers(istp,isfp,estp,esfp) 68% likes EDM-\n"+list4[random.randrange(0,10)]
        return var
    elif a=="none":
        var="Personality Test was not attempted. Please do the test to have this recommendation"
        return var
    else:
        print("Invalid response")


    
