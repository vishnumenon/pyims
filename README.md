# PyIMS

A simple python wrapper around the IMS (It Makes Sense) word-sense disambiguation toolkit, that integrates it with NLTK's WordNet interface. Requires IMS to be downloaded separately, which requires a working Java installation. Also requires NLTK with WordNet downloaded. Only tested in Linux, might not work in other OSes. Built for python 3.6+

## Installation

First, follow the instructions in [Section 3 of the IMS Readme](https://raw.githubusercontent.com/NUNLP/ims/master/README.txt) to install the components of IMS into some directory; extract the models from [here](http://www.comp.nus.edu.sg/~nlp/corpora.html#onemilwsd) (step 3.e) into the same directory as in steps 3.b and 3.c. Then, run:

```
pip install pyims
```

## Usage

```python
from pyims import PyIMS

wsd = PyIMS("path/to/ims", "modelsDirName")
print(wsd.disambiguate("I am interested in the interest rates at the bank.", probs=True, synsets=False))

# If probs=True, returns a list of (token, probability_distribution) tuples where probability_distribution is a map of lemma to its probability
# If probs=False (default False), returns a list of (token, lemma) where lemma is the most probable word-sense in WordNet for the given token
# If synsets=True, lemmas are replaced with the Synsets to which they belong
# If synsets=False (default False), to access a lemma's synset, call lemma.synset()
```

## References

* Zhong, Zhi and Ng, Hwee Tou. 2010. It Makes Sense: A Wide-Coverage Word Sense Disambiguation System for Free Text. In Proceedings of the ACL 2010 System Demonstrations, pages 78--83, Uppsala, Sweden
