# Art

ArtDatabase is software development project that allows users to 
get information about famous artists and their most iconic paintings. 
Additionally it allows to get information about artists belonging to the
same artistic movement or nationality and constructs a short biography on the fly.
If the name of the artist or painting provided as input is not present,
the program asks the user wheather he/she wants to insert it. 
All of this can be managed directly from the machine terminal of the user.

# How to start

First thing to do in order to develop the main functionalities described above,
is to clone the remote directory. In order to do so the user needs to use 
git clone https://github.com/Annanardo/Art/tree/main, by doing this is possible to
automatically download all the files, contained in the "Art" folder, that the user 
needs to run the program.

# Functionalities

ArtDatabase contains mainly 4 functions contained in different modules:

- inserter function;
- check_artist and check_painting functions;
- bio function;
- similarities function.

All of them are called by the argparse from the main.py module.
