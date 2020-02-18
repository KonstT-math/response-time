
# How to use:
#
# download psychopy for it is required
#
# In the "initialization section":
# 1) Input a sequence which represents the stimulus position as follows: observables=[3,1,2,0,1]
# 2) Set the file path to print output: f=open(r"path\to\file.txt", "w")
# 3) Set the file path for the image stimulus: the_image=r'path\to\image.jpg'
#
# In the "first/second experiment" sections:
# 4) Enter the number of times your experiment(s) is going to be repeated: experiment(observables, repetition_times)
# 5) run the python script (in the command line: python3 name_of_script.py)


# -----------------------------------------------------------------
# --------------------------- imports -----------------------------

# Import the PsychoPy library, et c.
from psychopy import core, visual, event
from random import random, randrange
import numpy as np

# -----------------------------------------------------------------
# -------------------------- functions ----------------------------


# make a vector containing the transitions (ex i->j == [i,j])
def pairlist(tlist):
	res = [[tlist[i], tlist[i + 1]] for i in range(len(tlist) - 1)]
	res.append([tlist[len(tlist) - 1], tlist[0]])
	return res


# a function to create the transition probability distribution matrix
# input: observable sequence
def prob_distro(observables):
	# list of transition pairs:
	Pairs_observables=pairlist(observables)
	# we count each elements (to be used for restriction 1 for block 5):
	n0=observables.count(0)
	n1=observables.count(1)
	n2=observables.count(2)
	n3=observables.count(3)

	# we create the probability distribution (transition matrix for the Markov process):
	for i in range(0,4):
		if i==0:
			a00=Pairs_observables.count([i,0])/n0
			a01=Pairs_observables.count([i,1])/n0
			a02=Pairs_observables.count([i,2])/n0
			a03=Pairs_observables.count([i,3])/n0
		elif i==1:
			a10=Pairs_observables.count([i,0])/n1
			a11=Pairs_observables.count([i,1])/n1
			a12=Pairs_observables.count([i,2])/n1
			a13=Pairs_observables.count([i,3])/n1
		elif i==2:
			a20=Pairs_observables.count([i,0])/n2
			a21=Pairs_observables.count([i,1])/n2
			a22=Pairs_observables.count([i,2])/n2
			a23=Pairs_observables.count([i,3])/n2
		else:
			a30=Pairs_observables.count([i,0])/n3
			a31=Pairs_observables.count([i,1])/n3
			a32=Pairs_observables.count([i,2])/n3
			a33=Pairs_observables.count([i,3])/n3

	A=np.array([[a00,a01,a02,a03], [a10,a11,a12,a13], [a20,a21,a22,a23], [a30,a31,a32,a33]])
	
	return A, n0, n1, n2, n3


