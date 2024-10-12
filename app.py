player1 = [] #to store values of player 1
player2 = [] #to store values of player 2

while True: #running infinity loop
    inp1 = int(input("Player 1: ")) #player 1 input
    while inp1<=0 or inp1>6: #invalid input condition
      print("Invalid input. Enter again.")
      inp1 = int(input("Player 1: ")) #taking input of player 1 again
    if sum(player1)+inp1 <= 25: #value storing in list player 1 condition
        player1.append(inp1)
    
    while player1[-1] == 6 and sum(player1) != 25: #getting 6 as step condition
        inp1 = int(input("Player 1: "))
        player1.append(inp1)
        if len(player1) >= 3: #getting triple 6 condition
            if player1[-3:] == [6,6,6]:
                player1 = player1[:-3] #not storing the values 
                break #breaking the loop
    if sum(player1) == 25: #player 1 winning conditon
        print("Player 1 wins")
        break

    if sum(player1) == sum(player2): #eating player 2 condition
        player2 = []


    inp2 = int(input("Player 2: ")) #player 2 input
    while inp2<=0 or inp2>6: #invalid input condition
      print("Invalid input. Enter again.")
      inp2 = int(input("Player 2: ")) #taking input of player 1 again
    if sum(player2) + inp2 <= 25:
        player2.append(inp2) #value storing in list player 1 condition
    
    while player2[-1] == 6  and sum(player2) != 25: #getting 6 as step condition
        inp2 = int(input("Player 2: "))
        player2.append(inp2)
        if len(player2) >= 3: #getting triple 6 condition
            if player2[-3:] == [6, 6, 6]:
                player2 = player2[:-3] #not storing the values
                break #breaking the loop

    if sum(player2) == 25: #player 2 winning conditon
        print("Player 2 wins")
        break

    if sum(player2) == sum(player1): #eating player 1 condition
        player1 = []
