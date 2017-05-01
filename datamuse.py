#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:19:49 2017

@author: huseyin
"""

import requests
import re

"""

rel_[code]: code parameter should be a list
jja 	Popular nouns modified by the given adjective, per Google Books Ngrams 	gradual → increase
jjb 	Popular adjectives used to modify the given noun, per Google Books Ngrams 	beach → sandy
syn 	Synonyms (words contained within the same WordNet synset) 	ocean → sea
trg 	"Triggers" (words that are statistically associated with the query word in the same piece of text.) 	cow → milking
ant 	Antonyms (per WordNet) 	late → early
spc 	"Kind of" (direct hypernyms, per WordNet) 	gondola → boat
gen 	"More general than" (direct hyponyms, per WordNet) 	boat → gondola
com 	"Comprises" (direct holonyms, per WordNet) 	car → accelerator
par 	"Part of" (direct meronyms, per WordNet) 	trunk → tree
bga 	Frequent followers (w′ such that P(w′|w) ≥ 0.001, per Google Books Ngrams) 	wreak → havoc
bgb 	Frequent predecessors (w′ such that P(w|w′) ≥ 0.001, per Google Books Ngrams) 	havoc → wreak
rhy 	Rhymes ("perfect" rhymes, per RhymeZone) 	spade → aid
nry 	Approximate rhymes (per RhymeZone) 	forest → chorus
hom 	Homophones (sound-alike words) 	course → coarse
cns 	Consonant match 	sample → simple"""

"""
parameters
ml(means-like): require that the results have a meaning related to this string value, which can be any word or sequence of words.

sl(sounds-like):require that the results are pronounced similarly to this string of characters. 
(If the string of characters doesn't have a known pronunciation, the system will make its best 
guess using a text-to-phonemes algorithm.) 

sp(spelled-like):  A pattern can include any combination of alphanumeric characters, spaces, 
and two reserved characters that represent placeholders — * (which matches any number of characters) 
and ? (which matches exactly one character). 
    
code: dictionary({jja : word ...}), require that the results, when paired with the word in this parameter, are in a predefined lexical relation indicated by [code].
Any number of these parameters may be specified any number of times.(theese code are explained above)

v(vocabulary): Identifier for the vocabulary to use

topics (Topic words): An optional hint to the system about the theme of the document being written

max: Maximum number of results to return
md 	Metadata flags: A list of single-letter codes (no delimiter) requesting
that extra lexical knowledge be included with the results.
"""


def search_datamuse_wordenp(ml, sl=None, sp=None, code=None, max_res=100, v=None ):  # did not understand qe
    #md = '&md=f'  # meta data, hardwired to word part of speech
    ml = re.sub(" ", "+", ml)  # change spaces w/ +
    req_base = "https://api.datamuse.com/words?max=" + str(max_res) + '&'
    req_base = req_base + "ml=" + ml

    # can be used for rhymes
    if sl is not None:
        req_base = req_base + '&sl=' + sl

    # known letters / unknown letters
    if sp is not None:
        req_base = req_base + '&sp=' + sp

    # related word codes as given above
    # code is a list
    code_string = ''
    if code is not None:
        for key, item in code.items():
            code_string = code_string + "&rel_" + key + "=" + item

    req_addr = req_base + code_string # + md

    # vocabulary used
    if v is not None:
        req_addr = req_addr + '&v=' + v

    print(req_addr)

    r = requests.get(req_addr)
    json_data = r.json()
    return json_data


# there may not be a need for this
def wiki_search(ml, sl=None, sp=None, code=None, max_res=100, qe=None):
    len = ""
    for i in range(word_len):
        len += '?'
    ans_list = search_datamuse_wordenp(ml, sl, len,code, max_res, v='enwiki')
    for el in answer_list:
        el.pop("tags")
    return ans_list

# autocomplete
def search_datamuse_sug(s, max_res):
    req_base = "https://api.datamuse.com/sug?"
    req_addr = req_base + 's=' + s + '&max=' + str(max_res)
    r = requests.get(req_addr)


def datamuse_answer_list(clue, word_length):
    len = ""
    for i in range(word_length) :
        len += '?'
    ans_list = search_datamuse_wordenp(clue, max_res=10, sp=len)
    for el in ans_list:
        el.pop("tags")
    return ans_list





