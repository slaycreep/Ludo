# Ludo
Imagine you are designing a minimalistic version of the game ludo with the following conditions:

a. The player who crosses throughout the board of exactly 25 boxes wins.

b. Each of the players get to roll the dice and can get from 1-6. If a player scores 6, he/she gets another immediate turn. If a player scores 6 three times in a row, all three turns get cancelled and the player stays stationary.

c. If a player crosses 24 boxes, he/she has to get exactly 1 after rolling the dice in order to win. Otherwise, he/she will stay in the same place.

d. The one who gets to the 25th box first will win.

e. Until a winner is decided, the dice will be rolled between the players and the game will continue.

f. If one player gets to a box which is already occupied by another player, the one who occupied the box gets eaten and has to start from box no 1 again.

```
Sample Input #1:
1. Player 1: 5
2. Player 2: 4
3. Player 1: 5
4. Player 2: 5
5. Player 1: 6
6. Player 1: 1
7. Player 2: 4
8. Player 1: 4
9. Player 2: 6
10. Player 2: 6
Output:
Player 2 wins


Sample Input #2:
1. Player 1: 5
2. Player 2: 3
3. Player 1: 5
4. Player 2: 2
5. Player 1: 5
6. Player 2: 4
7. Player 1: 5
8. Player 2: 5
9. Player 1: 3
10. Player 2: 4
11. Player 1: 5
12. Player 2: 4
13. Player 1: 1
14. Player 2: 6
15. Player 1: 3
16. Player 2: 4
17. Player 1: 1
Output:
Player 1 wins
Sample Input #3:
1. Player 1: 2
2. Player 2: 3
3. Player 1: 6
4. Player 1: 6
5. Player 1: 6
6. Player 2: 3
7. Player 1: 5
8. Player 2: 3
9. Player 1: 5
10. Player 2: 6
11. Player 2: 6
12. Player 2: 4
Output:
Player 2 wins
[Hint: Player 1 hits 3 6s
in a row and therefore
his turn gets cancelled
and he stays stationary]


Sample Input #4:
1. Player 1: 4
2. Player 2: 5
3. Player 1: 4
4. Player 2: 5
5. Player 1: 4
6. Player 2: 5
7. Player 1: 4
8. Player 2: 5
9. Player 1: 4
10. Player 2: 5
11. Player 1: 4
12. Player 2: 5
```
13. Player 1: 1
Output:
Player 1 wins
[Hint: Player 2 gets
eaten in turn no 9 and
starts from box 1 again]
