import pandas as pd

def similarities(column, parameter):
    """
    This function returns all the artists that satisfy a required parameter
    given by the user. 
    """ 
    db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))
    
    column = str(column)
    
    if type(parameter) == int:
        valore = str(input("Do you want to search for artists that have made more (>), less (<) or the same (==) number you provided as input?"))
        
        if valore == ">":
            result = db.loc[db[column] > parameter ][["Name", column]]
            if len(result) >1:
                print("The artists that painted more than {} artworks are the following: {}".format(parameter, result))
            else:
                print("Sorry, there are no artists that painted more than {} artworks.".format(parameter))
        
        elif valore == "<":
            result = db.loc[db[column] < parameter ][["Name", column]]
            if len(result) >1:
                print("The artists that painted less than {} artworks are the following: {}".format(parameter, result))
            else:
                print("Sorry, there are no artists that painted less than {} artworks. ".format(parameter))
        elif valore == "==":
            result = db.loc[db[column] == parameter ][["Name", column]]
            if len(result) >1:
                print("The artists that painted {} artworks are the following: {}".format(parameter, result))
            elif len(result)==1:
                print("The artist that painted {} artworks is the following: {}".format(parameter, result))
            else:
                print("Sorry, there are no artists that painted {} artworks".format(parameter))
        else:
            print("You have to enter <, > or ==.")

    else:
        parameter = str(parameter)
        result = db.loc[db[column] == parameter ][["Name"]]
        if len(result) >1:
            print("The artists that satisfy the parameter {} are the following: {}".format(parameter, result))
        else:
            print("Sorry, we there are not similarities with {} parameter ".format(parameter))