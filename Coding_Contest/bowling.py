import numpy as np
import argparse

# Define Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Bowling input")
args = vars(ap.parse_args())

# Get input from command line and cast it from string to int
def processInputs(input):
    # Split up input and put the throws in an array and the rounds_played in an integer
    input = np.array(input.split(":"))
    throws = np.array(input[1].split(",")).astype(int)
    rounds_played = int(input[0])
    return rounds_played, throws


class Player:

    # Init the Player
    def __init__(self, rounds_in_a_match):
        self.score = np.empty(rounds_in_a_match, int)
        self.rounds_played = 0
        self.strike_last_round = False
        self.spare_last_round = False


    def playMatch(self, rounds_played, throws):
        j = 0
        for i in range(0, rounds_played):
            if throws[j] == 10:
                self.strikeRound(throws[j])
                j += 1
            elif j == len(throws) - 1:
                self.abnormalRound(throws[j])
            else:
                self.normalRound(throws[j], throws[j + 1])
                j += 2




    def normalRound(self, throw1, throw2):
        # Add throws to score
        self.score[self.rounds_played] = throw1 + throw2

        # Add Boni if there was a Strike or Spare last Round
        if self.strike_last_round:
            self.score[self.rounds_played - 1] += throw1 + (throw1 + throw2)
        elif self.spare_last_round:
            self.score[self.rounds_played - 1] += throw1

        # Check if there is a Spare current round and set the Boolean
        if throw1 + throw2 == 10:
            self.spare_last_round = True

        # Add the Score from last round to the current round
        if self.rounds_played > 0:
            self.score[self.rounds_played] += self.score[self.rounds_played - 1]

        # Increase the played rounds
        self.rounds_played += 1


    def strikeRound(self, throw1):
        # Add throws to score
        self.score[self.rounds_played] = throw1

        # Add Boni if there was a Strike or Spare last Round
        if self.strike_last_round:
            self.score[self.rounds_played - 1] += throw1
        elif self.spare_last_round:
            self.score[self.rounds_played - 1] += throw1

        # Add the Score from last round to the current round
        if self.rounds_played > 0:
            self.score[self.rounds_played] += self.score[self.rounds_played - 1]

        # set Strike to True
        self.strike_last_round = True

        # Increase Round Counter
        self.rounds_played += 1


    def abnormalRound(self, throw1):
        # Add Boni if there was a Strike or Spare last Round
        if self.strike_last_round:
            self.score[self.rounds_played - 1] += throw1
        elif self.spare_last_round:
            self.score[self.rounds_played - 1] += throw1




# Init Player with the number of rounds his match is supposed to take
player1 = Player(10)

# Play the match and calculate the socre
rounds_played, throws = processInputs(args["input"])
player1.playMatch(rounds_played, throws)

#print out the score in the wanted form
print("The Array is : ")
for i in range(0, player1.rounds_played):
    print(player1.score[i], end = ',')
