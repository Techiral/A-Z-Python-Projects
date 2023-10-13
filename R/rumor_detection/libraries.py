import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # visualization
import seaborn as sns # visualizing data

import os
for dirname, _, filenames in os.walk('../input/pheme-dataset-for-rumour-detection/dataset.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import regex

!pip install nltk
nltk.download('omw-1.4')

