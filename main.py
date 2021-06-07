"""
This is the main file where we created
the interaction between the user and the
database of artists.
We used the argparse module to configure
all the positional and optional arguments.
Depending on the arguments given,
the program leads the user to a series of steps
to either check the presence of an artist or painting
inside the database and/or add them to it.
There is also the possibility to check out
the association between artists and paintings,
the list of paintings and the list of artists.
"""
import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))
parser = argparse.ArgumentParser(description='this program will' +
                                             ' check if the name you put is' +
                                             'inside our database of ' +
                                             'artists and their ' +
                                             'most famous artwork.' +
                                             'If the names have' +
                                             'more than one space,' +
                                             'wrap them ' +
                                             'around quotes ("")')
group = parser.add_mutually_exclusive_group()
parser.add_argument("name", help="input the name of a known artist or painting")
group.add_argument("-a", "--add", action="store_true",
                   help="add a new artist or painting")
group.add_argument("-d", "--database", action="store_true",
                   help="show artist and relative painting")
group.add_argument("-p", "--paintings", action="store_true",
                   help="show the list of paintings")
group.add_argument("-art", "--artist", action="store_true",
                   help="show the list of artists")
args = parser.parse_args()
answer = args.name

if args.paintings:
    print("Now you can see by yourself if the painting is present in our database!")
    #db.drop("Unnamed: 0", axis=1, inplace=True)
    print(db["Artwork"])
if args.artist:
    print("Now you can see by yourself if the artist is present in our database!")
    #db.drop("Unnamed: 0", axis=1, inplace=True)
    print(db["Name"])
if args.database:
    print("Now you can see by yourself if the artist and his/her most famous painting are present in our database!")
    #db.drop("Unnamed: 0", axis=1, inplace=True)
    print(db["Name"]+ " : " + db["Artwork"])
