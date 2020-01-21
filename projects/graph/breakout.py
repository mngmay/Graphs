'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
'''

from graph import Graph
from timeit import default_timer as timer

words = []
with open('words.txt', 'r') as wordsfile:
    for word in wordsfile:
        currentWord = word[:-1]
        words.append(currentWord)



def transform(begin_word, end_word):
    start = timer()
    if len(begin_word) != len(end_word):
        return None
# get words that are the same length as the beginning word to rule out irrelevant sized words
    valid_words = [word.lower() for word in words if len(word) == len(begin_word)]
# create graph with valid words 
    word_graph = Graph()
    for word in valid_words:
        word_graph.add_vertex(word)

# create edge between words if there's a 1 letter difference 
    for word in valid_words:
        for reviewed in valid_words:
            if word != reviewed and sum(a!=b for a,b in zip(word, reviewed)) == 1:
                word_graph.add_edge(word, reviewed)

# call bfs to find the shortest path
    print("Path found in:" + str(timer() - start))
    return word_graph.bfs(begin_word, end_word)
        


print(transform("sail", "boat"))
print(transform("hit", "cog"))
print(transform("hungry", "happy"))