from enum import Enum
from datetime import datetime
import time
from getpass import getpass
import pyfiglet
 
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

class Player(Enum):
    self_destruct = 0
    player1 = 1
    player2 = 2

validCards = [e.name for e in Cards]

def isInvalid(card):
    return card not in validCards

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.gameover = False
        self.winner = None
        self.gameCycleCounter = 0

    def startlog(self):
        now = datetime.now()
        dt_string = now.strftime("%m-%d-%Y_%H:%M:%S")

        self.log_file_path = f"gamelogs/{self.player1}_{self.player2}_{dt_string}.txt"
        self.log_file = open(self.log_file_path, "w")
        self.log_file.close()

        print(f"Created a game log at {self.log_file_path}.")

    def fightSimple(self, card1, card2):
        """
        Returns the winner of a fight where no special conditions apply, 
                and you can just compare sizes of the cards
        """
        if (card1.value > card2.value):
            return Player.player1
        elif (card1.value < card2.value):
            return Player.player2
        else:
            return Player.self_destruct

    def fightWithGongBing(self, card1, card2):
        """
        Returns the winner of a fight (@Player) where one of card1/card2 is a gongbing
        """
        if (card1 == Cards.gobi):
            if (card2 == Cards.dile):
                return Player.player1
        else:
            if (card1 == Cards.dile):
                return Player.player2
        
        return self.fightSimple(card1, card2)
    
    def fightWithDiLei(self, card1, card2):
        """
        Returns the winner of a fight when one of card1/card2 is a dilei. One of card1 and card2 must be.
        """
        if (card1 == Cards.dile):
            if (card2 == Cards.gobi):
                return Player.player2
            elif (card2 == Cards.zhda):
                return Player.self_destruct
            else:
                return Player.player1
        else:
            if (card1 == Cards.gobi):
                return Player.player1
            elif (card1 == Cards.zhda):
                return Player.self_destruct
            else:
                return Player.player2
        
    def fightCard(self, card1, card2):

        """
        returns either Player.player1, Player.player2 or Player.self_destruct
        """

        if (card1 == None) or (card2 == None):
            raise ValueError("One of the cards is not right, please try again.")

        if (card1 == Cards.juqi):
            self.gameover = True
            self.winner = self.player2
            return Player.player2
        elif (card2 == Cards.juqi):
            self.gameover = True
            self.winner = self.player1
            return Player.player1
        elif (card1 == card2):
            return Player.self_destruct
        elif (card1 == Cards.zhda) or (card2 == Cards.zhda):
            return Player.self_destruct
        elif (card1 == Cards.dile) or (card2 == Cards.dile):
            return self.fightWithDiLei(card1, card2)
        else:
            ## will only have from gongbing to SiLing left, can do direct compare
            return self.fightSimple(card1, card2)
        
    def playerName(self, player):
        if (player == Player.player1):
            return self.player1
        elif (player == Player.player2):
            return self.player2
        else:
            return "SELF DESTRUCT"
    
    def logFight(self, card1, card2, winner):
        """
        Logs one fight between two cards, recording time, fight#, and winner.
        """

        with open(self.log_file_path, "a") as log:
            log.write(datetime.now().strftime("%m-%d-%Y_%H:%M:%S"))
            log.write(f" Game Fight {self.gameCycleCounter}:\n")
            log.write(f"{self.player1}'s card: {card1.name} \t {self.player2}'s card: {card2.name}\n")
            log.write(f"The winner declared is: {self.playerName(winner)}")
            log.write("\n\n")
    
    def playerWith(self, card, card1, card2):
        """
        card MUST BE one of card1 and card2
        """
        if (card == card1):
            return self.player1
        elif (card == card2):
            return self.player2
        else:
            raise ValueError("Card being compared does not belong to either player1 or player2.")


    def compareAndLog(self, card1, card2):
        
        """
        Transforms card1, card2 from strings to Cards. Then, completes the fight and the logging.
        """

        player1_card = Cards[card1]
        player2_card = Cards[card2]

        winner = self.fightCard(player1_card, player2_card)
        self.gameCycleCounter += 1
        
        self.logFight(player1_card, player2_card, winner)

        return winner

    def endgame(self):
        print(pyfiglet.figlet_format("GAME OVER!"))
        print(pyfiglet.figlet_format(f"{self.winner} wins!"))
        return

    def printWinner(self, winner):
        """
        @param winner: Player
        """
        winnerName = self.playerName(winner)

        print("\n==============================================================")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        print("RESULT:")
        if winnerName == "SELF DESTRUCT":
            print(f"{winnerName}.")
        else:
            print(f"{winnerName} won.")
        print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("==============================================================")

        if self.gameover != True:
            time.sleep(1.5)
        

    def fight(self):
        print("===========================================\n")
        print("Waiting for a fight ... I will be here when you need! \n")
        print("===========================================\n")

        player1_card = getpass(f"{self.player1}'s card (4 letters): ")
        player1_card_is_invalid = isInvalid(player1_card)

        while player1_card_is_invalid:
            print(f"{self.player1}, your card is invalid. Your card must be in the format of one of")
            print(validCards)
            print("\n")
            player1_card = getpass(f"{self.player1}'s card (4 letters): ")
            player1_card_is_invalid = isInvalid(player1_card) 
        print("===========================================\n")

        player2_card = getpass(f"{self.player2}'s card (4 letters): ")
        player2_card_is_invalid = isInvalid(player2_card)

        while player2_card_is_invalid:
            print(f"{self.player2}, your card is invalid. Your card must be in the format of one of")
            print(validCards)
            print("\n")
            player2_card = getpass(f"{self.player2}'s card (4 letters): ")
            player2_card_is_invalid = isInvalid(player2_card) 
        
        print("===========================================\n")
             
        winner = self.compareAndLog(player1_card, player2_card)

        self.printWinner(winner)

        if self.gameover == True:
            return self.endgame()
        else:
            return self.fight()
        

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
    