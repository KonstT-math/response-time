# response-time
An application used for reaction time measurement, intended mainly for social science experiments. A visual stimulus appears on a window at one of four positions: 0-top, 1-right, 2-bottom, 3-left. Then the user is to press one of the arrow keys on the keyboard, in correspondence to the position of the image. The reaction time and the response result (true or false) is measured by the program, which is printed on a text file.

Consists of two parts:

(a) the first experiment with a given sequence of positions (states) of the visual stimulus
- can be repeated as many times as needed

(b) the second experiment, which constructs a new sequence from the one given in (a) via a Markov stochastic process
- the new sequence obeys two restrictions: 
- (1) each state (position) appears the same number of times as in the previous experiment
- (2) the probability distribution to construct the new one, is inherited from the first experiment

To be cited as:

DOI: 
10.5281/zenodo.3673881




The project is inspired from the following study:

Lum, J., Kidd, E., Davis, S., Conti-Ramsden, G., (2010). "Longitudinal study of declarative and procedural memory in primary school-aged children",
Australian Journal of Psychology, 62(3), 139-148.


How to use:

download psychopy for it is required

In the "initialization section":

1) Input a sequence which represents the stimulus position as follows: observables=[3,1,2,0,1]

2) Set the file path to print output: f=open(r"path\to\file.txt", "w")

3) Set the file path for the image stimulus: the_image=r'path\to\image.jpg'


In the "first/second experiment" sections:

4) Enter the number of times your experiment(s) is going to be repeated: experiment(observables, repetition_times)

5) run the python script (in the command line: python3 name_of_script.py)
