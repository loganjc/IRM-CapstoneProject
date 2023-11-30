class Text_Pre_Processor:
    '''
    Prepare dataframe for use in Tf-id and semantic similarity comparison. 
    
    Args: 
    nlp= initialized spaCy 
    df = labeled + formatted pandas dataframe
    
    Output: 
    Doc object with lemmatized text version of input without punct or stop words
    
    Methods:
    remove_punct(self, text)
    stop_word_removal(self, text)
    lemmatization(self, doc)
    process(self, text)
    '''

    def __init__(self, nlp):
        self.nlp = nlp
     
    #input string, remove punct, return new string
    def remove_punct(self, text):
        # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        #string.punctuation
        text = text.translate(str.maketrans('','','!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
        return text
        
    #input text, remove text, return new doc.
    def stop_word_removal(self, text):
        doc = self.nlp(text)
        stop_word_index = []
        for index, token in enumerate(doc):
            if token.text.lower() in self.nlp.Defaults.stop_words:
                stop_word_index.append(index)
        filtered_tokens = [token.text for i,token in enumerate(doc) if i not in stop_word_index]
        doc = self.nlp(' '.join(filtered_tokens))
        return doc
        
    #input doc, return lemmatized doc
    def lemmatization(self, doc):
        lemmas = ''
        for token in doc:
            lemmas = lemmas + (token.lemma_) + ' '
        return self.nlp(lemmas)
        
    #Perform all processing on text input
    def process(self, utterance):
        text = self.remove_punct(utterance)
        doc = self.stop_word_removal(text)
        doc = self.lemmatization(doc)
        return doc