#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class NaiveBayesWordClassifier(object):

    def __init__(self):
        
        self.qtdeDocument = {'0': 0, '1': 0}
        self.totalDocuments = 0

        self.word = {}
        self.freq = {'0': 0, '1': 0}
        self.probability = {}

        self.vocabulary = 0

    def getDocsPos(self):
        return self.qtdeDocument['1']

    def getDocsNeg(self):
        return self.qtdeDocument['0']

    def getTotalDocs(self):
        return self.totalDocuments

    def train(self, listOfDocuments):
        
        # listing documents 
        for doc in listOfDocuments:

            # attributes from the list
            document = doc[0]
            sentiment = doc[1]
            tweet = doc[2]

            # updating total documents and amount of each sentiment
            self.totalDocuments+=1
            self.qtdeDocument[sentiment]+=1

            # getting the words from the current document
            words = tweet.split()

            for w in words:

                # if the word does not exist we initialize
                if w not in self.word:
                    self.word[w] = {'0': 0, '1': 0}
                    self.vocabulary+=1

                # update times a word appeard on each class
                self.word[w][sentiment]+=1

                # updating frequency of words in each class
                self.freq[sentiment]+=1

        # calculating probabilities
        for word,qtde in self.word.iteritems():
            self.probability[word] = {}
            self.probability[word]['1'] = (1 + float(qtde['1'])) / (float(self.vocabulary) + float(self.freq['1']))
            self.probability[word]['0'] = (1 + float(qtde['0'])) / (float(self.vocabulary) + float(self.freq['0']))



    def classificator(self, document):

        # to calculate P(ci|w)
        probability_pos = math.log(float(self.qtdeDocument['1']) / float(self.totalDocuments))
        probability_neg = math.log(float(self.qtdeDocument['0']) / float(self.totalDocuments))

        # getting the words from the current document
        words = document.split()

        for w in words:

            # if the word exists in train data we use it to calculate P(ci|w)
            if w in self.probability:
                probability_pos += math.log(self.probability[w]['1'])
                probability_neg += math.log(self.probability[w]['0'])
        if probability_pos > probability_neg:
            return "1"
        return "0"