# the experiment function
# input: observable sequence, number of times to repeat, file to write on, image stimulus, window
def experiment(observables, repeat):
	block=1
	
	while (block <= repeat):
		print('BLOCK {}\n'.format(block),file=f)
		print('Observables are: {}\n'.format(observables),file=f)

		# counter is the variable counting the correct responses
		counter=0
		# attempt is the variable counting the number of responses for the block
		attempt=1

		for i in observables:
				
			
			# fixation cross that appears between image stimulus
			fix_cross.draw()
			win.flip()

			# position for ImageStim: stim.pos = (horizontal axis, vertical axis)
			# wait for 3-8 seconds to read feedback and have uncertain wait time before next trial
			core.wait(3+int(random()*6))

			if i==0:
				stim.pos = (0, 0.5) # up
				stim.draw()
				win.flip() # the win.flip() is required in order for the win to appear
				# -----------
				# clear any keystrokes before starting
				event.clearEvents()
				allKeys=[]

				# reaction time reset
				RT.reset() 

				while len(allKeys)==0: # wait for a keypress
					allKeys=event.getKeys(timeStamped=RT)
				# note that allKeys = [(key, milliseconds)]
				# if you don't have pyglet, you need to get the time explicitly via getTime()
				if not wintype == 'pyglet':
					allKeys[0][1] = RT.getTime()

				# note that allKeys = [(key, milliseconds)]
				thekey=allKeys[0][0]
				theRT =allKeys[0][1]
	
				flag=0
				if thekey=='escape':
					core.quit()
				elif thekey=='up':
					counter=counter+1
					flag=1
				else:
					pass
		
				# appends result to text file:
				print('attempt {}: key={} \t reaction time={} \t evaluation={} \n'.format(attempt,thekey,theRT,flag), file=f)

				
				# -----------
			elif i==1:
				stim.pos = (0.5, 0) # right
				stim.draw()
				win.flip()
				# -----------
				# clear any keystrokes before starting
				event.clearEvents()
				allKeys=[]
				
				# reaction time reset
				RT.reset() 

				while len(allKeys)==0: # wait for a keypress
					allKeys=event.getKeys(timeStamped=RT)
				# note that allKeys = [(key, milliseconds)]
				# if you don't have pyglet, you need to get the time explicitly via getTime()
				if not wintype == 'pyglet':
					allKeys[0][1] = RT.getTime()

				# note that allKeys = [(key, milliseconds)]
				thekey=allKeys[0][0]
				theRT =allKeys[0][1]
	
				flag=0
				if thekey=='escape':
					core.quit()
				elif thekey=='right':
					counter=counter+1
					flag=1
				else:
					pass
		
				# appends result to text file:
				print('attempt {}: key={} \t reaction time={} \t evaluation={} \n'.format(attempt,thekey,theRT,flag), file=f)



				# -----------
			elif i==2:
				stim.pos = (0, -0.5) # down
				stim.draw()
				win.flip()
				# -----------
				# clear any keystrokes before starting
				event.clearEvents()
				allKeys=[]
				
				# reaction time reset
				RT.reset() 

				while len(allKeys)==0: # wait for a keypress
					allKeys=event.getKeys(timeStamped=RT)
				# note that allKeys = [(key, milliseconds)]
				# if you don't have pyglet, you need to get the time explicitly via getTime()
				if not wintype == 'pyglet':
					allKeys[0][1] = RT.getTime()

				# note that allKeys = [(key, milliseconds)]
				thekey=allKeys[0][0]
				theRT =allKeys[0][1]
	
				flag=0
				if thekey=='escape':
					core.quit()
				elif thekey=='down':
					counter=counter+1
					flag=1
				else:
					pass
		
				# appends result to text file:
				print('attempt {}: key={} \t reaction time={} \t evaluation={} \n'.format(attempt,thekey,theRT,flag), file=f)



				# -----------
			else:
				stim.pos = (-0.5, 0) # left
				stim.draw()
				win.flip()
				# -----------
				# clear any keystrokes before starting
				event.clearEvents()
				allKeys=[]
				
				# reaction time reset
				RT.reset() 

				while len(allKeys)==0: # wait for a keypress
					allKeys=event.getKeys(timeStamped=RT)
				# note that allKeys = [(key, milliseconds)]
				# if you don't have pyglet, you need to get the time explicitly via getTime()
				if not wintype == 'pyglet':
					allKeys[0][1] = RT.getTime()

				# note that allKeys = [(key, milliseconds)]
				thekey=allKeys[0][0]
				theRT =allKeys[0][1]
	
				flag=0
				if thekey=='escape':
					core.quit()
				elif thekey=='left':
					counter=counter+1
					flag=1
				else:
					pass
		
				# appends result to text file:
				print('attempt {}: key={} \t reaction time={} \t evaluation={} \n'.format(attempt,thekey,theRT,flag), file=f)



				# -----------
			win.flip()
			attempt=attempt+1
	
		# prints the number of correct responses to the file:
		print('Number of correct responces for the block: {}\n-------------------------\n\n'.format(counter), file=f)

		block=block+1


