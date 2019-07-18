def help1():
    print()
    print()
    print("Welcome to Help Section of tic-tac-toe game ")
    print("Please wait Strategies is loading..." )
    import time
    for i in range(7):
        print('loading...')
        time.sleep(1)
    print()
    print()
    print()
    print("Strategies of tic-tac-toe games :   ")
    print("1)  Win: If the player has two in a row, they can place a third to get three in a row.")
    print("2)  Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.")
    print("3)  Fork: Create an opportunity where the player has two threats to win (two non-blocked lines of 2).")
    print("4)  Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it.")
    print("    Otherwise, the player should block any forks in any way that simultaneously allows them to create two in a row.")
    print("    Otherwise, the player should create a two in a row to force the opponent into defending, as long as it doesn't result in them creating a fork.")
    print("    For example, if 'X' has two opposite corners and 'O' has the center, 'O' must not play a corner in order to win. (Playing a corner in this scenario creates a fork for 'X' to win.)")
    print("5)  Center: A player marks the center. (If it is the first move of the game, playing on a corner gives the second player more opportunities to make a mistake")
    print("    and may therefore be the better choice; however, it makes no difference between perfect players.)")
    print("6)  Opposite corner: If the opponent is in the corner, the player plays the opposite corner.")
    print("7)  Empty corner: The player plays in a corner square.")
    print("8)  Empty side: The player plays in a middle square on any of the 4 sides.")
    print()
    print()
    print("1) Exit")
    print("2) Play Game")
    p=int(input("Please choose any one of the option    "))
    if p==1:
        Exit()
    elif p==2:
        playgame()
    else:
        print("Wrong key is pressed")
        print()
        exit(0)
def Contact_us():  
    print("THE TIC-TAC-TOE GAME")
    print("Contact Us")
    print()
    print()
    print()
    print("Name : Maaz Mohammed")
    print("Enrolment no. : BT18GCS105")
    print("Section : S3")
    print("Email Id : maaz.mohammed18@st.niituniversity.in")
    print("Mobile : 9811259816")
    print()
    print()
    print("1) Exit")
    print("2) Play Game")
    print("3) Help")
    print("Please choose one of the options    ")
    u=int(input())
    if u==1:
        Exit()
    elif u==2:
        playgame()
    elif u==3:
        help1()
    else:
        print("You pressed the wrong key")
        print()
def Exit():
    print("Thanks for playing!!!")
    print("Press Y key to exit")
    print("Or press N to play more")
    a=input("Please type a character according to your choice     ")
    if a=='Y' or a=='y':
        playgame()
    elif a=='n' or a== 'N':
        exit(0)
    else:
        print("you type the wrong key")
        exit(0)
def playgame():
    a=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    print()
    print("Welcome to tic-tac-toe game")
    print("Please wait game is loding")
    import time
    for i in range(10):
        print("Loading...")
        time.sleep(0.5)
    print("Please write the name of first player")
    player_1=input()
    print("Please write the name of second ")
    player_2=input()
    import random
    b=random.choice([1,2])
    if b==1:
        print(player_1," is player 1 ")
    elif b==2:
        print(player_2," is player 1 ")
    print("Please select your symbol (x,o)  ")
    b1=input("Player 1 choose  ")
    b2=input("Player 2 choose  ")
    if (b2==b1):
        if(b1=='o'):
            print("Player already taken o")
            print("your symbol is x")
            b2='x'
        elif(b2=='x'):
            print("Player already taken x")
            print("your symbol is o")
            b2='o'
    print()
    print()
    time.sleep(6)
    print("Please remember the number and their arrangement")
    print()
    print()
    print("|---|---|---|")
    print("| 1 | 2 | 3 |")
    print("|---|---|---|")
    print("| 4 | 5 | 6 |")
    print("|---|---|---|")
    print("| 7 | 8 | 9 |")
    print("|---|---|---|")
    print()
    print()
    print("Followings no. will be used in the game.")
    print("If a person select 1 then his symbol will be saved to left-top corner area")
    print()
    print()
    print("Lets start game in : ")
    for i in range(1,4):
        print(i)
        time.sleep(1)
    print()
    print()
    print()
    for i in range(1,5):
        print("Player 1 please choose where you want to place your symbol")
        c1=[]
        c1.append(input())
        print("Player 2 please choose where you want to place your symbol")
        c2=[]
        c2.append(input())
    print("Player 1 please choose where you want to place your symbol")
    c1=[]
    c1.append(input())
    if (1 in c1) and (2 in c1) and (3 in c1):
        print("Player 1 wins the game...")
    elif (1 in c1) and (4 in c1) and (7 in c1):
        print("Player 1 wins the game...")
    elif (4 in c1) and (5 in c1) and (6 in c1):
        print("Player 1 wins the game...")
    elif (2 in c1) and (5 in c1) and (8 in c1):
        print("Player 1 wins the game...")
    elif (7 in c1) and (8 in c1) and (9 in c1):
        print("Player 1 wins the game...")
    elif (3 in c1) and (6 in c1) and (6 in c1):
        print("Player 1 wins the game...")
    elif (1 in c1) and (5 in c1) and (9 in c1):
        print("Player 1 wins the game...")
    elif (3 in c1) and (5 in c1) and (7 in c1):
        print("Player 1 wins the game...")
    elif (1 in c2) and (2 in c2) and (3 in c2):
        print("Player 2 wins the game...")
    elif (1 in c2) and (4 in c2) and (7 in c2):
        print("Player 2 wins the game...")
    elif (4 in c2) and (5 in c2) and (6 in c2):
        print("Player 2 wins the game...")
    elif (2 in c2) and (5 in c2) and (8 in c2):
        print("Player 2 wins the game...")
    elif (7 in c2) and (8 in c2) and (9 in c2):
        print("Player 2 wins the game...")
    elif (3 in c2) and (6 in c2) and (6 in c2):
        print("Player 2 wins the game...")
    elif (1 in c2) and (5 in c2) and (9 in c2):
        print("Player 2 wins the game...")
    elif (3 in c2) and (5 in c2) and (7 in c2):
        print("Player 2 wins the game...")
    else:
        print('Draw')
    print()
    print()
    print()
    print(" Enter  any key to exit")
    m=input()
    exit(0)

print()
print()
print()
print("The tic-tac-toe game")
print("   -Maaz Mohammed")
print()
print()
print()
print("MENU")
print()
print("1) Play Game ")
print("2) Help")
print("3) Contact Us")
print("4) Exit")
print()
print("please choose a option   ")
q=int(input())
if q==1:
    playgame()
elif q==2:
    help1()
elif q==3:
    Contact_us()
elif q==4:
    Exit() 
    
    
