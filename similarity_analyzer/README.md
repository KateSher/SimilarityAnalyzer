# similarity_analyzer

**similarity_analyzer** - document similarity analyzer by keywords based on the TF-IDF criterion. This module is a Python library that allows you to compare documents by the weight of a given keyword in them in accordance with the TF-IDF criterion. For the requested keyword, you can get IDs of the most weighty texts in descending order of the TF-IDF coefficient, and also print texts based on the found IDs.

## Installation

Install the current version:
```python
pip install from similarity_analyzer-0.1.0-py3-none-any.whl
```
## Usage

You can enter a keyword and a number between 1 and 30 to get the IDs of the most significant documents. Found IDs will be displayed in the form of a list of numbers, according to which you can display the corresponding articles.

## Example

You need to import the library like this: ```from similarity_analyzer import RelevantText```.
Specify the path to the TF-IDF model and the wiki corpus text file. Create an instance of the class for ```RelevantText```, specifying the paths for the model and text file. Call the ```text_relevance_by_word``` method to search for text IDs, specifying the keyword and the required number of texts as arguments. Call the ```find_text``` method to display texts on the screen, passing it the list of found IDs as an argument.

```python
from similarity_analyzer import RelevantText

# Path to model and text file
model_path = 'full_result_dict.pickle'
text_path = 'wiki(num_title).txt'

# creating an instance of a class RelevantText
rt = RelevantText(model_path, text_path)

# getting a list of IDs of relevant texts
list_num_texts = rt.text_relevance_by_word('dogwood', 3)
    
# gettin relevant texts according to the list of IDs
list_texts = rt.find_text(list_num_texts)
```

You can check the doc with an example _Example.ipynb_.

## License

The module is available as open source under the terms of the [Apache License 2.0][Apache License].

[Apache License]: <https://opensource.org/licenses/Apache-2.0>