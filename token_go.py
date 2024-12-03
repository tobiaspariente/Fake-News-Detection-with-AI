import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define the cleaning and tokenizing function
def clean_and_tokenize(text):
    """
    Clean and tokenize input text for classification.

    Parameters:
    - text (str): The input text to clean and tokenize.

    Returns:
    - list: A list of cleaned and tokenized words.
    """
    nltk_stopwords = stopwords.words('english')
    
    # Lowercase the text
    text = text.lower()

    # Remove URLs
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = re.sub(r"www\.[a-z]?\.?(com)+|[a-z]+\.(com)", '', text)
    text = re.sub(r'{link}', '', text)
    text = re.sub(r"\[video\]", '', text)
    text = re.sub(r'&[a-z]+;', '', text)

    # Remove Twitter handles and other unwanted characters
    text = re.sub(r"@[A-Za-z0-9]+", '', text)
    text = re.sub(r"[^a-z\s\(\-:\)\\\/\];='#]", '', text)

    # Remove punctuation
    text = "".join([i for i in text if i not in string.punctuation])

    # Remove extra spaces
    text = re.sub(r"[ ]{2,}", ' ', text)

    # Tokenize and remove stopwords
    tokens = [word for word in word_tokenize(text) if word not in nltk_stopwords]

    return tokens