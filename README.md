# Art

ArtDatabase is a software development project that allows users to 
get information about famous artists and their most iconic paintings. 
Additionally it allows to get information about artists belonging to the
same artistic movement or nationality and constructs a short biography on the fly.

If the name of the artist or painting provided as input is not present,
the program asks the user whether he/she wants to insert it. 
All of this can be managed directly from the machine terminal of the user.

# CSV file

In order to store all the paintings and authors, we created a csv file, containing:

- Name of the artist
- Birth and death dates
- Most famous painting
- Year of execution
- Where is the painting
- Artistical movement
- Nationality of the artist
- Number of paintings the artist did in his/her life
- Link to Wikipedia artist's page

The original file contains 49 rows (corresponding to 49 different artists), but this 
structure can be changed by the user, since there is a function that allows him/her to
add rows by simply fulfilling some requirements (as the name of the artist the user wants
to add, the most famous painting, etc.).

All those information are needed to the software in order to perform properly.

# How to start

First thing to do in order to develop the main functionalities described above,
is to clone the remote directory. In order to do so the user needs to use 
 `git clone https://github.com/Annanardo/Art/tree/main ` .
By doing this is possible to automatically download all the files, 
contained in the "Art" folder, and the user will be able to run the program.

# Functionalities

To develop an appropriate structure for our project according to the goals
we wanted to achieve, we created 4 main functions and we stored them into 
different modules, and they are:

-  `inserter` function;
-  `check_artist` and  `check_painting` functions;
-  `return_bio` function;
-  `similarities` function.

All of them are called by argparse from the main.py module.
In the main.py, functions are recalled by the positional arguments.

This means that if the user wants to get some insights from our functions, he/she
doesn't need to point on the specific module that contains the function, but it's
sufficient to type:

```bash
python main.py "name of the artist/painting" - positional argument
```


# Contributing

If you want to contribute in growing the information of the Artdatabase, feel free 
to pull requests.
Please contact us if you wish to implement significant modifications and test
before pulling.

#License

GNU License

#Authors

- Vittoria Lazzer
- Melissa Mattioli
- Aurora Menegatto
- Anna Nardo
