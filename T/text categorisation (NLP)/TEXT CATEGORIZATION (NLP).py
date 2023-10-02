#!/usr/bin/env python
# coding: utf-8

# # **TEXT CATEGORIZATION**
# ---
# 

# 
# ### **Problem Statement:**
# 
# The project aims to develop a NLP solution for categorizing customer grievances. Customer grievances can arise in various forms, including issues related to the quality of service, access and availability, billing/financial disputes, benefit packages, marketing and many more. Here in this project, I have tried to trained a classification model, which can classify texts into appropriate category and subcategory.
# 
# ### **Objectives:**
# 
# 1. **Data Preprocessing:** This involves loading a dataset containing customer grievances, primarily focusing on the 'Description of the Grievance' column. The data is then preprocessed by cleaning and transforming the text to facilitate meaningful analysis.
# 
# 2. **Label Encoding:** The target labels, specifically 'Grievance Category' and 'Grievance SubCategory,' are encoded into numerical values to prepare them for machine learning algorithms.
# 
# 3. **Feature Engineering:** Text data is converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. This step helps in representing the text data in a format suitable for machine learning models.
# 
# 4. **Model Building and Evaluation:** Several machine learning classifiers, including K Nearest Neighbors, Decision Tree, Random Forest, Logistic Regression, SGD Classifier, Naive Bayes, and SVM Linear, are employed to categorize customer grievances into predefined categories. Both 'Grievance Category' and 'Grievance SubCategory' are predicted separately using these classifiers.
# 
# 5. **Ensemble Modeling:** A Voting Classifier is constructed to combine predictions from multiple base classifiers. This ensemble approach aims to enhance prediction accuracy and robustness.
# 
# 6. **Performance Evaluation:** The accuracy of each individual classifier and the ensemble model is evaluated, and classification reports are generated to provide more detailed insights into model performance.
# 
# ### **Outcome:**
# 
# The project seeks to provide a robust and accurate solution for automatically categorizing customer grievances based on textual descriptions. This automated categorization can help organizations streamline their grievance handling processes, allocate resources efficiently, and enhance customer satisfaction by ensuring that grievances are directed to the appropriate teams for resolution. The use of machine learning and ensemble techniques allows for a more efficient and objective handling of customer grievances.
# 
# ##### Category Prediction Results:
# ##### Achieved the highest accuracy of 62.42% using the Voting Classifier model.
# 
# ##### Sub-Category Prediction Results: 
# ##### Achieved the highest accuracy of 37.58% through the combined efforts of the Voting Classifier and SVM                                                                            Linear models.
# 

# In[41]:


# Importing the Pandas library.
import pandas as pd

# Importing the 're' module.
import re

# Suppressing warnings to maintain a clean and readable output.
import warnings
warnings.filterwarnings("ignore")

# NLTK libraries for tokenization and lemmatization
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Scikit-learn libraries for data preprocessing and machine learning
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

# Scikit-learn metrics for model evaluation
from sklearn.metrics import accuracy_score, classification_report

# Loading the dataset from an Excel file named 'NLP_Data.xlsx' into a Pandas DataFrame.
data = pd.read_excel('NLP_Data.xlsx')


# ### Text Cleaning or Data Preprocessing

# In[42]:


# Removing rows with missing values in the 'Description of the Grievance' column.
data.dropna(subset=['Description of the Grievance'], inplace=True)


# In[43]:


# Defining a function to preprocess text data.
def preprocess_text(text):
    if isinstance(text, str):
        # Cleaning the text by removing special characters, punctuation, and numbers using regular expressions.
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Converting the text to lowercase for consistency.
        text = text.lower()
    else:
        # Handling missing values or non-string data by setting text to an empty string.
        text = ''
    return text


# In[44]:


# Applying text preprocessing to the 'Description of the Grievance' column
data['cleaned_description'] = data['Description of the Grievance'].apply(preprocess_text)

# Removing punctuation
data['cleaned_description']  = data['cleaned_description'] .str.replace(r'[^\w\d\s]', ' ')

# Replacing whitespace between terms with a single space
data['cleaned_description']  = data['cleaned_description'] .str.replace(r'\s+', ' ')

# Removing leading and trailing whitespace
data['cleaned_description']  = data['cleaned_description'] .str.replace(r'^\s+|\s+?$', '')


# In[45]:


# Converting the cleaned text in the 'cleaned_description' column to lowercase.
data['cleaned_description'] = data['cleaned_description'].str.lower()

# Printing the cleaned and lowercase text in the 'cleaned_description' column.
print(data['cleaned_description'])


# In[46]:


# Importing the 'stopwords' module from NLTK (Natural Language Toolkit).
from nltk.corpus import stopwords

# Converting the cleaned text in the 'cleaned_description' column to lowercase.
data['cleaned_description'] = data['cleaned_description'].str.lower()

# Printing the cleaned and lowercase text in the 'cleaned_description' column.
print(data['cleaned_description'])


# In[47]:


