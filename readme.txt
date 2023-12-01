# Capstone Project Intention Recognition Model

## Overview ----------------------------------------------------------------------------------------------------

This project is an intention recognition model created using SpaCy and scikit-learn. It provides a useful tool for users to identify intentions from input data. Currently the pipeline incorperates a single SVM model utilizing tfidf data. The pipeline can be extended to incorperate other models and data as needed. Currently classifaction results are simply printed to the console however in a production envrionment the ClassificationHandler class of the main.py module can be modified to incorperate output results such as API calls.


## Requirements ----------------------------------------------------------------------------------------------------

To run the main.py module:
- Python 3.x
- joblib

To run the preprocessing.py module:
- Python 3.x
- joblib
- spaCy
- pandas

To run the model_training.py module:
- Python 3.x
- joblib
- spaCy
- pandas
- scikitlearn


## Installation ----------------------------------------------------------------------------------------------------

To set up the model simply store the main.py module, fitted_model.txt, and spacy_nlp.txt in the same directory. For ease of use in customizing the preprossesing and model training components of the pipeline, both the .py and .ipynb files are included in the project directory. Additionally, the Bittext data set has been included in the project files.

To install the required dependencies, run:

pip install joblib
pip install spacy
pip install pandas
pip install scikit-learn

Additionally, install the spaCy language model required for this project. You can use the following command:

python -m spacy download en_core_web_sm


## Project Structure ----------------------------------------------------------------------------------------------------

- `main.py`: Contains the main method to test the intention recognition model through a command line interface. Able to be modified for use in other systems.
- `preprocessing.py`: Refines text and extracts data from dataset. Currently configured for Bittext customer service data sets.
- `model_training`: Implements the intention recognition model using SpaCy and scikit-learn Currently incorperates tfidf with a linear SVM model for classification.

- `spacy_serializer.py`: Small script to serialize a pre-loaded spaCy nlp pipeline object.
- `text_processing.py` : Class used in main.py and preprocessing.py modules to refine text input.


## Usage ----------------------------------------------------------------------------------------------------

Run the main.py module in a python environment to test the model's output via a command line interface.

Integration of the model into a production environment is dependent on the existing IT ifrastructure. Modification of the main.py module can facilitate integration into various customer service software solutions. The ClassificationHandler class can be customized to integrate model output. A custom input method or class would need to be created specifically for the preexisting IT infrastructure.

Customization of the data preprocessing and machine learning modules can be performed as needed. Potential areas of customization include the incorperation of new and or larger datasets as well as the addition of further classification methods. Addition of classification methods would require subsequent modification of the main module to incorperate the model output.


## Contributors ----------------------------------------------------------------------------------------------------

Just me, Logan C.


## Acknowlegements ----------------------------------------------------------------------------------------------------

NLP- Natural Language Processing with Python, Jose Portilla: Udemy course including tfidf and SVM topics used in project.
"Natural Language Processing with Python and Spacy", Yuli Vasiliev: Book covering spaCy and nlp topics.


## License ----------------------------------------------------------------------------------------------------

MIT License

If you choose to use this software (bless you) feel free to use it as you see fit.