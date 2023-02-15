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

    def startlog(self):
        now = datetime.now()
        dt_string = now.strftime("%m-%d-%Y_%H:%M:%S")

        self.log_file_path = f"gamelogs/{self.player1}_{self.player2}_{dt_string}"
        self.log_file = open(self.log_file_path, "w")
        self.log_file.close()

        print(f"Created a game log at {self.log_file_path}.")
    
    def fightCard(self, card1, card2):

        """
        returns either Player.player1, Player.player2 or Player.self_destruct
        """

        if (card1 == None) or (card2 == None):
            raise ValueError("One of the cards is not right, please try again.")
        
        if (card1 == Cards.juqi):
            return Player.player2
        elif (card2 == Cards.juqi):
            return Player.player1
        elif (card1 == card2):
            return Player.self_destruct
        elif (card1 == Cards.zhda) or (card2 == Cards.zhda):
            return Player.self_destruct
        
        """
            function fight(blackCard: string, redCard: string): Player {

                const blackCardSize = cardIndex.get(blackCard);
                const redCardSize = cardIndex.get(redCard);

                if (!blackCardSize || !redCardSize) {
                    throw new Error("One of the black or red cards is invalid. Please check again.");
                }

                if ((blackCardSize === Cards.JUNQI) || (redCardSize === Cards.JUNQI)) {
                    return (blackCardSize === Cards.JUNQI) ? Player.RED_WIN : Player.BLACK_WIN;
                } else if (blackCardSize === redCardSize) {
                    return Player.SELFDESTRUCT;
                } else if ((blackCardSize === Cards.ZHADAN || redCardSize === Cards.ZHADAN)) {
                    return Player.SELFDESTRUCT;
                } else if ((blackCardSize === Cards.GONGBING || redCardSize === Cards.GONGBING)) {
                    return fightWithGongBing(blackCardSize, redCardSize);
                } else {
                    // should be no gongbing, dilei, or zhadan, just cards to compare sizes
                    return fightSimple(blackCardSize, redCardSize);
                }
            }

            function fightWithGongBing(blackCardSize: number, redCardSize: number): Player {
                if (blackCardSize === Cards.GONGBING) {
                    if (redCardSize === Cards.DILEI) {
                        return Player.BLACK_BIGGER;
                    }
                } else {
                    if (blackCardSize === Cards.DILEI) {
                        return Player.RED_BIGGER;
                    }
                }
                return fightSimple(blackCardSize, redCardSize);
            }


            function fightSimple(blackCardSize: number, redCardSize: number): Player {
                if (blackCardSize > redCardSize) {
                    return Player.BLACK_BIGGER;
                } else if (blackCardSize < redCardSize) {
                    return Player.RED_BIGGER;
                } else {
                    return Player.SELFDESTRUCT;
                }
            }
        
        """


        return
    
    def logFight(self, card1, card2, largerCard):
        print("Did the logging")
        return
    
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
        
        ## This method will all use Card enum() types.

        player1_card = Cards[card1]
        player2_card = Cards[card2]

        winner = self.fightCard(player1_card, player2_card)
        self.logFight(player1_card, player2_card, winner)
        return winner

    def endgame(self):
        return


    def fight(self):
        print("===========================================\n")
        print("Waiting for a fight ... I will be here when you need! \n")
        print("===========================================\n")

        player1_card = input(f"{self.player1}'s card (4 letters): ")
        player1_card_is_invalid = isInvalid(player1_card)

        while player1_card_is_invalid:
            print(f"{self.player1}, your card is invalid. Your card must be in the format of one of")
            print(validCards)
            player1_card = input(f"{self.player1}'s card (4 letters): ")
            player1_card_is_invalid = isInvalid(player1_card) 
        print("===========================================\n")

        player2_card = input(f"{self.player2}'s card (4 letters): ")
        player2_card_is_invalid = isInvalid(player2_card)

        while player2_card_is_invalid:
            print(f"{self.player2}, your card is invalid. Your card must be in the format of one of")
            print(validCards)
            player2_card = input(f"{self.player2}'s card (4 letters): ")
            player2_card_is_invalid = isInvalid(player2_card) 
        
        print("===========================================\n")
             
        winner = self.compareAndLog(player1_card, player2_card)
        print(f"For this fight, {winner} won the fight.")
        print("===========================================\n")

        if self.gameover == True:
            self.endgame()
        else:
            self.fight()
        

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
    