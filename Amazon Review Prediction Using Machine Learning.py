# Source Code
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.svm import LinearSVC 
from sklearn.metrics import accuracy_score
from pickle import dump,load 
from IPython.display import clear_output

f = pd.read_csv('Datasets/amazonreviews.tsv','\t')

f.isnull().sum()

f.dropna(inplace=True)
blanks = []
for i,l,r in f.itertuples():
    if type(r) == str :
        if r.isspace() :
            blanks.append(i)
            
f.drop(blanks,inplace=True)

x = f['review']
y = f['label']
rev_train, rev_test, lab_train, lab_test = train_test_split(x, y, test_size=0.25, random_state=7)

classifier = Pipeline([('tfidf',tf()),('svc',LinearSVC())])

classifier.fit(rev_train,lab_train)

print('')

file1 = open('classifier.pkl','wb')
dump(classifier,file1)
file1.close()

'''

# Execution
from predictor import predictor as start
start()