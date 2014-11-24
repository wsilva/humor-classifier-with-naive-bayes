#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import random

def separateTrainAndTestGroups(csvfile='Sentiment Analysis Dataset.csv', testSetPercentSize=0.3):
    
    try:
        # open database file and sort it 'randomly'
        with open(csvfile,'r') as source:
            data = [ (random.random(), line) for line in source ]
        data.sort()

        # get the limit of lines on train file
        trainSetPercentSize = 1 - testSetPercentSize
        trainSetLimitLines = trainSetPercentSize * len(data)

        # writting 2 files with trainSet and testSet based on limit lines on each
        cont = 0
        with open('trainSetFile.csv','w') as trainFile, open('testSetFile.csv','w') as testFile:
            for _, line in data:
                if cont < trainSetLimitLines:
                    trainFile.write(line)
                else:
                    testFile.write(line)
                cont+=1

        # closing the resources
        source.close()
        trainFile.close()
        testFile.close()

        return True

    except IOError as e:
        source.close()
        trainFile.close()
        testFile.close()
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        source.close()
        trainFile.close()
        testFile.close()
        print "Unexpected error:", sys.exc_info()[0]
        raise

def readFileToLists(csvfile='trainSetFile.csv'):

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

def getProbabilities(vocabulary):

    for words,frequency in vocabulary:
        prob_positive = float(freq["1"]) / float(self.count_positive)
        prob_negative = float(freq["0"]) / float(self.count_negative)

def main():

    print "Embaralhando dados e separando em conjuntos de treinamento e teste..."
    separateTrainAndTestGroups("../Sentiment Analysis Dataset.csv", 0.3)
    print "Concluído"
    print "..."

    print "Lendo arquivo de treinamento para a memória"
    twittes = readFileToLists("trainSetFile.csv")
    print "Concluído"
    print "..."

    print "Montando Vocabulário"
    vocabulary = setupVocabulary(twittes)
    print "Concluído"
    print "..."

    print "Calculando prioris"
    # prob = getProbabilities(vocabulary)
    print "Concluído"
    print "..."

    print "Fim"

if __name__ == '__main__':
    main()