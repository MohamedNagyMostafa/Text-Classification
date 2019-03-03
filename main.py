from __future__ import division
from codecs import open

def read_documents(doc_file):
    docs = []
    labels = dict()
    total = 0
    max_ite = 0
    with open(doc_file, encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
            	if not word in labels:
            		labels[word] = 0
            	else:
            		labels[word] += 1

            		if labels[word] == 1:
            			max_ite += 1

            	total += 1
            			
            
    return labels, total, max_ite

def naiveByas(dic_words, total_words, word_, max_ite):
	## Repeating words
	repeat = 0
	for word in dic_words:
		repeat += dic_words[word]

	P_word_G_repeating = 0
	
	P_word = 1/len(dic_words)
	
	P_wordcount = (repeat+max_ite)/total_words

	if repeat != 0:
		P_word_G_repeating = (dic_words[word_] + 1)/total_words

	P_word_repeating = P_word_G_repeating * P_wordcount + (1-P_wordcount) *(1-P_wordcount)

	print('P({})= {}, P(repearting)= {}, P=(repeating|{})= {}'.format(word_, P_word, P_wordcount, word_, P_word_G_repeating))
	print('P(repeating|{})={}'.format(word_, P_word_repeating/P_wordcount))

dic_words, total_words, max_ite = read_documents('classification.txt')



print(naiveByas(dic_words, total_words, 'amazing', max_ite))
