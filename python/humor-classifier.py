#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time, sys
import re
import random
import NaiveBayesWordClassifier

# holdout
def separateTrainAndTestGroupsUsingHoldout(csvfile='Sentiment Analysis Dataset.csv', testSetPercentSize=0.3):

    # reading file
    sourceFile = open(csvfile, 'r')
    lines = sourceFile.readlines()

    # removing first line
    lines = lines[1:]

    # sort randonly
    random.shuffle(lines)

    # calculating limit of lines in test file
    testFileLimit = int(testSetPercentSize * len(lines))

    testFile = open('testSetFile.csv', 'w')
    trainFile = open('trainSetFile.csv', 'w')
    
    # populating each file
    cont = 0

    for line in lines:
        if cont<testFileLimit:
            testFile.write(line)
        else:
            trainFile.write(line)
        cont+=1

    sourceFile.close()
    testFile.close()
    trainFile.close()

    return True


# crossvalidation
def separateTrainAndTestGroupsUsingCrossvalidation(csvfile='Sentiment Analysis Dataset.csv', qtdeFolds=10):
    
    # reading file
    sourceFile = open(csvfile, 'r')
    lines = sourceFile.readlines()

    # removing first line
    lines = lines[1:]

    # sort randonly
    random.shuffle(lines)

    # calculating limit of lines in each file
    foldLimit = int(len(lines)/qtdeFolds)

    # opening fold files
    foldDictionary = {}
    for fold in range(1, 1+qtdeFolds):
        filename = 'crossvalidation-{}.csv'.format(fold)
        foldDictionary[fold] = open(filename, 'w')

    # populating each fold file
    cont = 0
    fold = 1
    for line in lines:
        foldDictionary[fold].write(line)
        if cont<foldLimit:
            cont+=1
        else:
            fold+=1
            cont=0

    # closing destination files
    for fold in range(1, 1+qtdeFolds):
        foldDictionary[fold].close()

    # closing source file
    sourceFile.close()

    return True

def readFileToLists(csvfile='trainSetFile.csv'):

    arq = open(csvfile, 'r')
    documents = []

    # reading all lines
    sourceFile = arq.readlines() 

    for line in sourceFile :
        
        # get only 4 columns ignoring comas inside the tweet
        columns = line.split(',', 3)

        # get document number and tweet text in lower case
        document = columns[0]
        sentiment = columns[1]
        text = columns[3].lower()

        # removing 'trashy' characters with regex
        text = re.sub(r'[^0-9a-z\ ]','', text)
        
        documents.append([document, sentiment, text])

    # closing file
    arq.close()

    return documents
    
def main():

    print "Embaralhando dados e separando em conjuntos de treinamento (30% trainSetFile.csv) e teste (70% testSetFile.csv)..."
    separateTrainAndTestGroupsUsingHoldout("../Sentiment Analysis Dataset.csv", 0.3)
    print "Concluído"
    print ""

    print "Lendo o arquivo de treino (trainSetFile.csv) para memória, limpando e preparando..."
    listOfDocuments = readFileToLists("trainSetFile.csv")
    print "Concluído"
    print ""

    print "Criando e treinando o Naive Bayes com o arquivo de treinamento (testSetFile.csv)..."
    nb = NaiveBayesWordClassifier.NaiveBayesWordClassifier()
    nb.train(listOfDocuments)
    print "Concluído"
    print ""

    print "Resultados do treinamento:"
    print "|V| = %s (vocabulário)" % (nb.vocabulary)
    print "Prioris: P(pos) = %.5f" % (float(nb.qtdeDocument['1']) / float(nb.totalDocuments))
    print "         P(neg) = %.5f" % (float(nb.qtdeDocument['0']) / float(nb.totalDocuments))
    print "ni (número total da frequência de palavras de cada classe):"
    print "     n[pos] = %s" % (nb.freq['1'])
    print "     n[neg] = %s" % (nb.freq['0'])
    print "P(wi|ci) - Probabilidade condicional de cada palaavra dada uma classe."
    print "Limitando quantidade de exemplos em 5"
    cont=0
    for word, prob in nb.probability.iteritems():
        cont+=1
        if cont < 6:
            print "    P(%s|pos) = %.10f" % (word, prob['1']) 
            print "    P(%s|neg) = %.10f" % (word, prob['0'])
    print ""

    print "Lendo o arquivo de teste (testSetFile.csv) para memória, limpando e preparando..."
    listOfDocuments = readFileToLists("testSetFile.csv")
    print "Concluído"
    print ""

    print "Testando cada documento do arquivo de teste e contabilizando acertos..."
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
    print "Concluído"
    print ""

    print "Resultados do teste:"
    print "%s acertos em %s documentos" % (hits, len(listOfDocuments))
    print "%.2f %% de acertos" % (100 * float(hits)/float(len(listOfDocuments)))
    print ""

    print "Embaralhando dados e separando em 10 conjuntos (crossvalidation-{1..10}.csv)"
    separateTrainAndTestGroupsUsingCrossvalidation("../Sentiment Analysis Dataset.csv")
    print "Concluído"
    print ""

    print "Fim"
    print ""

if __name__ == '__main__':
    main()

