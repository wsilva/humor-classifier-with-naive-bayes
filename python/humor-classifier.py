#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

def readFileToLists(csvfile='../Sentiment Analysis Dataset.csv'):

    try:
        arq = open(csvfile, 'r')

        twittes = []

        # ignoring first line - header with label
        txt = arq.readlines()[1:] 

        for linha in txt :
            
            # get 4 columns
            lista = linha.split(',', 3)
            cod = lista[0]
            twit = lista[3].lower()
            # removing 'trashy' characters
            twit = re.sub(r'[^0-9a-z\ ]','', twit)
            humor = lista[1]
            
            twittes.append([cod,humor,twit])

        arq.close()
        return twittes
        
    except IOError as e:
        arq.close()
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        arq.close()
        print "Unexpected error:", sys.exc_info()[0]
        raise

def setupVocabulary(twittes):
    vocabulary = {}

    for twit in twittes:
        words = twit[2].split()
        humor = twit[1]
        for w in words:
            if w not in vocabulary:
                # print "Adicionando %s ao dicionario" % (w)
                vocabulary[w] = {'0': 0, '1': 0}

            vocabulary[w][humor]+=1
            # print "Incrementando o contador para %s com humor %s (%s)" % (w, humor, vocabulary[w][humor])

    return vocabulary

def main():
    print "Lendo arquivo para a memória..."
    twittes = readFileToLists()
    vocabulary = setupVocabulary(twittes)
    print "Vocabulário montado"
    print "Fim"

if __name__ == '__main__':
    main()