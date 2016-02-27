import random
import sys
import os

# create tuple of condition 1 and 2 scores
c1score = (999, 380, 412, 276, 232, 412)
c2score = (100, 632, 497, 551, 469, 502)

# create subject ID lis
subID = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6']

# convwert score tuples to lists.
c1scoreList = list(c1score)
c2scoreList = list(c2score)

# Description of program
jeff = '''Hello Jeff!  What I have built is a sample of a very simple 
example of experimental data in an interval timing experiment.
There are five participants who each reproduced a 300 ms and 500 ms 
stimulus one time each.  The data is as below.'''

print('\n\n\n\n' + jeff + '\n\n\n\n')

# Print scores for each subject
def chart(x, y, z):
	print('\n' + "The following are the duration judgements in ms for each subject." + '\n' +'\n')
	print("Subject ID         Condition 1          Condition 2" + '\n' + '\n')
	i = 0
	while (i <= len(x) - 1):
		print(x[i],end="")
		print("           ",end="")
		print(y[i],end="")
		print("                  ",end="")
		print(z[i])
		i += 1

chart(subID, c1scoreList, c2scoreList)

# perform basic stats

print('\n' + "The minimum score in condition 1 is ",end="")
print(min(c1score))
print("The maximum score in condition 1 is ",end="")
print(max(c1score))

def avgScore(x):
	j = 0
	t = 0
	while (j <= len(x) - 1):
		t += x[j]
		j += 1
	avscore = t / len(x)
	return avscore

print("The average score in condition 1 is ",end="")
print(avgScore(c1score))

print('\n' + "The minimum score in condition 2 is ",end="")
print(min(c2score))
print("The maximum score in condition 2 is ",end="")
print(max(c2score))	
print("The average score in condition 2 is ",end="")
print(avgScore(c2score))

# Notes on data
datNotes = '''Note that in the raw scores, Subject 1 performed
much differently than their counterparts.  As we
perform further statistics, we will find this 
participants performance to be an outlier in both conditions.

For this reason, we remove the participant's data.'''
print('\n\n\n\n' + datNotes + '\n\n\n\n')

# Remove outlier
del(c1scoreList[0])
del(c2scoreList[0])
del(subID[0])
c1score = tuple(c1scoreList)
c2score = tuple(c2scoreList)

chart(subID, c1scoreList, c2scoreList)

# redo stats
print('\n' + "The minimum score in condition 1 is ",end="")
print(min(c1score))
print("The maximum score in condition 1 is ",end="")
print(max(c1score))
print("The average score in condition 1 is ",end="")
print(avgScore(c1score))

print('\n' + "The minimum score in condition 2 is ",end="")
print(min(c2score))
print("The maximum score in condition 2 is ",end="")
print(max(c2score))	
print("The average score in condition 2 is ",end="")
print(avgScore(c2score))

# More statistical meanderings
moreStats = '''Further, we can combine the data for each condition
to come up with a global average.  This is not somethign you would
ever want to do with real data, but I am too tired to build more 
functions for absolute error and such!'''
print('\n\n\n\n' + moreStats + '\n\n\n\n')

c3scoreList = c1scoreList + c2scoreList
c3score = tuple(c3scoreList)

print('\n' + "The minimum score in combined scores is ",end="")
print(min(c3score))
print("The maximum score in combined scores is ",end="")
print(max(c3score))
print("The average score in combined scores is ",end="")
print(avgScore(c3score))
