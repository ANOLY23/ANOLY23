
import time

#The function below checks if there are still available spaces to be played in.
def empty(list_):
    for item in list_:
        if "_" in item:
            return False
    else: 
        return True
    return False
#The function below checks if a player has won.


def iswon(subject, listt):
    
    #The function below caters for horizontal matching. 
    def func(rr, y, list__):
        if list__[0][y] == list__[1][y] == list__[2][y]== rr:
            return True
        else:
            return False
        
    #The function below caters for row or vertical matching.
    def func2 (aa, list_):
        for row in list_:
            if all(i == aa for i in row):
                return True
        return False
    
    #The function below caters for diagonal or cross-wise matching. 
    def diagonal(ss,lis):
        if lis[0][0] == lis[1][1] == lis[2][2] == ss:
            return True
        if lis[0][2] == lis[1][1] == lis[2][0] == ss:
            return True
    list_ = (0,1,2)
    
    #The following code merges all the functions such that any case where True, the player wins.
    if func2(subject, listt) == True or any(func(subject,x, listt) == True for x in list_ ) or diagonal(subject, listt):
        return True
    else:
        return False
    
    
def intelligence(mylist, user, com):
   
    def smart2(listt, xx):
        #Vertical checking
        slist = [0,1,2]
        f1 = (listt[0]).index(xx) if xx in listt[0] else 5
        f2 = (listt[1]).index(xx) if xx in listt[1] else 5
        f3 = (listt[2]).index(xx) if xx in listt[2] else 5
        if f1==f2 and f1 in slist:
            return [2,f1]
        elif f1==f3 and f1 in slist:
            return [1,f3]
        elif f2==f3 and f2 in slist:
            return [0,f2]
        else:
            return 0
    def smart3(listt, xx):
        #Forward Diagonal checking
        f1 = listt[0][0]
        f2 = listt[1][1] 
        f3 = listt[2][2]
        if f1 == f2 == xx:
            return [2,2]
        elif f1 == f3 == xx:
            return [1,1]
        elif f3 == f2 == xx:
            return [0,0]
        else:
            return 0
    def smart4(listt, xx):
        #Backward Diagonal checking
        f1 = listt[0][2]
        f2 = listt[1][1] 
        f3 = listt[2][0]
        if f1 == f2 == xx:
            return [2,0]
        elif f1 == f3 == xx:
            return [1,1]
        elif f3 == f2 == xx:
            return [0,2]
        else:
            return 0
    def smart(listt, xx):
        #Horizontal checking
        test = list(listt)
        for item in test:
            if item.count(xx) == 2:
                #Amy
                count= test.count(item)
                if count == 1:
                    if "_" in item:
                        bb = item.index("_") 
                        aa = test.index(item)
                        return [aa,bb]
                    else:
                        continue
                else:
                    return 0
        else:
            return 0

    intlist =  [smart(mylist, user), smart2(mylist, user), smart3(mylist, user), smart4(mylist, user)]
    intlist2 = [smart(mylist, com), smart2(mylist, com),smart3(mylist, com), smart4(mylist,com)]
    for x in intlist2:
        print (f"2 {x}")
    count_1 = 0
    for x in intlist2:
        print (x)
        if type(x) == list and mylist[x[0]][x[1]] == "_":
            count_1 += 1
            continue
    if count_1 > 0:
        for x in intlist2:
            if type(x) == list and mylist[x[0]][x[1]] == "_":
                print(x)
                return x
    elif count_1==0:
        count = 0
        for y in intlist:
            print (y)
            if type(y) == list and mylist[y[0]][y[1]] == "_":
                count += 1
                continue
        if count > 1:
            print("You gat me! You're smart.")
            time.sleep(2)
            for y in intlist:
                if type(y) == list and mylist[y[0]][y[1]] == "_":
                    return y
            else:
                return 0
        else:
            for y in intlist:
                if type(y) == list and mylist[y[0]][y[1]] == "_":
                    return y
            else:
                return 0
            
    



