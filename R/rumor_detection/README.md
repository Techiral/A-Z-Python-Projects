# Rumor-Detection-for-PHEME

![image](https://user-images.githubusercontent.com/102687995/193467800-5b0a602e-b16a-46ec-be99-468a5338e66d.png)


## About Dataset :
PHEME dataset for Rumour Detection and Veracity Classification: This dataset contains a collection of Twitter rumours and non-rumours posted during breaking news. It contains rumours related to 9 events,In this dataset we have converted the PHEME Dataset into it's csv format and focused on 2 events the german wing crash and charlie hebdo, the dataset contains over 60,000+ rows.
If you'd like to see the original dataset :
https://figshare.com/articles/dataset/PHEME_dataset_for_Rumour_Detection_and_Veracity_Classification/6392078

The dataset is the csv format of the popular PHEME dataset, this dataset contains 60,000+ rows and also has some null values, this dataset is great for someone just looking to understand classification,this dataset focuses on only 2 of the subtopics in the PHEME Dataset.

1. Charlie Hebdo
2. German Wing Crash

## Approach :
1. At first, preprocessed the PHEME text based on Word Tokenizing, Conversion of words to lower case, Punctuations Removal, Removal of StopWords and Lemmatization using WordNetLemmatizer.
2. Built 6 classification models in Python and identified which works the best for our data using Voting Classifier.
3. Multinomial Naive Bayes, Gaussian Naive Bayes, Random Forest, KNeighbours Classifier, Decision Tree and Gradient Boosting are the 6 models that I used for training dataset.
