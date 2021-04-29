from stock_madlibs import letter_from_george as lfg, nickelodoen as nick, election
import random

if __name__ == "__main__":
    m = random.choice([lfg, nick, election])
    m.madlib()