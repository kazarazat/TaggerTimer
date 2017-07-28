# Tagger Timer

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

##### Have you ever wanted to time multiple NLP Part-of-Speech taggers with multiprocessor threading to see the resulting tags and their corresponding times to completion? Me too which is why I made this simple program. #####

  - Type or paste your desired text input
  - Run the program
 ```sh
$ python process.py
```
  - Marvel at the results

# Included Taggers

  - NLTK 3.2.1, Stanford POS Tagger and Senna POS Tagger
  - Add more if you like or alter the code to compare Chunkers, NERs, etc

### Tech

Get the libraries and data for the taggers I used here:

* [Stanford POS Tagger](https://nlp.stanford.edu/software/tagger.html) - The Stanford NLP Group
* [Senna Tagger](https://ronan.collobert.com/senna/) - Senna Tag developed by Ronan Collobert

### Installation

You probably already have nltk but just in case

```sh
$ pip install nltk
```

Inside the process.py file pay close attentio to the pathing for the libraries

**Senna Tag**
```sh
home = expanduser("~/senna/")
from nltk.tag.senna import SennaTagger
senTag = SennaTagger(home)
```
**Stanford Tag**
```sh
home_ = expanduser("~/stanford-postagger/")
from nltk.tag import StanfordPOSTagger
_path_to_model = home_ + 'models/english-bidirectional-distsim.tagger'
_path_to_jar = home_ + 'stanford-postagger-3.5.2.jar'
stanPOS = StanfordPOSTagger(_path_to_model,path_to_jar=_path_to_jar) 
```
### My Input
```sh
sentence = ("All truth passes through three stages. First, "
			"it is ridiculed. Second, it is violently opposed. "
			"Third, it is accepted as being self-evident. "
			"- Arthur Schopenhauer (1788-1860) ")
```
### My Output

```sh
NLTK Tagging: starting
Senna Tagging: starting
Stanford Tagging: starting

Senna Tagging: finishing
tags:[('All', u'DT'), ('truth', u'NN'), ('passes', u'VBZ'), ('through', u'IN'), ('three', u'CD'), ('stages.', u'NNS'), ('First,', u'NNP'), ('it', u'PRP'), ('is', u'VBZ'), ('ridiculed.', u'JJ'), ('Second,', u'NNP'), ('it', u'PRP'), ('is', u'VBZ'), ('violently', u'RB'), ('opposed.', u'JJ'), ('Third,', u'NN'), ('it', u'PRP'), ('is', u'VBZ'), ('accepted', u'VBN'), ('as', u'IN'), ('being', u'VBG'), ('self-evident.', u'NN'), ('-', u':'), ('Arthur', u'NNP'), ('Schopenhauer', u'NNP'), ('(1788-1860)', u'.')] 
time: 0.539201974869

NLTK Tagging: finishing
tags:[('All', 'DT'), ('truth', 'NN'), ('passes', 'NNS'), ('through', 'IN'), ('three', 'CD'), ('stages', 'NNS'), ('.', '.'), ('First', 'NNP'), (',', ','), ('it', 'PRP'), ('is', 'VBZ'), ('ridiculed', 'VBN'), ('.', '.'), ('Second', 'JJ'), (',', ','), ('it', 'PRP'), ('is', 'VBZ'), ('violently', 'RB'), ('opposed', 'VBN'), ('.', '.'), ('Third', 'NNP'), (',', ','), ('it', 'PRP'), ('is', 'VBZ'), ('accepted', 'VBN'), ('as', 'IN'), ('being', 'VBG'), ('self-evident', 'JJ'), ('.', '.'), ('-', ':'), ('Arthur', 'NNP'), ('Schopenhauer', 'NNP'), ('(', '('), ('1788-1860', 'CD'), (')', ')')] 
time: 1.40881919861

Stanford Tagging: finishing
tags:[(u'All', u'DT'), (u'truth', u'NN'), (u'passes', u'VBZ'), (u'through', u'IN'), (u'three', u'CD'), (u'stages.', u'FW'), (u'First,', u'FW'), (u'it', u'PRP'), (u'is', u'VBZ'), (u'ridiculed.', u'FW'), (u'Second,', u'FW'), (u'it', u'PRP'), (u'is', u'VBZ'), (u'violently', u'RB'), (u'opposed.', u'FW'), (u'Third,', u'FW'), (u'it', u'PRP'), (u'is', u'VBZ'), (u'accepted', u'VBN'), (u'as', u'IN'), (u'being', u'VBG'), (u'self-evident.', u'NN'), (u'-', u':'), (u'Arthur', u'NNP'), (u'Schopenhauer', u'NNP'), (u'(1788-1860)', u'CD')] 
time: 4.33212590218
```


### Pay it Forward
If this saves you a little work please don't forget to star.



