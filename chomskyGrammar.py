import random
import sys
import os

# This program is intended to generate a grammar based on a set of rules.

# Set of terminals and non-terminals
print('''The set of terminals for this grammar is:
	{Trump Cruz Sanders Clinton people guns money Constitution hates loves criminalizes defends mean old dishonest compassionate who that''' + '}')

print('''The set of non-terminals for this grammar is:
	{SENTENCE NOUN_PHRASE VERB_PHRASE NOUN VERB  ADJECTIVE OBJECTIVE''' + '}')

print('''This program will use the rules of the grammar to randomly create 20 sentences.  
	The sentences are different each time it is run.  
	A Markov Chain is included to implement the requirement of recursion.''' + '\n' + '\n')

# Rules of our grammar
def SENTENCE(x):
	# SENTENCE -> NOUN_PHRASE VERB_PHRASE
	print("Sentence ",end="")
	print(x)
	print('\n' + '\n')
	NOUN_PHRASE(x)

def NOUN_PHRASE(X):
	y = (1, 2, 3, 4, 5)
	NP = random.choice(y)
	if NP == 1:
		# Noun_Phrase -> ADJECTIVE
		ADJECTIVE(y)
	else:
		NOUN(y)

def ADJECTIVE(y):
	adj = [' mean', ' old', ' dishonest', ' compassionate', ' creepy', ' horny', ' angry', ' funny', ' sad']
	x = random.choice(y)
	print(random.choice(adj),end="")
	if x == 1:
		ADJECTIVE(y)
	else:
		NOUN(y)

def NOUN(y):
	n1 = [' Trump', ' Cruz', ' Sanders', ' Clinton']
	n2 = [' people', ' guns', ' money', ' Constitution', ' Military', ' Russia', ' Mexico', ' rapists', ' socialism']
	x = random.choice(y)	
	if x == 5:
		x = random.choice(y)
		if x  <= 2:
			print(random.choice(n2) + ', that',end="")				
			VERB_PHRASE(y)
		else:
			print(random.choice(n1) + ', who',end="")	
			VERB_PHRASE(y)
	elif x == 1:
		x = random.choice(y)
		if x <= 3:
			print(random.choice(n1) + '.' + '\n' + '\n')
		else:
			print(random.choice(n2) + '.' + '\n' + '\n')
	else:
		if x <= 3:
			print(random.choice(n1),end="")
			VERB_PHRASE(y)
		else:
			print(random.choice(n2),end="")
			VERB_PHRASE(y)			

def VERB_PHRASE(y):
	VERB = [' hates', ' loves', ' criminalizes', ' defends', ' burns', ' assaults', ' murders', ' fucks', ' rapes', ' fracks', ' dreams of']
	x = random.choice(y)
	if x == 1:
		print(random.choice(VERB) + '.' + '\n' + '\n')
	else:
		print(random.choice(VERB),end="")
		NOUN_PHRASE(y)		

i = 1

# Derivation of 20 sentences 
while i <= 20:
	SENTENCE(i)
	i += 1








