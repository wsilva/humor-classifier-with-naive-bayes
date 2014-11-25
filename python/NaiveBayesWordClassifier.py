#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def classificador(self,document):
        pass








        