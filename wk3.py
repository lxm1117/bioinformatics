from wk1 import *
from wk2 import *

def Composition(text,k):
	for i in range(0, len(text)-k+1): print text[i:i+k]
	# return sorted(compos_str)
'''
def GenomePath(text_list):
	ans=''

	k_heads=['x']*len(text_list)
	k_tails=['x']*len(text_list)
	
	for(i=0;i<len(text_list);i++):
		k_heads[i]=text_list[i][0:k]
		k_tails[i]=text_list[i][-k:]	
	
	for(i=0;i<len(text_list);i++):
		try: 
			j=k_tails.index(k_heads[i])
			ans+=
		except: 
		# this should be the sequence to start with
			
'''

def GenomePath(textlist):
	ans=textlist[0]
	k=len(textlist[0])-1

	for i in range(1, len(textlist)):
		ans+=textlist[i][-1]

	return ans


def ReadTextList(filename):
	text_list=[]
	with open(filename, 'r') as f:
		for line in f: text_list.append(line[0:-1])
	
	f.close()
	return text_list


def OverlapGraph(kmer_list):
	K=len(kmer_list)
	prefix=['x']*K
	suffix=['x']*K

	for i in range(0, K):
		prefix[i]=kmer_list[i][0:-1]
		suffix[i]=kmer_list[i][1:]

	overlap_list=dict(zip(kmer_list,['']*K))
	for i in range(0, K):
		overlap_list[kmer_list[i]]=list(overlap_list[kmer_list[i]])
		for j in range(0, K):
			if (prefix[j]==suffix[i]) & (j!=i):
				overlap_list[kmer_list[i]].append(kmer_list[j])	
		
	return overlap_list
