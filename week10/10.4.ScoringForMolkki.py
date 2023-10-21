"""
COMP.CS.100 Programming 1.
10.3.ClassifiedCar.py
Creator: Thinh Kieu
Student id number: 152167613
"""


class Player:
    """
    This class stores the information about the player and their state.
    """

    def __init__(self, player_name):
        """
        Initialize a player.
        :param player_name: string, the name of the player
        """
        self.__name = player_name
        self.__score = 0
        self.__cumulative_score = 0
        self.__rounds_played = 0
        self.__successful_rounds = 0

    def get_name(self):
        """
        Return the name of the player
        :return: string, name of the player
        """
        return self.__name

    def get_points(self):
        """
        Return the score of the player
        :return: int, score of the player
        """
        return self.__score

    def add_points(self, pts):
        """
        Add the points from a turn to a player's score.
        If the score after adding is higher than 50, it falls back to 25.
        Also modifies the cumulative score, the number of rounds played and the number of successful rounds.
        :param pts: int, the points from a turn
        """
        self.__score += pts
        self.__cumulative_score += pts
        self.__rounds_played += 1
        if pts > 0:
            self.__successful_rounds += 1

        if self.__score > 50:
            self.__score = 25
            print(f"{self.__name} gets penalty points!")

    def has_won(self):
        """
        Decide whether a player has won the game.
        :return: bool, True if the player has won the game.
        """
        if self.__score == 50:
            return True
        else:
            return False

    def score_warning(self):
        """
        Print out a warning for the players if their score is close to 50.
        """
        if self.__score >= 40 and self.__score <= 49:
            print(f"{self.__name} needs only {50 - self.__score} points. It's better to avoid knocking down the pins "
                  f"with higher points.")

    def get_average_points(self):
        """
        Return the average score from all the turns a player has played.
        :return: float, the average score
        """
        return self.__cumulative_score / self.__rounds_played

    def cheers(self, pts):
        """
        Print out a cheer message if a player's point in one turn is higher than their average one.
        :param pts: int, the points from a turn
        """
        if pts > self.get_average_points():
            print(f"Cheers {self.__name}!")

    def get_success_percentage(self):
        """
        Return the percentage of successful turns so far.
        :return: float, the percentage of successful turns.
        """
        if self.__rounds_played == 0:
            return 0
        return self.__successful_rounds / self.__rounds_played * 100


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)
        in_turn.score_warning()
        in_turn.cheers(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,", f"hit percentage {player1.get_success_percentage():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p,", f"hit percentage {player2.get_success_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