# Creating a set of English stopwords using the NLTK library.
stop_words = set(stopwords.words('english'))

# Defining a function to remove stopwords from a text.
def remove_stopwords(text):
    if isinstance(text, str):
        # Split the text into terms, remove stopwords, and join the remaining terms back into a text.
        return ' '.join(term for term in text.split() if term not in stop_words)
    else:
        return text  # Return non-string values unchanged

# Applying the remove_stopwords function to the 'cleaned_description' column to eliminate stopwords.
data['cleaned_description'] = data['cleaned_description'].apply(remove_stopwords)


# ### Stemming

# In[48]:


# Importing the NLTK library and the Porter Stemmer from NLTK.
import nltk
from nltk.stem import PorterStemmer

# Initializing the Porter Stemmer.
ps = PorterStemmer()

# Defining a function to apply stemming to text strings.
def stem_text(text):
    if isinstance(text, str):
        # Split the text into terms, apply stemming to each term, and join them back into a text.
        return ' '.join(ps.stem(term) for term in text.split())
    else:
        return text  # Return non-string values unchanged

# Applying the stem_text function to the 'cleaned_description' column to perform word stemming.
data['cleaned_description'] = data['cleaned_description'].apply(stem_text)


# ### Lemmatization

# In[49]:


# Importing the NLTK library and the WordNet Lemmatizer from NLTK.
import nltk
from nltk.stem import WordNetLemmatizer

# Initializing the WordNet Lemmatizer.
lemmatizer = WordNetLemmatizer()

# Defining a function to apply lemmatization to text strings.
def lemmatize_text(text):
    if isinstance(text, str):
        # Spliting the text into terms, apply lemmatization to each term, and join them back into a text.
        return ' '.join(lemmatizer.lemmatize(term) for term in text.split())
    else:
        return text  # Return non-string values unchanged

# Applying the lemmatize_text function to the 'cleaned_description' column for lemmatization.
data['cleaned_description'] = data['cleaned_description'].apply(lemmatize_text)


# In[50]:


# Import the NLTK library and download the 'punkt' resource.
import nltk
nltk.download('punkt')


# In[51]:


# Initializing a LabelEncoder for encoding target labels.
label_encoder = LabelEncoder()

# Encoding the 'Grievance Category' column and store the results in 'Category_Labels'.
data['Category_Labels'] = label_encoder.fit_transform(data['Grievance Category'])

# Displaying the encoded 'Category_Labels'.
data['Category_Labels']

# Encoding the 'Grievance SubCategory' column and store the results in 'Category_SubLabels'.
data['Category_SubLabels'] = label_encoder.fit_transform(data['Grievance SubCategory'])

# Displaying the encoded 'Category_SubLabels'.
data['Category_SubLabels']


# In[52]:


# Importing the NLTK library and download the 'omw-1.4' resource.
import nltk
nltk.download('omw-1.4')


# In[53]:


# Spliting the dataset into features (X) and target labels (y1 and y2).
X = data['cleaned_description']  # Features, containing cleaned text descriptions
y1 = data['Category_Labels']  # Target labels for 'Grievance Category'
y2 = data['Category_SubLabels']  # Target labels for 'Grievance SubCategory'


# ### Vectorization

# In[54]:


# Createing a TF-IDF vectorizer with hyperparameter tuning.
# Seting the maximum number of features to 1000 and specify English stop words.
tfidf_vectorizer = TfidfVectorizer(max_features=60, stop_words='english')

# Fiting and transforming the cleaned text data using TF-IDF vectorization.
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Spliting the data into training and testing sets for 'Grievance Category' prediction.
X_train, X_test, y1_train, y1_test = train_test_split(X_tfidf, y1, test_size=0.3, random_state=42)

# Spliting the data into training and testing sets for 'Grievance SubCategory' prediction.
X_train, X_test, y2_train, y2_test = train_test_split(X_tfidf, y2, test_size=0.3, random_state=42)


# ### Category Prediction (Y1)

# In[55]:


# Defining a list of base classifiers with hyperparameter tuning
classifiers = [
     ('svm', GridSearchCV(SVC(kernel='linear'), {'C': [0.01, 0.1, 1.0]}, cv=5)),
      ('naive_bayes', MultinomialNB()),
     ('logistic_regression', GridSearchCV(LogisticRegression(max_iter=100), {'C': [0.01, 0.1, 1.0]}, cv=5))
    
]

# Creating a Voting Classifier with the specified base classifiers
voting_classifier = VotingClassifier(estimators=classifiers, voting='hard')

# Training the Voting Classifier on the training data
voting_classifier.fit(X_train, y1_train)

# Making predictions on the test data using the ensemble model
y1_pred = voting_classifier.predict(X_test)

# Evaluating the performance of the ensemble model by calculating accuracy
accuracy = accuracy_score(y1_test, y1_pred)
print(f"Accuracy of Voting Classifier: {accuracy * 100:.2f}%")

# Generating a classification report for more detailed evaluation
classification_rep = classification_report(y1_test, y1_pred)
print("Classification Report for Voting Classifier:")
print(classification_rep)


