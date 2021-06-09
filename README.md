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

- Name of the artist;
- Dates of birth and death;
- Most famous painting;
- Year of execution;
- Painting location (Meuseum);
- Artistical movement;
- Nationality of the artist;
- Number of paintings the artist did in his/her life;
- Link to Wikipedia artist's page.

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
we wanted to achieve, we created 4 main functions and stored them into 
different modules:

-  `inserter` function;
-  `check_artist` and  `check_painting` functions;
-  `return_bio` function;
-  `similarities` function.

All of them are called by argparse from the main.py module.
In the main.py, functions are recalled by the optional arguments.

This means that if the user wants to get some insights from our functions, he/she
doesn't need to point on the specific module that contains the function, but it's
sufficient to type:

```bash
python main.py "name of the artist/painting" - optional argument
```
The name of the artist or of the painting is indeed a positional argument,
that should always been inserted. No optional argument is required if the user only wants to know whether the artist
is present in the csv file. For example, if we now want to know if Claude Monet is present, we have just to write:

```bash
python main.py "Claude Monet"
```

And the output will be:

```bash
Claude Monet is the artist of Impression, Sunrise
```

Instead, for more complicated queries, we can recall some optional arguments. 
Here follow some examples:

```bash
paython main.py "Bansky" -a
```
This argument allows to insert a new artist into the database. The -a activates the `inserter` function that will 
first check if the artist is already present in our database and then generate a sequence of questions to insert all the necessary data:

```bash
Now enter the name of his/her most famous painting -> Baloon girl
Now enter the date of birth and death of the artist-> 1973 - still alive
Now enter the year(s) of realization of the most famous artwork of the artist-> 2002
Now enter the museum and place (museum - city) where the painting is placed-> Waterloo Bridge - London
Now enter the artistic movement of the artist-> Street-art
Now enter the nationality of the artist-> British
Now enter the total number of artworks realized by the artist-> 136
Now enter the link to the wikipedia page of the artist-> https://en.wikipedia.org/wiki/Banksy
Thank you for your contribution!
```
Another argument is `python main.py "Claude Monet" -d`, which after being called allows to get the database realtion between artist and painting:

```bash
Now you can see by yourself if the artist and his/her most famous painting are present in our database!
0                    Amedeo Modigliani : Reclining Nude
1                  Vasiliy Kandinskiy : Composition VII
2                        Diego Rivera : Street in Avila
3                    Claude Monet : Impression, Sunrise
4               Rene Magritte : The Treachery of Images
5             Salvador Dali : The persistence of memory
6             Edouard Manet : The Luncheon on the Grass
7                               Andrei Rublev : Trinity
8                   Vincent van Gogh : The Starry Night
9                               Gustav Klimt : The Kiss
10    Hieronymus Bosch : The Garden of Earthly Delights
11                      Kazimir Malevich : Black Square
12                    Mikhail Vrubel : The Demon Seated
13                             Pablo Picasso : Guernica
14    Peter Paul Rubens : The Massacre of the Innocents
15    Pierre-Auguste Renoir : Bal du moulin de la Ga...
16                       Francisco Goya : The nuda maja
17    Frida Kahlo : Self-potrait with thorn necklace...
18                   El Greco : Dormition of the Virgin
19                        Albrecht Dürer : Self-potrait
20                 Alfred Sisley : Snow at Louveciennes
21    Pieter Bruegel : Landscape with the Fall of Ic...
22                         Marc Chagall : The Promenade
23               Giotto di Bondone : Ognissanti Madonna
24               Sandro Botticelli : The Birth of Venus
25         Caravaggio : The Incredulity of Saint Thomas
26                         Leonardo da Vinci : Gioconda
27                        Diego Velazquez : Las Meninas
28                                Henri Matisse : Dance
29       Jan van Eyck : Portrait of man with red turban
30                        Edgar Degas : The dance class
31    Rembrandt : Christ in the storm on the Sea of ...
32                    Titian : Assumption of the Virgin
33      Henri de Toulouse-Lautrec : At the Moulin Rouge
34                 Gustave Courbet : The Stone Breakers
35    Camille Pissarro : Boulevard Montmartre, Effet...
36              William Turner : The fighting temeraire
37                            Edvard Munch : The Scream
38    Paul Cezanne : Mont Sainte-Victoire seen from ...
39      Eugene Delacroix : La Liberté guidant le peuple
40                  Henri Rousseau : The Sleeping Gypsy
41    Georges Seurat : Un dimanche après-midi à l'Îl...
42                              Paul Klee : Red Balloon
43               Piet Mondrian : Broadway Boogie-Woogie
44                 Joan Miro : The Harlequin's Carnival
45                    Andy Warhol : The Marilyn Diptych
46                     Paul Gauguin : The Yellow Christ
47                       Raphael : The School of Athens
48                             Michelangelo : The Pietà
49                         Jackson Pollock : Blue Poles
```

Other two commands are:

- `paython main.py "Impression, Sunrise" -p` which allows to see the entire list of paintings
- `paython main.py "Claude Monet" -a`, to have access to the entire list of artists only.



# Contributing

If you want to contribute in growing the information of the Artdatabase, feel free 
to pull requests.
Please contact us if you wish to implement significant modifications and test
before pulling.

# License

GNU License

# Authors

- Vittoria Lazzer
- Melissa Mattioli
- Aurora Menegatto
- Anna Nardo
