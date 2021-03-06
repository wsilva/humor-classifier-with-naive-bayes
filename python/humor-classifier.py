#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time, sys, itertools, math
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

def holdoutFlow(removeStopWords=False):
    trainSizePercent = 0.3
    print "Embaralhando dados e separando em conjuntos de treinamento (%d%% trainSetFile.csv) e teste (%d%% testSetFile.csv)..." % ((100*trainSizePercent), (1-trainSizePercent)*100)
    separateTrainAndTestGroupsUsingHoldout("../Sentiment Analysis Dataset.csv", 0.3)
    print "Concluído"
    print ""

    print "Lendo o arquivo de treino (trainSetFile.csv) para memória, limpando e preparando..."
    listOfDocuments = readFileToLists("trainSetFile.csv")
    print "Concluído"
    print ""

    print "Criando e treinando o Naive Bayes com o arquivo de treinamento (testSetFile.csv)..."
    nb = NaiveBayesWordClassifier.NaiveBayesWordClassifier()
    nb.train(listOfDocuments, removeStopWords)
    print "Concluído"
    print ""

    print "Resultados do treinamento:"
    print "|V| = %s (vocabulário)" % (nb.vocabulary)
    print "Prioris: P(pos) = %.5f" % (float(nb.qtdeDocument['1']) / float(nb.totalDocuments))
    print "         P(neg) = %.5f" % (float(nb.qtdeDocument['0']) / float(nb.totalDocuments))
    print "ni (número total da frequência de palavras de cada classe):"
    print "     n[pos] = %s" % (nb.freq['1'])
    print "     n[neg] = %s" % (nb.freq['0'])
    print "P(wi|ci) - Probabilidade condicional de cada palavra dada uma classe."
    print "Limitando quantidade de exemplos em 2"
    cont=0
    for word, prob in nb.probability.iteritems():
        cont+=1
        if cont < 3:
            print "    P(%s|pos) = %.10f" % (word, prob['1']) 
            print "    P(%s|neg) = %.10f" % (word, prob['0'])
    print ""

    print "Lendo o arquivo de teste (testSetFile.csv) para memória, limpando e preparando..."
    listOfDocuments = readFileToLists("testSetFile.csv")
    print "Concluído"
    print ""

    print "Testando cada documento do arquivo de teste e contabilizando acertos..."
    hits = 0 #contador de acertos
    miss = 0 #contador de erros
    posPos=0
    posNeg=0
    negPos=0
    negNeg=0

    for doc in listOfDocuments:

        # attributes from the list
        document = doc[0]
        sentiment = doc[1]
        tweet = doc[2]
        identifiedClass = nb.classificator(tweet, removeStopWords)
        
        # counting the right hits
        if sentiment==identifiedClass:
            hits+=1
            if sentiment=='1':
                posPos+=1
            else:
                negNeg+=1
        else:
            miss+=1
            if sentiment=='1':
                posNeg+=1
            else:
                negPos+=1

    print "Concluído"
    print ""

    print "Resultados do teste:"
    print "%s acertos em %s documentos" % (hits, len(listOfDocuments))
    print "%.2f %% de acertos" % (100 * float(hits)/float(len(listOfDocuments)))
    print "%.2f %% de erros" % (100 * float(miss)/float(len(listOfDocuments)))
    print "+-----+---------+---------+"
    print "|     |   POS   |   NEG   |"
    print "+-----+---------+---------+"
    print "| POS | %07d | %07d |" % (posPos, posNeg)
    print "| NEG | %07d | %07d |" % (negPos, negNeg)
    print "+-----+---------+---------+"
    print ""

def crossvalidationFlow(removeStopWords=False):
    qtdeFolds = 10
    print "Embaralhando dados e separando em %s conjuntos (crossvalidation-{1..%s}.csv)" % (qtdeFolds, qtdeFolds)
    separateTrainAndTestGroupsUsingCrossvalidation("../Sentiment Analysis Dataset.csv", qtdeFolds)
    print "Concluído"
    print ""

    print "Preparando as rodadas de crossvalidation"
    trainList={}
    testList={}
    for j in range(1, 1+qtdeFolds):
        print "   Rodada %s do crossvalidation" % j
        for i in range(1, 1+qtdeFolds):
            filename = 'crossvalidation-{}.csv'.format(i)
            tmpList = readFileToLists(filename)
            if i==j:
                testList[j] = tmpList
                print "   Arquivo %s separado para teste" % filename
            else:
                if j in trainList:
                    trainList[j] = itertools.chain(trainList[j], tmpList)
                else:
                    trainList[j] = tmpList
                # print "Arquivo %s separado para treino" % filename
    print "Concluído"
    print ""

    print "Usando o naive bayes nas rodadas do crossvalidation"
    hitsList=[]
    missList=[]
    for i in range(1,1+qtdeFolds):
        print "   Treinamento número %s" % i
        nb = NaiveBayesWordClassifier.NaiveBayesWordClassifier()
        nb.train(trainList[i], removeStopWords)

        hits = 0 #contador de acertos
        miss = 0 #contador de acertos
        print "   Teste número %s" % i
        for doc in testList[i]:

            # attributes from the list
            document = doc[0]
            sentiment = doc[1]
            tweet = doc[2]
            identifiedClass = nb.classificator(tweet, removeStopWords)
            
            # counting the right hits
            if sentiment==identifiedClass:
                hits+=1
            else:
                miss+=1
        
        hitsPercent = 100 * float(hits)/float(len(testList[i]))
        missPercent = 100 * float(miss)/float(len(testList[i]))
        print "   Acuracia: %.2f %%" % hitsPercent
        print "   Erro: %.2f %%" % missPercent

        hitsList.append(hitsPercent)
        missList.append(missPercent)

        avgHits = sum(hitsList) / float(len(hitsList))
        avgMiss = sum(missList) / float(len(missList))

        summary = 0
        for i in hitsList:
            summary = summary + ((i-avgHits)*(i-avgHits))
        desvioPadraoHits = math.sqrt(summary / float(len(hitsList)))

        summary = 0
        for i in missList:
            summary = summary + ((i-avgMiss)*(i-avgMiss))
        desvioPadraoMiss = math.sqrt(summary / float(len(missList)))


    print "Média de acertos: %.2f %% com desvio padrão de %.2f" % (avgHits, desvioPadraoHits)
    print "Média de erros: %.2f %% com desvio padrão de %.2f" % (avgMiss, desvioPadraoMiss)
    print ""
    
def main():

    print "================= Holdout =================="
    holdoutFlow() 

    print "======= Holdout removendo stop words ======="
    holdoutFlow(True)    

    print "============= Cross Validation =============="
    crossvalidationFlow()

    print "=== Cross Validation removendo stop words ==="
    crossvalidationFlow(True)

    print "Concluído"
    print ""

    print "Fim"
    print ""

if __name__ == '__main__':
    main()

# 