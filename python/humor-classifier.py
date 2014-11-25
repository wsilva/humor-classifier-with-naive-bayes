#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import random
import NaiveBayesWordClassifier

def separateTrainAndTestGroups(csvfile='Sentiment Analysis Dataset.csv', testSetPercentSize=0.3):
    
    try:
        # open database file and sort it 'randomly'
        with open(csvfile, 'r') as source:
            data = [ (random.random(), line) for line in source ]
        data.sort()

        # getting the limit of lines inside trainning file
        trainSetPercentSize = 1 - testSetPercentSize
        trainSetLimitLines = trainSetPercentSize * len(data)

        # writting 2 files with trainSet and testSet based on limit lines on each
        cont = 0
        with open('trainSetFile.csv', 'w') as trainFile, open('testSetFile.csv', 'w') as testFile:
            for _, line in data:

                # bypassing file header
                if 'ItemID,Sentiment,SentimentSource,SentimentText' not in line:
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
        documents = []

        # ignoring first line due to header with label
        txt = arq.readlines()[1:] 

        for linha in txt :
            
            # get only 4 columns ignoring comas inside the tweet
            lista = linha.split(',', 3)
            document = lista[0]
            text = lista[3].lower()

            # removing 'trashy' characters with regex
            text = re.sub(r'[^0-9a-z\ ]','', text)
            sentiment = lista[1]
            
            documents.append([document, sentiment, text])

        arq.close()
        return documents
        
    except IOError as e:
        arq.close()
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        arq.close()
        print "Unexpected error:", sys.exc_info()[0]
        raise

def main():

    print "Embaralhando dados e separando em conjuntos de treinamento (trainSetFile.csv) e teste (testSetFile.csv)..."
    separateTrainAndTestGroups("../Sentiment Analysis Dataset.csv", 0.3)
    print "Concluído"
    print "..."

    print "Lendo o arquivo de treino para memória e preparando..."
    listOfDocuments = readFileToLists("trainSetFile.csv")
    print "Concluído"
    print "..."

    print "Criando e treinando o Naive Bayes com o arquivo de treinamento..."
    nb = NaiveBayesWordClassifier.NaiveBayesWordClassifier()
    nb.train(listOfDocuments)
    print "|V| = %s (vocabulário)" % (nb.vocabulary)
    print "Prioris: P(pos) = %s" % (float(nb.qtdeDocument['1']) / float(nb.totalDocuments))
    print "         P(neg) = %s" % (float(nb.qtdeDocument['0']) / float(nb.totalDocuments))
    print "ni (número total da frequência de palavras de cada classe):"
    print "     n[pos] = %s" % (nb.freq['1'])
    print "     n[neg] = %s" % (nb.freq['0'])
    print "P(wi | ci) - Probabilidade condicional de uma palavra dada uma classe."
    cont=1
    for key,value in nb.word.iteritems():
        cont+=1
        if cont < 7:
            print "    P(%s|pos) = %s" % (key, (1 + float(value['1'])) / (nb.vocabulary + float(nb.freq['1']))) # with laplace
            print "    P(%s|neg) = %s" % (key, (1 + float(value['0'])) / (nb.vocabulary + float(nb.freq['0']))) # with laplace
    print "Limitando quantidade de exemplos em 5 (usando laplace para evitar frequência zerada)"
    print "Concluído"
    print "..."

    # print "Montando Vocabulário"
    # # vocabulary = setupVocabulary(twittes)
    # print "Concluído"
    # print "..."

    # print "Calculando prioris"
    # # prob = getProbabilities(vocabulary)
    # print "Concluído"
    # print "..."

    print "Fim"

if __name__ == '__main__':
    main()