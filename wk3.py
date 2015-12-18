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

# to generate kmer_list
# kmer_list=[]
# for i in range(0,16): kmer_list.append(bin[i][2:].zfill(4))

def OverlapGraph(kmer_list):
	K=len(kmer_list)
	prefix=['x']*K
	suffix=['x']*K

	for i in range(0, K):
		prefix[i]=kmer_list[i][0:-1]
		suffix[i]=kmer_list[i][1:]

	overlap_list=dict(zip(range(0,K),[0]*K))
	for i in range(0, K):
		overlap_list[i]=[]
		for j in range(0, K):
			if (prefix[j]==suffix[i]) & (j!=i):
				overlap_list[i].append(j)	
		
	return overlap_list


def HGraph(dictionary):
	#i=dictionary.keys()[-1]  # start from 0 will enter infinite loop
	k=0
	while(k<len(dictionary.keys())):
		break_flag=False
		i=dictionary.keys()[k]
		gph=[i]
			
		while(len(gph)<len(dictionary.keys())):
			i=gph[-1]
			tmp_ind=0
			for j in dictionary[i]:
				if j not in gph:
					gph.append(j)
					break
				else: continue
				tmp_ind+=1
				if tmp_ind==len(dictionary[i]): 
					break_flag=True
					break
		
			if break_flag:
				k+=1
				break
			
			print tmp_ind, gph

	return		


# reload(wk3)
