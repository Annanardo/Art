# Art

ArtDatabase is a software development project that allows users to 
get information about famous artists and their most iconic paintings. 
Additionally, it allows to get information about artists belonging to the
same artistic movement or nationality and constructs a short biography on the fly.

If the name of the artist or painting provided as input is not present,
the program asks the user whether he/she wants to insert it. 
All of this can be managed directly from the machine terminal of the user.

In this brief, we will show a general overview of the initial CSV file as well
as a short explanation of how the software works and the results the user can 
get out of it.

# CSV file

In order to store all the paintings and authors, we created a CSV file we called
 `artists_paintings`, defined by the following properties:

- Name of the artist;
- Dates of birth and death;
- Most famous painting;
- Year of execution;
- Painting location (Museum);
- Artistical movement;
- Nationality of the artist;
- Number of paintings the artist did in his/her life;
- Link to Wikipedia artist's page.

The original file contains 49 rows (corresponding to 49 different artists), but this 
structure can be changed by the user since there is a function that allows him/her to
add rows by simply fulfilling some requirements (as the name of the artist the user wants
to add, the most famous painting, etc.).

This information is needed to the software in order to perform properly.


# How to start

The first thing to do in order to develop the main functionalities described above
is to clone the remote directory. To do so the user needs to use 
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

The name of the artist or the painting is, indeed, a positional argument,
that should always be inserted. No optional argument is required if the user only wants to know whether the artist
is present in the CSV file. 

For example, if we now want to know if Claude Monet is present, we have just to write:

```bash
python main.py "Claude Monet"
```

And the output will be:

```bash
Claude Monet is the artist of Impression, Sunrise
```

Instead, for more complicated queries, we can recall some optional arguments. 


Here follow some examples:

### •	Add a new artist (-a)

```bash
python main.py "Bansky" -a
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

### •	Find manually if the artist/painting is present in the database (-d)

Another argument is `python main.py "Claude Monet" -d`, which after being called allows to get the database relation between artist and painting:

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

- `python main.py "Impression, Sunrise" -p` which allows to see the entire list of paintings
- `python main.py "Claude Monet" -a`, to have access to the entire list of artists only.


### •	Print a bio of the artist (-bio)

The function of the biography module can be used to explain, more understandably and completely, the life of the artists. Together with the name and the nationality, It puts together some details that can be found in the dataset's columns. 
The function first checks if the input we inserted is present in the database, if not the system will warn you and invite you to check if you wrote it correctly.
You can also check the full biography with Wikipedia's link.

To use the function the user should recall the optional argument:

```bash
python main.py "Claude Monet" -bio
```

This will return a brief description of who was the artist, in which years has lived, which was his/her most famous 
painting and in which year it was painted. After this, you can find the museum in which the artwork is
displayed, to which movement the artist belongs, and the total number of artworks that have been made, 
together with Wikipedia's link. 

The output:

```bash
Claude Monet is a/an French artist who lived in these years: 1840 - 1926 . 
The artist painted in 1872 the most famous painting, named: Impression, Sunrise ,
now displayed at the Musée Marmottan Monet - Paris . 
The painter belongs to:  Impressionism movement(s). 
in addition to his/her most famous painting, she/he made 73 artworks in total.
Here you can find the web link to see 
the complete biography:  http://en.wikipedia.org/wiki/Claude_Monet

```

### •	Compare different artists (-s)

The similarities function is a function that allows the user to make some
comparisons between the artist she/he is interested in and other artists.
The function has been thought to have the columns "Nationality", "Genre"
and "paintings" as criteria for comparison and returns a result only if the number of artists
satisfying a given parameter are 2 or more. 
To use the function the user should recall the optional argument:

```bash
python main.py "Claude Monet" -s
```

After this, the user is asked if she/he wants to visualize similarities according
to nationality (nat), artistic movement (mov), or the number of paintings (nop).
Here an example:

```bash
Do you want to see the similarities according to nationality, artistic movement or number of paintings? 
(nat, mov, nop) -> nat 
```
If the user chooses nationality or artistic movement, the function retreives 
all the artists that satisfy the requirement.

```bash
3                Claude Monet
6               Edouard Manet
15      Pierre-Auguste Renoir
28              Henri Matisse
30                Edgar Degas
33  Henri de Toulouse-Lautrec
34            Gustave Courbet
35           Camille Pissarro
38               Paul Cezanne
39           Eugene Delacroix
40             Henri Rousseau
41             Georges Seurat
46               Paul Gauguin
```

On the other hand, if the user chooses to visualize 
the number of paintings, she/he is asked if she/he wants to visualize
the artists with a higher (>), smaller (<) or equal (==) number of artworks and,
after the choice, the list of artists is provided.
For example:

```bash
Do you want to search for artists that have made more (>), less (<) or the same (==) number you provided as input?<
```

```bash
2       Diego Rivera         70
25        Caravaggio         55
34   Gustave Courbet         59
36    William Turner         66
37      Edvard Munch         67
38      Paul Cezanne         47
39  Eugene Delacroix         31
40    Henri Rousseau         70
41    Georges Seurat         43
48      Michelangelo         49
49   Jackson Pollock         24
```

# Contributing

If you want to contribute to the Artdatabase by adding more information, feel free
to pull requests.
Please, contact us if you wish to implement significant modifications and test
before pulling.


# License

GNU License


# Authors

- Vittoria Lazzer
- Melissa Mattioli
- Aurora Menegatto
- Anna Nardo
