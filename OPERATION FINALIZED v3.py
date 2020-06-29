#APPENDIX - OTHER DEFINITIONS
        
def checkpw(pw): #check if password has met the conditions for operation 6
    smallletter=0
    bigletter=0
    number=0
    for i in pw:
        if i>="a" and i<="z": #min 1 small letter
            smallletter+=1
        elif i>="A" and i<="Z": #min 1 capital letter
            bigletter+=1
        elif i>="0" and i<="9": #min 1 number
            number+=1
    if smallletter>0 and bigletter>0 and number>0 and len(pw)>=6 and len(pw)<=12:
         return True
    else:
         print("\nPlease read the requirements!")
    return False
    
#Necessary importation
import math
from decimal import *
from time import *
import turtle

#1. opening of files

try:
    worlddata=open('WorldPopulationData2019.txt', 'r')
except FileNotFoundError:
    print("Invalid file. Please try again.")
try:
    form=open('Feedback.txt','a+')
except FileNotFoundError:
    print("Invalid file. Please try again.")

#2 classification of most data
Hi=worlddata.read()             #extract the whole text from txt
Lines=list(Hi.split("\n"))      #converts each country into list
no1=Lines.pop(0)                #remove 1st line
no2=Lines.pop(0)                #remove 2nd line
data=[ ]

for i in Lines:
    category=list(i.split('; '))    #'category' was categorised based on countries
    dictionary=[{'Rank': category[0],
          'Country': category[1],
          '2018': int(category[2]),
          '2019': int(category[3]),
          '% share': category[4],
          'Pop change': category[5],
          '% change': category[6],
          'continent': category[7]}] #countries further divided into subgroups forming dictionary
    data.extend(dictionary)

continents ={'Asia':0,
           'North America':0,
           'South America':0,
           'Africa':0,
           'Europe':0,
           'Oceania':0} #for accumulation of the population for each continent for operation 1

for j in data:
        if j['continent'] in continents.keys():
            continents[j['continent']]+=j['2019']

percent=[]
for i in data:
    L=[[i['Country'], int(i['2019']), float(i['% change'])]]
    percent.extend(L)

nonpercent=[]
for i in data:
    L=[[i['Country'], int(i['2018']), float(i['% change'])]]
    nonpercent.extend(L)

for a in range(len(percent)-1): #sorting by the percentage change in descending order for operation 2 and operation 3
    swapped = False
    for i in range(len(percent)-a-1):
        if percent[i][2]<percent[i+1][2]:
            temp = percent[i]
            percent[i] = percent[i+1]
            percent[i+1] = temp
            swapped = True
    if not swapped:
        break;
    
#3 operation 1
def contperc(continents,data): #provides a list of continents and population
    print("{:^20s}|{:^20s}".format("Continent", "Population"))
    print("------------------------------------------")
    for key,value in continents.items():
        print("{:^20s}|{:^20.0f}".format(key,value))

    a=continents["Asia"]
    b=continents["North America"]
    c=continents["South America"]
    d=continents["Africa"]
    e=continents["Europe"]
    f=continents["Oceania"]
    total=a+b+c+d+e+f

    myTurtle=turtle.Turtle()
    window=turtle.Screen()
    
    def fill(b): #Routine rocedures to create pie chart
        myTurtle.begin_fill()
        myTurtle.left(180)
        myTurtle.forward(100)
        myTurtle.left(90)
        myTurtle.circle(100,360*(b/total))
        myTurtle.left(90)
        myTurtle.forward(100)
        myTurtle.end_fill()

    window.setup(width=625, height=600) #create window
    window.title('Pie Chart Continents')
    myTurtle.speed(10000) #high turtle speed
    myTurtle.hideturtle()   

    myTurtle.color('sky blue') #create piechart
    fill(a)

    myTurtle.color('pink')
    fill(b)

    myTurtle.color('pale Goldenrod')
    fill(c)

    myTurtle.color('plum')
    fill(d)

    myTurtle.color('wheat')
    fill(e)

    myTurtle.color('pale green')
    fill(f)

    myTurtle.penup()
    myTurtle.backward(130)
    myTurtle.right(90)
    myTurtle.circle(130,180*(a/total))
    myTurtle.color('black')
    myTurtle.write("{:^5.2f}%\n{:^4s}".format(100*(a/total),"Asia")) #labelling
    myTurtle.circle(150,180*((a+b)/total))
    myTurtle.write("{:^5.2f}%\n{:^13s}".format(100*(b/total),"North America"))
    myTurtle.circle(150,180*((c+b)/total))
    myTurtle.write("{:^5.2f}%\n{:^13s}".format(100*(c/total), "South America"))
    myTurtle.circle(150,180*((c+d)/total))
    myTurtle.write("{:^5.2f}%\n{:^6s}".format(100*(d/total),"Africa"))
    myTurtle.circle(150,180*((e+d)/total))
    myTurtle.write("{:^5.2f}%\n{:^6s}".format(100*(e/total),"Europe"))
    myTurtle.circle(150,180*((e+f)/total))
    myTurtle.write("{:^5.2f}%\n{:^6s}".format(100*(f/total),"Oceania"))

    h=input('Enter to clear.')
    window.clearscreen()

