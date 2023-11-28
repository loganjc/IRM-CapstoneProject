*******
**Default doc object creation:** 
*****
import spacy

nlp = spacy("en_core_web_sm") 
*#this is the statistical model [[Install spaCy|downloaded]] earlier*.

doc = nlp(u'Some string input goes here.')
*#this creates the doc object which contains tokens.*
*******

At this point we can begin to perform various analysis of the tokens, look at POS tags, dependency tags, etc.

****
*#lemmas*
for token in doc:
	print(token.text, token.lemma_)
*****
