># algorithmic-music

This repository was created for the course ["Algorithmic Sound Structure & Composition"](https://avarts.ionio.gr/en/studies/undergraduate/courses-descriptions/aud821/) at the Department of Audio & Visual Arts of the Ionian University, taught by Prof. Zannos Ioannis. The purpose is to put in practice current methods of digital sound synthesis and algorithmic creation of musical structures, that were taught during the course.

## Built with

This project was built using [FoxDot](https://foxdot.org/), a Python library which is used as a live coding environment, along with the sound synthesis engine [SuperCollider](https://supercollider.github.io/). FoxDot creates an interactive programming environment scheduling musical events while it communicates with SuperCollider. Both FoxDot and SuperCollider are free and open-source softwares providing detailed documentation with relevant examples.

## Workflow

The synthesis was composed with FoxDot library using a variety of its built-in objects and methods like: SynthDefs, Pattern methods, functions and Generators, filters, effects and algorithmic manipulation. While FoxDot is a live coding environment mostly being used as a performing arts form giving the possibility for interactive programming in an improvised way, the present project is written in a form that can be reproduced initially in the given sequence as in the provided recorded file. The recording was made on SuperCollider using the commands: `s.record;` and `s.stopRecording;`. The output file was converted to mp3 format using the open-source audio software [Audacity](https://www.audacityteam.org/).


##  Αlgorithms & techniques for Sound synthesis

Musical algorithmic composition can be described as a process of making music by using some formal processes and computational methods which require minimal human intervention. Although it sounds like a modern technique that has been developed due to the revolution in computer science during the last decades, it seems that its roots date back to the ancient times when Pythagoras discovered the connection between music and maths. According to its teachings there is a direct relation between the natural laws and musical harmony while music is perceived as inseparable to numbers. Numbers were thought to be the key to the spiritual and physical universe and the musical sounds that are ordered by numbers exemplify the harmony of the universe corresponding to it. This way, he set the mathematical baseline for musical composition and experimentation that would follow.
Several years later, Wolfgang Amadeus Mozard created his own automated technique based on chance and randomness.

The potential of computers to generate music was recognised since the 19th century when Ada Lovelace, the inventor of the calculating engine, noticed that it might be able to compose elaborate and scientific pieces of different degrees of complexity or extent.

Several years later, the first computer generated composition by Lejaren Hiller at the University of Illinois, was created by using raw musical material which was initially produced by the machine and was then modified according to different functions which were rated at the end based on specific rules.

One of the pioneering methods of algorithmic composition was that which was created by Iannis Xenakis who applied multiple different probability theories making use of the computational speed in order to create stochastic compositions, based on probability and random numbers. He was also the pioneer of Granular Synthesis, a technique which was developed by using a collage of muptiple recorded short sound sources.

Nowadays, the vast use of computers and information technology have brought a revolution not only in the music creativity and digital techniques in music production but also in the relationship and the experience that the audience has with music. Musical creation is no longer based on the pursuit of the ideal and unique form but it is rather based on an subtractive realism which gives a plethora of possibilities for creativity and artistic expression. Taken for granted that the digital revolution has affected many different aspects of musical production and sound editing, computational and algorithmic synthesis is a subject that is taught and explored at the Musical Departments of the Universities, although there is a controversy over the aesthetics of the produced sounds and musical genres.

There are several and different approaches to algorithmic sound synthesis and structure depending on the way they affect the provided information, the kind of information that the algorithm modifies and the result that is produced. Regarding sound synthesis, some of the most representative techniques are: additive synthesis, subtractive synthesis, modulation techniques, wavetable synthesis, delay lines and granular synthesis. Depending on the way these techniques affect the initial information and the production of new spectral content, they are called linear or non-linear techniques.


# Getting started

In order to get a copy of this project up and running on your local machine for development and testing purposes, please follow the instructions below.

## Prerequisites

- It is necessary to install SuperCollider and FoxDot following all the required steps in the respective installation guides. 
- It is recommended to install [git](https://git-scm.com/downloads) as well.
- Python 3.8.5 or an earlier version is also necessary.

## How to run the project

If you wish to try running the file yourself and experiment with it, after having installed both FoxDot and SuperCollider:

1. First on SuperCollider you run the command `FoxDot.start;`. After that, SuperCollider is ready to listen to messages from FoxDot. Make sure that you have installed before FoxDot Quarks on SuperCollider. In case you face any problems just follow the steps that are described [here](https://forum.toplap.org/t/frequently-asked-questions/504).

2. Then on git bash or your preferred command line, after you cd in FoxDot directory, run the command: `python -m FoxDot` or `py -m FoxDot` depending on the Python version you have installed on your OS. This command opens up the FoxDot interface.

3. Open the file and execute it line by line making any changes you wish and listen to the results.

## Authors

Evi Giannakou

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License. Please read the LICENSE.md file for further details.

## Acknowledgments

Professor Ioannis Zannos, Department of Audio & Visual Arts, Ionian University.

## References

Anderling, V., et al. 2014. Generation of music through genetic algorithms. Chalmers University of Technology and University of Gothenburg.

Lotis, Th., Diamantopoulos, T. 2015. Music Informatics & Computer Music. [ebook] Athens:Hellenic Academic Libraries Link. [Available Online](http://hdl.handle.net/11419/4920).

Ruviaro, Br. 2015. A Gentle Introduction to SuperCollider. Santa Clara University.

Tolonen, T., Välimäki, V., and Karjalainen, M. 1998. Evaluation of Modern Sound Synthesis Methods. HUT.
