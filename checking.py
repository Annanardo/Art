"""
This module focuses on checking if the input
given by the user is present in our database (csv file)
that contains information of artists and paintings.
"""

import pandas as pd


class Check:


    def check_artist(self, artist):
        """
        This function controls if the input given
        by the user is present in the artist
        column inside the csv file.
        """
        def Convert(string):
            li = list(string.split(" "))
            return li
        artist = artist.lower()
        db = pd.DataFrame(pd.read_csv('artistsandpaintings.csv'))
        artists = db["Name"].str.lower()
        if artist in artists.values:
            return True
        return False

    def check_paintings(self, painting):
        """
        This function controls if the input given
        by the user is present in the artwork
        column inside the csv file.
        """
        painting = painting.lower()
        db = pd.DataFrame(pd.read_csv('artistsandpaintings.csv'))
        paintings = db["Artwork"].str.lower()
        if painting in paintings.values:
            return True
        return False