#4 operation 2
def bottomfew(percent):
    print("\n{:^40s}|{:^20s}|{:^20s}".format("Countries", "2019 population", "% change"))
    print("------------------------------------------------------------------------------")
    for i in percent:
        print("{:^40s}|{:^20d}|{:^20.2f}".format(i[0],i[1],i[2]))

    while True:
        try:
            n=int(input("\nSelect how many countries you want to show with greatest negative change (between 2 and 15: ")) #prompt user to enter a number
            if n<2 or n>15:
                raise ZeroDivisionError
            break
        except ValueError: #error handling
            print("Please insert an integer, not string/float")
        except ZeroDivisionError:
            print("Please insert an integer between 2 and 15.")
            continue

    print("\n{:^7s}|{:^40s}|{:^20s}|{:^20s}".format("Ref","Countries", "2019 population", "% change"))
    print("--------------------------------------------------------------------------------")
    for i in range(-1,-n-1,-1):
        print("{:^7s}|{:^40s}|{:^20d}|{:^20.2f}".format(percent[i][0][:3],percent[i][0],percent[i][1],percent[i][2]))
    
    myTurtle=turtle.Turtle() #turtle setup
    window=turtle.Screen() #windown setup
    window.setup(width=625, height=600)
    window.title('Largest Decrease In Population')
    myTurtle.speed(10000)
    myTurtle.hideturtle()

    myTurtle.penup()#draws x-axis
    myTurtle.goto((-1250/4)+50,-250)
    myTurtle.pendown()
    myTurtle.color('black')

    bottomten=percent[-1:-n-1:-1]
    country=[]
    values=[]
    for i in bottomten:
       country.append(i[0])
       values.append(i[2])

    for i in range(0,n): 
        
        myTurtle.forward(25)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.penup()
        myTurtle.forward(15)
        myTurtle.left(90)
        myTurtle.backward(15)
        myTurtle.pendown()
        myTurtle.write("{:<10s}".format(country[i][:3]))
        myTurtle.penup()
        myTurtle.forward(15)
        myTurtle.right(90)
        myTurtle.backward(25)
        myTurtle.left(90)
        myTurtle.pendown()

    myTurtle.penup()#draws y-axis
    myTurtle.goto((-1250/4)+50,-250)
    myTurtle.pendown()
    myTurtle.color('black')
    z=1
    myTurtle.left(90)
    while z<=15:
        myTurtle.forward(25)
        myTurtle.left(90)
        myTurtle.forward(10)
        myTurtle.penup()
        myTurtle.forward(15)
        myTurtle.pendown()
        myTurtle.write(z*-0.25)
        myTurtle.penup()
        myTurtle.backward(25)
        myTurtle.pendown()
        myTurtle.right(90)
        z+=1

    myTurtle.penup()
    myTurtle.goto((-1250/4)+75,-250)
    myTurtle.pendown()
    myTurtle.color('red')

    for i in range(0,n): #draws line graph
        a=values[i]/(-0.25)*25
        b=50*i
        if i==0:
            myTurtle.penup()
            myTurtle.forward(a)
            myTurtle.pendown()
        else:
            myTurtle.goto((-1250/4)+75+b/2,-250+a)
    h=input('Enter to clear.')
    window.clearscreen()

#5 operation 3 (top n population with largest increase in 2019)
def yearpop(percent):
    while True:
        try:
            m=int(input("\nHow many countries do you want to know (between 2 and 15? ")) #input number of countries
            if m<2 or m>15:
                raise ZeroDivisionError
            break
        except ValueError: #error handling
            print("Please insert an integer, not string/float")
        except ZeroDivisionError:
            print("Please insert an integer between 2 and 15.")
            continue
    top=[]
    for j in range(0,m):
            L=[percent[j]]
            top.extend(L)
    print("\n")
    print("{:^7s} | {:^40s} | {:^10s}".format("Ref","Country","% change"))
    print("-------------------------------------------------------------------")
    for i in top:
        print("{:^7s} | {:^40s} | {:^10.2f}".format(i[0][:3],i[0],i[2]))

    myTurtle=turtle.Turtle()
    window=turtle.Screen()
    window.setup(width=625, height=600)
    window.title('Bar graph on largest increase countries')
    myTurtle.speed(10000)
    myTurtle.hideturtle()

    myTurtle.penup()#draws x-axis
    myTurtle.goto((-1250/4)+50,-250)
    myTurtle.pendown()
    myTurtle.color('black')

    topten=percent[0:m]
    country=[]
    values=[]
    for i in topten:
       country.append(i[0])
       values.append(i[2])

    for i in range(0,m): 
        
        myTurtle.forward(25)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.penup()
        myTurtle.forward(15)
        myTurtle.left(90)
        myTurtle.backward(15)
        myTurtle.pendown()
        myTurtle.write("{:<10s}".format(top[i][0][:3]))
        myTurtle.penup()
        myTurtle.forward(15)
        myTurtle.right(90)
        myTurtle.backward(25)
        myTurtle.left(90)
        myTurtle.pendown()

    myTurtle.penup()#draws y-axis
    myTurtle.goto((-1250/4)+50,-250)
    myTurtle.pendown()
    myTurtle.color('black')
    z=1
    myTurtle.left(90)
    myTurtle.showturtle()
    myTurtle.speed(10)
    while z<=20:
        myTurtle.forward(25)
        myTurtle.left(90)
        myTurtle.forward(10)
        myTurtle.penup()
        myTurtle.forward(15)
        myTurtle.pendown()
        myTurtle.write(z*0.25)
        myTurtle.penup()
        myTurtle.backward(25)
        myTurtle.pendown()
        myTurtle.right(90)
        z+=1

    myTurtle.penup()
    myTurtle.goto((-1250/4)+50+12.5,-250)
    myTurtle.pendown()
    colours=['red','dark red','orange','yellow','green'
             ,'blue','navy blue','lavender','purple',
            'violet','indigo','pink', 'beige', 'brown', 'black']


    for i in range(0,m): #draws bar graph
        a=top[i][2]/(0.25)*25
        myTurtle.color('black',colours[i])
        myTurtle.begin_fill()
        myTurtle.forward(a)
        myTurtle.right(90)
        myTurtle.forward(25)
        myTurtle.right(90)
        myTurtle.forward(a)
        myTurtle.end_fill()
        myTurtle.color('black')
        myTurtle.left(180)
    h=input('Enter to clear.')
    window.clearscreen()


