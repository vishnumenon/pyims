import subprocess
import os
import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from queue import Queue
from threading import Thread



# Not declared as an instance method to allow for pickling, because want to switch to multitprocessing later
def get_probabilities(dist_str, find_synsets):
    _, *senses = dist_str.split()
    senses_dist = {}
    for sense in senses:
        k, v = sense.split("|")
        v = float(v)
        try:
            k = wn.lemma_from_key(k)
        except nltk.corpus.reader.wordnet.WordNetError:
            k = None
        if find_synsets and k is not None:
            k = k.synset()
        if k in senses_dist:
            senses_dist[k] += float(v)
        else:
            senses_dist[k] = float(v)
    return senses_dist

def disambiguate_helper(script_path, models_dir, sense_path, ims_path, text, probs, synsets):
    ims_proc = subprocess.run(
        [script_path, models_dir, "/dev/stdin", "/dev/stdout", sense_path, "0", "0", "0", "0"],
        cwd=ims_path,
        input=text,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    doc_root = ET.fromstring("<root>" + ims_proc.stdout + "</root>")
    output = []
    if doc_root.text is not None:
        for tok in word_tokenize(doc_root.text):
            output.append((tok, None))
    for child in doc_root:
        senses = get_probabilities(child.attrib["length"], synsets)
        output.append((child.text, senses if probs else max(senses.keys(), key=lambda k: senses[k])))
        if child.tail is not None:
            for tok in word_tokenize(child.tail):
                output.append((tok, None))
    return output

def disambiguate_async_helper(q, script_path, models_dir, sense_path, ims_path, text, probs, synsets):
    output = disambiguate_helper(script_path, models_dir, sense_path, ims_path, text, probs, synsets)
    q.put(output)
    return

class PyIMS():
    def __init__(self, ims_path, models_dir):
        self.__ims_path = ims_path
        self.__models_dir = models_dir
        self.__script_path = os.path.join(ims_path, "testPlain.bash")
        self.__sense_path = os.path.join("lib", "dict", "index.sense")

    def disambiguate(self, text, probs=False, synsets=False):
        return disambiguate_helper(self.__script_path, self.__models_dir, self.__sense_path, self.__ims_path, text, probs, synsets)

    def disambiguate_async(self, text, probs=False, synsets=False):
        q = Queue(maxsize=0)
        t = Thread(target=disambiguate_async_helper, args=(q, self.__script_path, self.__models_dir, self.__sense_path, self.__ims_path, text, probs, synsets))
        t.start()
        return q
