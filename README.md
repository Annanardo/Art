# Art

ArtDatabase is a software development project that allows users to 
get information about famous artists and their most iconic paintings. 
Additionally it allows to get information about artists belonging to the
same artistic movement or nationality and constructs a short biography on the fly.

If the name of the artist or painting provided as input is not present,
the program asks the user wheather he/she wants to insert it. 
All of this can be managed directly from the machine terminal of the user.

# How to start

First thing to do in order to develop the main functionalities described above,
is to clone the remote directory. In order to do so the user needs to use 
 `git clone https://github.com/Annanardo/Art/tree/main ` , by doing this is possible to
automatically download all the files, contained in the "Art" folder, and the user will be 
able to run the program.

# Functionalities

ArtDatabase contains mainly 4 functions which are stored in different modules:

-  `inserter function`;
-  `check_artist` and  `check_painting` functions;
-  `return_bio` function;
-  `similarities` function.

All of them are called by argparse from the main.py module.

In the main.py, functions are recalled by the positional arguments.





# Contributing

If you want to contribute in growing the information of the Artdatabase, feel free to pull requests.
Please contact us if you wish to implement significant modifications and test before pulling.

#License

GNU License

#Authors

- Vittoria Lazzer
- Melissa Mattioli
- Aurora Menegatto
- Anna Nardo
