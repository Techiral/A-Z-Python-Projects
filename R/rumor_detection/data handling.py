df = pd.read_csv('../input/pheme-dataset-for-rumour-detection/dataset.csv')
df.head()

df.shape
df.dtypes
df.describe()
df.isnull().sum()
df.dropna(axis=0, inplace=True)
df.isnull().sum()
df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.duplicated().sum()

df['text'][40]
df['is_rumor'].value_counts()

# Label Encoding
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
df['is_rumor'] = enc.fit_transform(df['is_rumor'])
df['is_rumor'].value_counts()

