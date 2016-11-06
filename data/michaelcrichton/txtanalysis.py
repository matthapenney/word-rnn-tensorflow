import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy as sp
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import seaborn as sns


with open("output.txt") as jurassicpark:
	jurassicpark_txt = jurassicpark.read()
	#jurassicpark.close()
	jurassicpark_tokens = jurassicpark_txt.split() #with no arguments, splits on whitespace
	print(len(jurassicpark_tokens))

lastword = jurassicpark_tokens[-1]
print(lastword)

strangestring = ",".join(jurassicpark_tokens)
strangestring[:100]

jurassicparklc_tokens = [word.lower() for word in jurassicpark_tokens]
count = jurassicparklc_tokens.count("had")
print(count)

#find unique set of words, count how often used with count method on lists
uniquelctokens = set(jurassicparklc_tokens)	

tokendict = {}
for ut in uniquelctokens:
	tokendict[ut] = jurassicparklc_tokens.count(ut)

el = sorted(tokendict.items(), key= lambda args: args[1], reverse = True)[:100]
print(el)

topfreq = el[:20]
print(topfreq)
with sns.axes_style('whitegrid'):
	pos = np.arange(len(topfreq))
	plt.bar(pos, [e[1] for e in topfreq]);
	plt.xticks(pos+0.4, [e[0] for e in topfreq]);
	plt.xlabel("Words")
	plt.ylabel("Count")
	plt.title("Word Frequency in output text")

plt.show()