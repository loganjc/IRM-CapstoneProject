Free, open source Python library for NLP. Likely candidate for most of the project.

[[Install spaCy]]

[Natural Language Processing With Python and spaCy: A Practical Introduction by Yuli Vasiliev PDF](C:\Users\Logan\Documents\Computer Science\Ebooks\Python\naturallanguageprocessingwithpythonandspacy.pdf)
spaCy 101:  https://spacy.io/usage/spacy-101

****
**spaCy** is a multi function library for many differnt NLP related programs in Python. It does not function as a complete chatbot or API not is it a company or some research software.

Pros:
	Container Objects represent linguistic features of words stored within. 
	Pretrained models available in English.
	Built in visualizers for data exploration + analysis.
	Native support for word vectors/ word2vec algorithm.
	Lots of customization options + ability to train model from scratch.
	Interconnectivity to machine learning libraries such as scikit-learn, PyTorch, or TensorFlow.


**Features:**
	In the documentation, you’ll come across mentions of spaCy’s features and capabilities. Some of them refer to linguistic concepts, while others are related to more general machine learning functionality.


**Tokenization**
	Segmenting text into words, punctuations marks etc.

**Part-of-speech** (POS) **Tagging**
	Assigning word types to tokens, like verb or noun.

**Dependency Parsing**
	Assigning syntactic dependency labels, describing the relations between individual tokens, like subject or object.

**Lemmatization**
	Assigning the base forms of words. For example, the lemma of “was” is “be”, and the lemma of “rats” is “rat”.

**Sentence Boundary Detection** (SBD)
	Finding and segmenting individual sentences.

**Named Entity Recognition** (NER)
	Labelling named “real-world” objects, like persons, companies or locations.

**Entity Linking** (EL)
	Disambiguating textual entities to unique identifiers in a knowledge base.

**Similarity**
	Comparing words, text spans and documents and how similar they are to each other.

**Text Classification**
	Assigning categories or labels to a whole document, or parts of a document.

**Rule-based Matching**
	Finding sequences of tokens based on their texts and linguistic annotations, similar to regular expressions.

**Training**
	Updating and improving a statistical model’s predictions.

**Serialization**
	Saving objects to files or byte strings.

![[pipeline.svg]]