from joblib import load
import text_processing
'''
This module is the Main module which actually produces a category as output in response to novel text input.

The module utilizes serialized pipeline and ML components to prevent the need for the user to have the datasets and
SpaCy language libraries.

Currently the module runs a simple command line interface test method which allows a user to test the output of the model
in response to manually inputted novel text.
'''

#Load in serialized spacy pipeline and trained models
nlp = load("spacy_nlp.txt")
tfidf_lsvc = load("fitted_model.txt")

input_processor = text_processing.Text_Pre_Processor(nlp)

#Takes text input, returns output category as a text string
class Categorizer:
    '''
    
    
    '''
    def process_input_text(text):
        #treat incoming text
        doc = input_processor.process(text)
        lemmas = []
        for token in doc:
            lemmas.append(token.text)
        output_text = " ".join(lemmas)
        output_text = [output_text]
        #collect model predictions
        tfidf_lsvc_prediction = tfidf_lsvc.predict(output_text)
        #compare predictions
        
        #output prediciton
        return tfidf_lsvc_prediction[0]


class ClassificationHandler:
    '''
    Class to process results of categorization.
    Currently methods are stubs to demonstrate the structure of the class.
    Proper implementation of class in business software would likely place API calls to ticketing or response system here.
    
    Methods:
    process_classification
    '''
    def process_classification(category):
        if category == "ORDER":
            #handling code here
            print("Category: Order")
        elif category == "SHIPPING_ADDRESS":
            #handling code here
            print("Category: Shipping address")
        elif category == "CANCELLATION_FEE":
            #handling code here
            print("Category: Cancellation fee")
        elif category == "INVOICE":
            #handling code here
            print("Category: Invoice")
        elif category == "PAYMENT":
            #handling code here
            print("Category: Payment")
        elif category == "REFUND":
            #handling code here
            print("Category: Refund")
        elif category == "FEEDBACK":
            #handling code here
            print("Category: Feedback")
        elif category == "CONTACT":
            #handling code here
            print("Category: Contact")
        elif category == "ACCOUNT":
            #handling code here
            print("Category: Account")
        elif category == "DELIVERY":
            #handling code here
            print("Category: Delivery")
        elif category == "NEWSLETTER":
            #handling code here
            print("Category: Newsletter")
        else:
            #Not categorized code here
            print("Category: Unknown category")

#This method launches a command line interface to test the output of the pipeline.
def cli_test_mode():
    text = ''
    print('Please provide text input to test classification. Type \"exit\" to stop.')
    while text != 'exit':
        text = input('Enter text here: ')
        category = Categorizer.process_input_text(text)
        ClassificationHandler.process_classification(category)
        
cli_test_mode()

