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
        
        self.stopWordsList = ['a', 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'adopted', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came', 'can', 'cannot', 'cant', 'canot', 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', 'didnt', 'didnot', 'different', 'do', 'does', 'doesnt', 'doesnot', 'doing', 'done', 'dont', 'donot', 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', 'hasnt', 'hasnot', 'have', 'havent', 'havenot', 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', 'i', 'id', 'ie', 'if', 'ill', 'iwill', 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is', 'isnt', 'isnot', 'it', 'itd', 'itll', 'itwill', 'its', 'itself', 'ive', 'ihave', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'keys', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', 'll', 'will', 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', 'shell', 'shewill', 'shes', 'should', 'shouldnt', 'shouldnot', 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'state', 'states', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 't', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'thatll', 'thatwill', 'thats', 'thatve', 'thathave', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'therell', 'therewill', 'thereof', 'therere', 'theres', 'thereto', 'thereupon', 'thereve', 'therehave', 'these', 'they', 'theyd', 'theyll', 'theywill', 'theyre', 'theyve', 'theyhave', 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', 've', 'have', 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'wasnot', 'way', 'we', 'wed', 'welcome', 'well', 'wewill', 'went', 'were', 'werent', 'werenot', 'weve', 'wehave', 'what', 'whatever', 'whatll', 'whatwill', 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl', 'whowill', 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', 'wont', 'wonot', 'words', 'world', 'would', 'wouldnt', 'wouldnot', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', 'youll', 'youwill', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'youve', 'youhave', 'z', 'zero']

    def train(self, listOfDocuments, removeStopWords=False):
        
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

                if removeStopWords==True and w in self.stopWordsList:
                    pass
                else:
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



    def classificator(self, document, removeStopWords=False):

        # to calculate P(ci|w)
        probability_pos = math.log(float(self.qtdeDocument['1']) / float(self.totalDocuments))
        probability_neg = math.log(float(self.qtdeDocument['0']) / float(self.totalDocuments))

        # getting the words from the current document
        words = document.split()

        for w in words:

            if removeStopWords==True and w in self.stopWordsList:
                pass
            else:
                # if the word exists in train data we use it to calculate P(ci|w)
                if w in self.probability:
                    probability_pos += math.log(self.probability[w]['1'])
                    probability_neg += math.log(self.probability[w]['0'])


        if probability_pos > probability_neg:
            return "1"
        return "0"

