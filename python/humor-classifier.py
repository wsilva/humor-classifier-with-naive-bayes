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

    print "Lendo o arquivo de treino (trainSetFile.csv) para memória, limpando e preparando..."
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
    cont=0
    for word, prob in nb.probability.iteritems():
        cont+=1
        if cont < 6:
            print "    P(%s|pos) = %s" % (word, prob['1']) 
            print "    P(%s|neg) = %s" % (word, prob['0'])

    print "Limitando quantidade de exemplos em 5 (usando laplace para evitar frequência zerada)"
    print "Concluído"
    print "..."

    print "Lendo o arquivo de teste (testSetFile.csv) para memória, limpando e preparando..."
    listOfDocuments = readFileToLists("testSetFile.csv")
    print "Concluído"
    print "..."

    print "Testando cada documento lido..."
    hits = 0 #contador de acertos
    
    for doc in listOfDocuments:

        # attributes from the list
        document = doc[0]
        sentiment = doc[1]
        tweet = doc[2]
        identifiedClass = nb.classificator(tweet)
        
        # counting the right hits
        if sentiment==identifiedClass:
            hits+=1

    print "%s acertos em %s documentos" % (hits, len(listOfDocuments))
    print "%.2f %% de acertos" % (100 * float(hits)/float(len(listOfDocuments)))

    print "..."
    print "..."
    print "Fim"

if __name__ == '__main__':
    main()