# a function that implements the Markov model for four(4) states
# input: length of position sequence
# output: position sequence
def process(time):
	# possible sequences of events:
	transitionName=[["00","01","02","03"],["10","11","12","13"],["20","21","22","23"],["30","31","32","33"]]
	# pos_now=0 # starts from state 0
	pos_now=randrange(4) # starts from random state
	print("Start state: {}".format(pos_now))
	
	position_list=[pos_now]
	
	i=0
	# to calculate the probability of the position_List:
	prob=1
	while i!=time:
		if pos_now==0:
			change = np.random.choice(transitionName[0],replace=True,p=A[0])
			if change=="00":
				prob = prob*A[0][0]
				pos_now=0
				position_list.append(0)
				pass
			elif change=="01":
				prob = prob*A[0][1]
				pos_now=1
				position_list.append(1)
				
			elif change=="02":
				prob = prob*A[0][2]
				pos_now=2
				position_list.append(2)
				
			else:
				prob = prob*A[0][3]
				pos_now=3
				position_list.append(3)
		elif pos_now==1:
			change = np.random.choice(transitionName[1],replace=True,p=A[1])
			if change=="11":
				prob = prob*A[1][1]
				pos_now=1
				position_list.append(1)
				pass
			elif change=="10":
				prob = prob*A[1][0]
				pos_now=0
				position_list.append(0)
				
			elif change=="12":
				prob = prob*A[1][2]
				pos_now=2
				position_list.append(2)
				
			else:
				prob = prob*A[1][3]
				pos_now=3
				position_list.append(3)
		elif pos_now==2:
			change = np.random.choice(transitionName[2],replace=True,p=A[2])
			if change=="22":
				prob = prob*A[2][2]
				pos_now=2
				position_list.append(2)
				pass
			elif change=="21":
				prob = prob*A[2][1]
				pos_now=1
				position_list.append(1)
				
			elif change=="20":
				prob = prob*A[2][0]
				pos_now=0
				position_list.append(0)
				
			else:
				prob = prob*A[2][3]
				pos_now=3
				position_list.append(3)
		else:
			change = np.random.choice(transitionName[3],replace=True,p=A[3])
			if change=="33":
				prob = prob*A[3][3]
				pos_now=3
				position_list.append(3)
				pass
			elif change=="31":
				prob = prob*A[3][1]
				pos_now=1
				position_list.append(1)
				
			elif change=="32":
				prob = prob*A[3][2]
				pos_now=2
				position_list.append(2)
				
			else:
				prob = prob*A[3][0]
				pos_now=0
				position_list.append(0)
		i=i+1

	print('Possible states: {}'.format(position_list))
	print('Probability of the possible sequence of states: {}'.format(prob))
	
	return position_list

# -----------------------------------------------------------------
# ------------------------ initialization -------------------------


# open a file to print output
# when results are printed to text file, one may format the text so that tab characters (\t)
# are typed before and after "key", "responce time", or "evalutation" values. 
# This will enable one to easily pass the raw values to spreadsheets or stats software.
f=open(r"path\to\file.txt", "w")


# load image. Set the image file path for your machine..
the_image=r'path\to\image_file'


# create a window to draw in
# use specifications required in your application (see the phychopy documentation) 
# use pyglet if possible, it's faster at event handling
wintype='pyglet' 
win = visual.Window((800.0,700.0),winType=wintype)


# creates the ImageStim
stim = visual.ImageStim(win, image=the_image)

# fixation cross stimulus to appear at the centre
fix_cross = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=(1,0), wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)


# make a clock for capturing RT (reaction time)
# Note: psychopy selects a timer implementation as follows:
#     1) On Windows, the Windows Query Performance Counter 
# (Retrieves the current value of the performance counter, 
# which is a high resolution (<1us) time stamp that can be used for time-interval measurements.)
# API is used using ctypes access.
#     2) On other OS's, if the Python version being used is 2.6 or lower,
#        time.time is used. For Python 2.7 and above, the timeit.default_timer
#        function is used.
RT = core.Clock()


# set the position states
states=[0,1,2,3]
# here input the sequence of positions for the visual stimulus for the test
# for example:
observables=[3,1,2,0,2,1,3,2,1,0]


# calling prob_distro function on observables sequence
A, n0, n1, n2, n3 = prob_distro(observables)
print(A)


# -----------------------------------------------------------------
# ----------------------- first experiment ------------------------

# the first experiment uses the sequence that was input above.
# one may wish to repeat this experiment several times; each will be called a "block".

print('STANDARD BLOCKS\n',file=f)

experiment(observables, 2)


# -----------------------------------------------------------------
# ----------------------- second experiment -----------------------

# the stochastic block:
# in this block, we again have a sequence of positions of the same length as in the previous ones;
# but this time, the sequences is produced via a Markov stochastic process 
# with probability transition matrix (distribution) given by A (see above).
#
# it obeys the following restrictions:
# (1) each state in the new sequence appears the same number of times as in the previous experiment
# (2) the transition from state i to state j in the new sequence, is given by transition distribution A

# in the following, we create the new sequence until it validates restriction (1)
# restriction (2) is vadid because of process function (markov chain)

while True:

	observables = process(len(observables)-1)
	c0=observables.count(0)
	c1=observables.count(1)
	c2=observables.count(2)
	c3=observables.count(3)
	
	if c0==n0 and c1==n1 and c2==n2 and c3==n3:
		break
# -------------------

print('-------------------------\n-------------------------\n',file=f)
print('PROBABILISTIC BLOCKS\n',file=f)

# and the same code as in first experiment:

experiment(observables, 1)

# -----------------------------------------------------------------
# ----------------------- prepare to end --------------------------



# close file
f.close()
# wait for 3 secs
core.wait(3)

# Close the window
win.close()

# Close PsychoPy
core.quit()
