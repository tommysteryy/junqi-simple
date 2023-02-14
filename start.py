import sys
from enum import Enum
from datetime import datetime
 
class Cards(Enum):
    juqi = -1
    gobi = 1
    pazh = 2
    lizh = 3
    yizh = 4
    tuzh = 5
    lvzh = 6
    shzh = 7
    juzh = 8
    sili = 9
    zhda = 10
    dile = 11

validCards = [e.name for e in Cards]

def isInvalid(card):
    return card not in validCards

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.gameover = False

    def startlog(self):
        now = datetime.now()
        dt_string = now.strftime("%m-%d-%Y_%H:%M:%S")

        self.log_file_path = f"gamelogs/{self.player1}_{self.player2}_{dt_string}"
        self.log_file = open(self.log_file_path, "w")
        self.log_file.close()

        print(f"Created a game log at {self.log_file_path}.")
    
    def compare(self, card1, card2):
        return "Did the compare"
    
    def logFight(self, card1, card2, largerCard):
        return "Did the logging"

    def compareAndLog(self, card1, card2):
        largerCard = self.compare(card1, card2)
        self.logFight(card1, card2, largerCard)


    def fight(self):
        print("===========================================\n")
        print("Waiting for a fight ... I will be here when you need! \n")

        player1_card = input(f"{self.player1}'s card (4 letters): ")
        player1_card_is_invalid = isInvalid(player1_card)

        while player1_card_is_invalid:
            print(f"{self.player1}, your card is invalid. Your card must be in the format of one of")
            print(validCards)
            player1_card = input(f"{self.player1}'s card (4 letters): ")
            player1_card_is_invalid = isInvalid(player1_card) 
        

        player2_card = input(f"{self.player2}'s card (4 letters): ")
        player2_card_is_invalid = isInvalid(player2_card)

        while player2_card_is_invalid:
            print(f"{self.player2}, your card is invalid. Your card must be in the format of one of")
            print(validCards)
            player2_card = input(f"{self.player2}'s card (4 letters): ")
            player2_card_is_invalid = isInvalid(player2_card) 
             
        self.compareAndLog(player1_card, player2_card)


                


        
        


# # total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)
 
# # Arguments passed
# print("\nName of Python script:", sys.argv[0])
 
# print("\nArguments passed:", end = " ")
# for i in range(1, n):
#     print(sys.argv[i], end = " ")
     
# # Addition of numbers
# Sum = 0
# # Using argparse module
# for i in range(1, n):
#     Sum += int(sys.argv[i])
     
# print("\n\nResult:", Sum)

def game_init():
    p1 = input("What is the first player's name? \n")
    p2 = input("Okay, what about the second player? \n")
    game = Game(p1, p2)
    print(f"Created a new junqi game with {p1} and {p2}")
    return game
    




if __name__ == "__main__":
    game = game_init()
    game.startlog()
    game.fight()
    