#6 operation 4 - Search For country

def search(data):    
    k=0
    while True:
        while True:
            try:
                search=input("Search for country initials: ").upper()
                if len(search)>1 or len(search)<1:
                    raise TypeError
                elif not(search>='A' and search<='Z'):
                    raise TypeError
                break

            except TypeError:
                print("Must be a letter!")
        print("{:<5s}{:<40s}{:<10s}{:<10s}{:<8s}{:<12s}{:<10s}{:<8s}"
                      .format('Rank','Country','2018','2019','% share','Pop change',
                              '% change', 'continent'))
        for i in range(0, len(data)):
            if search in data[i]['Country']:
                print("{:<5s}{:<40s}{:<10d}{:<10d}{:<8s}{:<12s}{:<10s}{:<10s}"
                      .format(data[i]['Rank'],data[i]['Country'], data[i]['2018'],
                              data[i]['2019'],data[i]['% share'],data[i]['Pop change']
                              ,data[i]['% change'],data[i]['continent']))
                k+=1
        if k==0:
            print("No results found")
        enter=str(input("\n\n\nType 'cont' to continue, type anything to go back to menu. "))
        if enter=='cont':
            continue
        else:
            break
        

#7 Operation 5 - Feedback
def feeeedback(form):
    name=input("Name: ") #input name
    feedback=input("Feedback: ") #input feedback
    print("{:^20s}|\t{:<50s}".format(name, feedback), file=form)

    print("\nThank you for your feedback. Have a nice day!")

#8 Operation 6 - See Feedback

def seefeedback(form):
    while True:
        try:
            password=open('Password.txt', 'r')
            break
        except FileNotFoundError:
            try:
                password=open('Password.txt', 'w')
                while True:
                    passwords=input("Create a Password with these criteria:\n 1. between 6 and 12 char\n 2. min 1 small leter, 1 capital letter and 1 number\n\n Password: ")
                    cpass=input("Confirmation Password:")
                    yes=checkpw(passwords)
                    if passwords==cpass and yes==True:
                        password.write(passwords)
                        break
            except FileNotFoundError:
                print("Sorry, there's an unexpected problem")
    passworder=password.read()

    for a in range(0,5):
        cpass=input("Password: ")
        if cpass==passworder:
            try:
                form=open('Feedback.txt','r')
            except FileNotFoundError:
                print("404 File not found")
            for a in form:
                print(a)
            break
        else:
            print("Invalid Password.")
            continue
    password.close()

#MAIN MENU
while True:
    print("\n\nWelcome to the CountryStats!")
    sleep(1.2)
    print("1. Population of Continents\n2. Countries with largest decrease\n3. Top countries with largest increase\n4. Search for countries/letter\n5. Feedback\n6. Download feedback (Only authorised personel. Please restart the program.)\n7. Exit")
    while True:
        try:
            nooo=int(input("\nWhat would you like to do? "))
            if nooo<1 or nooo>8:
                raise ZeroDivisionError
            break
        except ValueError:
            print("Please enter an integer instead of string.")
        except ZeroDivisionError:
            print("Please insert an integer between 1 and 8.")
            
    if nooo==1:
        contperc(continents,data)
    elif nooo==2:
        bottomfew(percent)
    elif nooo==3:
        yearpop(percent)
    elif nooo==4:
        search(data)
    elif nooo==5:
        feeeedback(form)
    elif nooo==6:
        seefeedback(form)
    else:
        break


worlddata.close()
form.close()
exit()
