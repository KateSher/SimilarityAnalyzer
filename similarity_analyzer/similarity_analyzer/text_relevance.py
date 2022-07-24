# -*- coding: utf-8 -*-

'''Finding the most relevant documents for the requested keyword according to the TF-IDF criteria.'''


import pickle
import linecache


class RelevantText:

    def __init__(self, path_to_model, path_to_text):
        self.model_path = path_to_model
        self.model = pickle.load(open(self.model_path, 'rb'))
        self.text_path = path_to_text

    def text_relevance_by_word(self, word, num):
        '''
        the method finds a specified number of IDs of documents with the highest values
        of the TF-IDF coefficient for a given keyword, and forms a list of the found IDs.
        word - search keyword;
        num - the number of the most suitable documents (should be num <= 30).
        '''
        if word in self.model:
            # get all the most relevant numbers of texts from word
            all_relevant_texts = self.model.get(word)
            # get IDs of the most relevant 10 texts
            relevant_texts = [all_relevant_texts[i][0] for i in range(num)]
            numbers_of_texts = [int(i.replace('text', '')) for i in relevant_texts]
            return numbers_of_texts
        else:
            return False

    def find_text(self, numbers_list):
        '''
        the method searches and returns articles (ID, title, content) in
        a text file according to a given list of IDs.
        numbers_list - list of text IDs.
        '''
        lines = []
        for i in numbers_list:
            x = linecache.getline(self.text_path, i + 1)
            lines.append(x)
        # convert lines to lists to get number, title and content
        lines_text = []
        for i in ' '.join(lines).split('\n '):
            lines_text.append(i.split(' || '))
        return lines_text