# In[56]:


# Defining a list of classifier names and corresponding classifier instances
names = ["K Nearest Neighbors", "Decision Tree", "Random Forest", "Logistic Regression", "SGD Classifier",
         "Naive Bayes", "SVM Linear"]

classifiers = [
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    LogisticRegression(max_iter=100),  # Increase max_iter if needed
    SGDClassifier(),
    MultinomialNB(),
    SVC(kernel='linear')  # You can use other kernels as well
]

best_accuracy = 0
best_classifier = None

# Iterating through each classifier and evaluate its performance
for name, clf in zip(names, classifiers):
    print(f"Training and evaluating {name}:: ")
    
    # Training the classifier on the training data
    clf.fit(X_train, y1_train)
    
    # Making predictions on the test data
    y1_pred = clf.predict(X_test)
    
    # Calculating the accuracy of the model
    accuracy = accuracy_score(y1_test, y1_pred)
    print(f"Accuracy of {name}: {accuracy * 100:.2f}%")
    
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_classifier = name
        
    print("\n")
    
print(f"The best classifier is {best_classifier} with an accuracy of {best_accuracy * 100:.2f}%")


# ### SubCategory Prediction (Y2)

# In[57]:


# Defining a list of base classifiers with hyperparameter tuning
classifiers = [
    ('logistic_regression', GridSearchCV(LogisticRegression(max_iter=1000), {'C': [0.1, 1.0, 10.0]}, cv=5)),
    ('svm', GridSearchCV(SVC(kernel='linear'), {'C': [0.1, 1.0, 10.0]}, cv=5))
]

# Creating a Voting Classifier with the specified base classifiers
voting_classifier = VotingClassifier(estimators=classifiers, voting='hard')

# Training the Voting Classifier on the training data
voting_classifier.fit(X_train, y2_train)

# Make predictions on the test data using the ensemble model
y2_pred = voting_classifier.predict(X_test)

# Evaluating the performance of the ensemble model by calculating accuracy
accuracy = accuracy_score(y2_test, y2_pred)
print(f"Accuracy of Voting Classifier: {accuracy * 100:.2f}%")

# Generating a classification report for more detailed evaluation
classification_rep = classification_report(y2_test, y2_pred)
print("Classification Report for Voting Classifier:")
print(classification_rep)


# In[58]:


# Defining a list of classifier names and corresponding classifier instances for 'Grievance SubCategory'
names = ["K Nearest Neighbors", "Decision Tree", "Random Forest", "Logistic Regression", "SGD Classifier",
         "Naive Bayes", "SVM Linear"]

classifiers = [
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    LogisticRegression(max_iter=1000),  # Increase max_iter if needed
    SGDClassifier(),
    MultinomialNB(),
    SVC(kernel='linear')  # You can use other kernels as well
]

best_accuracy = 0
best_classifier = None

# Iterating through each classifier and evaluate its performance for 'Grievance SubCategory'
for name, clf in zip(names, classifiers):
    print(f"Training and evaluating {name} ::")
    
    # Train the classifier on the training data for 'Grievance SubCategory'
    clf.fit(X_train, y2_train)
    
    # Make predictions on the test data for 'Grievance SubCategory'
    y2_pred = clf.predict(X_test)
    
    # Calculate the accuracy of the model for 'Grievance SubCategory'
    accuracy = accuracy_score(y2_test, y2_pred)
    print(f"Accuracy of {name}: {accuracy * 100:.2f}%")
    print('\n')
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_classifier = name
        
    print("\n")
    
print(f"The best classifier is {best_classifier} with an accuracy of {best_accuracy * 100:.2f}%")


# ### DATASET WITH PREDCITION 

# In[59]:


data


# # **RESULT**

# 
# # ACCURACY (Y1 PREDICTION)
# 
# |   MODEL  |      ACCURACY |
# |----------|----------|
# | Voting Classifier  | 62.42%   |
# | K Nearest Neighbors   | 49.68% |
# | Decision Tree  | 39.49% |
# | Random Forest   |  54.78% |
# | Logistic Regression   | 59.87%   |
# | SGD Classifier   |  49.68% |
# | Naive Bayes  | 56.69%  |
# | SVM Linear   | 60.51%  |
# 
# 
# ## Best Performance: Voting Classifier (62.42% accuracy)

# ----------------------------------------------------------------------------------------------------------------------------
# 

# # ACCURACY (Y2 PREDICTION)

# 
# |   MODEL  |      ACCURACY |
# |----------|----------|
# | Voting Classifier  |  37.58%    |
# | K Nearest Neighbors   | 28.03%  |
# | Decision Tree  |   25.48% |
# | Random Forest   |   29.94% |
# | Logistic Regression   | 32.48% |
# | SGD Classifier   | 29.94% |
# | Naive Bayes  | 26.75%  |
# | SVM Linear   | 37.58% |
# 
# ## Best Performance: Voting Classifier and SVM (Linear) (37.58%  )
# 

# In[ ]:




