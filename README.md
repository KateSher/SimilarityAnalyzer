# Document similarity analyzer by keywords based on the TF-IDF criterion

Purpose: to develop a model that allows you to compare documents by the weight of a given keyword in them in accordance with the TF-IDF criterion.

## Usage
By sequentially working with the notebooks listed below, you can get your TF-IDF model to work with your Wikipedia dump.

## Content:

### 1_Preparing_the_Сorpus.ipynb
A notebook that downloads a Wikipedia dump and converts it from XML format to a text file.

### 2_Preprocessing_texts.ipynb
In this notebook, the text is preprocessed using regular expressions and tokenized using SpaCy.

### 3_Stopwords_Сleaning.ipynb
This notebook creating a dictionary of unique words by Gensim to get a list of stopwords (including non-English words). The text is cleaning from stopwords in SpaCy.

### 4_TF-IDF_vectorization_Gensim.ipynb
In notebook creating a dictionary of unique words by Gensim from texts that have been cleared of stopwords. Dictionary is additionally filtering from typos and rare words. Creating and training  TF-IDF model.

### 5_Adding_textIDs_in_TF-IDF_model.ipynb
Adding IDs of texts in TF-IDF model.

### 6_Creating_Batches_of_the_TF-IDF_dictionary.ipynb
This notebook creates dictionaries for each keyword from a dictionary of unique words. The keywords are the keys of the dictionaries, and the values are the IDs of the documents (texts) and the weights of the corresponding documents. The dictionary is created in 4 batches.

### 7_Processing_Batches_of_the_TF-IDF_dictionary.ipynb
Sorting and cutting up to 30 values of each dictionary. Saving 4 batches of the dictionary.

### 8_Complete_TF-IDF_model.ipynb
In a notebook compiling 4 batches of the dictionary into one whole, that is getting complete TF-IDF model.

### 9_Preparing_the_Corpus_for_Library.ipynb
In this notebook, we get a text file that will be used to search and print documents called by IDs.

### Example.ipynb
An example of the work of the created package **similarity_analyzer**. 
The [model](https://drive.google.com/file/d/1EfPDXJPvU4xli1mnJznwgusOuAoTUmpW/view?usp=sharing) and the [text file](https://drive.google.com/file/d/1JEADRYcLNeuIO3-k4L7Uk9slzl22Tnmx/view?usp=sharing) are on google drive.

### requirements.txt
List of all dependencies for notebooks.

### similarity_analyzer
A package based on the library (**text_relevance.py**) for searching document IDs by TF-IDF criteria.