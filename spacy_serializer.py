#Script to create a serialized version of a loaded SpaCy nlp model.
from joblib import dump
import spacy

nlp = spacy.load('en_core_web_md')
with open('spacy_nlp.txt', 'wb') as f:
    dump(nlp, f)