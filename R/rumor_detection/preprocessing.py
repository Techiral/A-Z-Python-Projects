# Label Encoding
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
df['is_rumor'] = enc.fit_transform(df['is_rumor'])
df['is_rumor'].value_counts()

# Removal of Stopwords
sw = stopwords.words('english')
print(sw)
lm = WordNetLemmatizer()

text_msg = []
for i in df['text']:
    t = regex.sub('[^A-Za-z0-9]',' ',i)    # Removal of Punctuations
    t = t.lower()                          # Conversion to lowercase
    t = word_tokenize(t)                   # word_tokenization
    t = [i for i in t if i not in sw]      # stopwords removal
    t = [lm.lemmatize(i) for i in t]       # Lemmatization
    t = " ".join(t)
    text_msg.append(t)
print(text_msg[:10])

# Vector transformation of text using Count Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2000) ### Here 2000 implies length of the sentence.
sm = cv.fit_transform(text_msg).toarray()  ### sparse_matrix
print(len(cv.get_feature_names_out()))
print(sm.shape)

print(len(sm[0]))
print(len(sm[2342]))
print(len(sm[3453]))
print(len(sm[876]))