#This is the main function for the progress of the game.
def playnow(xx):
    #The following code confirms a value, X or O for the computer.
    time.sleep(1)
    print("Play by inputing the row and column number of your move.")
    time.sleep(1)
    #B
    print("GOOD LUCK!")
    time.sleep(1)
    print("\n...and the game BEGINS!")
    time.sleep(2)
    comp= "O"
    if xx== "O":
        comp ="X"
    ticlist= [["_","_","_"], ["_","_","_"], ["_","_","_"]]
    #This function prints the display of the game in an orderly arrangement.
    def print_():
        print("\n")
        for item in ticlist:
            print("  {0} {1} {2} ".format(item[0], item[1], item[2]))
                
        
    print_()
    #The loop below progresses the game, but breaks when 'empty' returns true or when any player wins.
    while True:
        #This variable is needed to break the outer while loop.
        det = 0
        while True:
            try:
                x,y= [int(input("Row ")), int(input("Column "))]
                if ticlist[(x-1)][y-1] == "_":
                    ticlist[(x-1)][y-1] = xx
                else:
                    raise ValueError
            except:
                print("Invalid move")
                continue
            else:
                break
        
        
        print_()
        if not iswon(xx, ticlist):
        
            import random
            #The following loop helps the computer play only in a place that is empty for playing.
            while True:
                a = random.randint(1,3)
                b = random.randint(1,3)
                compchoose = ticlist[a-1][b-1]
                if compchoose == "_":
                   
                    brtlist = intelligence(ticlist, xx, comp)
                    if brtlist != 0:
                        #A
                        r = brtlist[0]
                        s = brtlist[1]
                        if ticlist[r][s] == "_":
                            ticlist[r][s] = comp
                        else:
                            ticlist[a-1][b-1] = comp
                    else:
                        ticlist[a-1][b-1] = comp
                    
                    if iswon(comp, ticlist):
                        print_()
                        print("You Lose")
                        det = 1
                        time.sleep(1)
                        input1 = input("Do you want to play again?\nYes or No? ")
                        if input1.lower() == "yes":
                            send()
                        else:
                            if input1.lower() != "no":
                            	print("Invalid input")
                            time.sleep(2)
                            print("Thank you for playing this game.")
                    break
                else:
                    if empty(ticlist) == True:
                        time.sleep(1)
                        print("\nGame Over")
                        time.sleep(1)
                        input1 = input("Do you want to play again?\nYes or No? ")
                        if input1.lower() == "yes":
                            send()
                        else: 
                            if input1.lower() != "no":
                                print("Invalid input.")
                                time.sleep(2)
                            print("Thank you for playing this game.")
            
                        det = 1
                        break
                    elif empty(ticlist) == False:
                        continue
                       
            if det == 1:
                break    
            print_()
        else:
            print("You Won!")
            time.sleep(1)
            input1 = input("Do you want to play again?\nYes or No? ")
            if input1.lower() == "yes":
                send()
            else: 
                if input1.lower() != "no":
                    print("Invalid input.")
                    time.sleep(2)
                print("Thank you for playing this game.")
            break
        
#This is the initial function which collects user input and calls the inner functions.            
def play(x):
    if x== 0:
        print("Coward!")
    elif x== 1:
        print("Great!")
        time.sleep(1)
        print("ANO~LY is ready to play too!")
        time.sleep(1)
        while True:
            try:
                XO= input("Are you X or O? ").lower()
                if XO != "x" and XO != "o":
                    raise ValueError
            except ValueError:
                continue
            else:
                playnow(XO.upper())
                break
    elif x=="2":
        print("!!!!! Input yes or no")
        send()
        
dict_rez= {"yes":1,
           "no" : 0}



def send():
    print("\n#####                                 ######\n##### Welcome to ANO~LY's TIC TAC TOE ######\n#####                                 ######")
    print("...")
    time.sleep(1)
    input_= input("Are you ready to play? ").lower()
    value = dict_rez.get(input_,"2")
    play(value)

#The calling of the first operation starts here.
send()



            
            

    