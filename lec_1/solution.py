#write your answer here
number = int(input("Enter your number: "))
count = 0
while (number>0):
    number = number//10
    count = count+1
print('Number of digits:', count)

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input('Enter a number: '))
print(factorial(n))
    if n==str:
print('Not a valid input'.isalpha())


Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
brand=[Computers["Laptop1"]["brand"],Computers["Laptop2"]["brand"],Computers["Desktop"]["brand"]]
OS=[Computers["Laptop1"]["OS"],Computers["Laptop2"]["OS"],Computers["Desktop"]["OS"]]
print(brand)
print(OS)

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):



            
            
     tasks = []

def displayTasks(all_tasks):
    print('\nYour tasks: ')
    for index, task in enumerate(all_tasks):
        print(f'{index+1}: {task}')         


def newOperation(all_tasks):
    operation = input("Press 'A' to add a new task,'E' to edit a task, 'S' to search a task, 'R' to remove a task or 'F' to quit: ")

    if operation == 'A':
        addTask(all_tasks)
    elif operation == 'S':
        pass
    elif operation == 'E':
        editTask(all_tasks)
    elif operation == 'R':
        removeTask(all_tasks) 
    elif operation == 'F':
        return
    else:
        newOperation(all_tasks)      

def editTask(all_tasks):
    task_number = input('Enter the number of the task you want to edit: ')

    new_task = input('Edit task: ')
    all_tasks[int(task_number)-1] = new_task

    print(f'Item {task_number} edited!')

    displayTasks(all_tasks)
    newOperation(all_tasks)

def removeTask(all_tasks):
    task_number= input('Enter the number of the task you want ot remove: ')

    all_tasks.remove(all_tasks[int(task_number)-1])

    print(f'\nItem {task_number} removed!')

    displayTasks(all_tasks)
    newOperation(all_tasks)



def addTask(all_tasks):
    new_task = input('Add a task: ')
    all_tasks.append(new_task)

    for task in all_tasks:
        print(task)


    newOperation(all_tasks)

addTask(tasks) 

def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 

def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
def check_win(player_pos, cur_player):
 
    
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
   
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            return True
       
    return False       
 

def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 

def single_game(cur_player):
 
    
    values = [' ' for x in range(9)]
     
    
    player_pos = {'X':[], 'O':[]}
     
    
    while True:
        print_tic_tac_toe(values)
         
        
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        
 
       
        values[move-1] = cur_player
 
       
        player_pos[cur_player].append(move)
 

        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
     
   
    cur_player = player1
 
    
    player_choice = {'X' : "", 'O' : ""}
 
    
    options = ['X', 'O']
 
   
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
   
    while True:
 
       
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
       
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        
        winner = single_game(options[choice-1])
         
        
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1       
            
            
            t = target - num
            if t in d:
                return [d[t], i]
            d[num] = i
        return [] 
