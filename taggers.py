from os.path import expanduser

# SENNA NLP
home = expanduser("~/senna/")
from nltk.tag.senna import SennaTagger
from nltk.tag.senna import SennaNERTagger
senTag = SennaTagger(home)
senNer = SennaNERTagger(home)

# Stanford NLP
from nltk.tag import StanfordPOSTagger
from nltk.tag import StanfordNERTagger
home_ = expanduser("~/stanford-postagger/")
base = expanduser("~/stanford-ner/")
_path_to_model = home_ + 'models/english-bidirectional-distsim.tagger'
_path_to_jar = home_ + 'stanford-postagger-3.5.2.jar'
stanPOS = StanfordPOSTagger(_path_to_model,path_to_jar=_path_to_jar) 

# NLTK
from nltk import pos_tag, word_tokenize


def stanford_tag(text):
	return stanPOS.tag(text.split())


def nltk_tag(text):
	return pos_tag(word_tokenize(text))


def senna_tag(text):
	return senTag.tag(text.split())