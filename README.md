# algorithmic-music

This repository was created for the course ["Algorithmic Sound Structure & Composition"](https://avarts.ionio.gr/en/studies/undergraduate/courses-descriptions/aud821/) at the Department of Audio & Visual Arts of the Ionian University, taught by Prof. Zannos Ioannis. The purpose is to put in practice current methods of digital sound synthesis and algorithmic creation of musical structures, that were taught during the course.

## Built with

This project was built using [FoxDot](https://foxdot.org/), a Python library which is used as a live coding environment, along with the sound synthesis engine [SuperCollider](https://supercollider.github.io/). FoxDot creates an interactive programming environment scheduling musical events while it communicates with SuperCollider. Both FoxDot and SuperCollider are free and open-source softwares providing detailed documentation with relevant examples.

## Workflow

This synthesis was composed with FoxDot library using a variety of its built-in objects and methods like: SynthDefs, Pattern methods, functions and Generators, filters, effects and algorithmic manipulation. While FoxDot is a live coding environment mostly being used as a performing arts form giving the possibility for interactive programming in an improvised way, the present project is written in a form that can be reproduced initially in the given sequence as in the provided recorded file. The recording was made on SuperCollider using the commands: `s.record;` and `s.stopRecording;`. The output file was converted to mp3 format using [Audacity](https://www.audacityteam.org/).


## Sound synthesis algorithms & techniques

## Prerequisites

It is necessary to install SuperCollider and FoxDot. It is recommended to install git as well.

## Running the project

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
