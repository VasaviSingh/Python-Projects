#Import libraries
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

#Read csv file
df=pd.read_csv('C:\\Users\\vasav\\Documents\\Python\\FakeNewsDetection\\news.csv')

#Define label
labels=df.label

#Split data into training and testing datsets
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

#Initialize tfidf vector
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

#Define tfidf train and test data
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)

#Initialize Passive Aggressive Classifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

#Find the predicted accuracy
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)

#Confusion Matrix
print(confusion_matrix(y_test,y_pred, labels=['FAKE','REAL']))

#Using your best performing classifier with your TF-IDF vector dataset (tfidf_vectorizer) and 
#Passive Aggressive classifier (linear_clf), inspect the top 30 vectors 
#for fake and real news
class_labels = pac.classes_
feature_names = tfidf_vectorizer.get_feature_names()

#sorted(zip(classifier.coef_[labelid], feature_names))[-n:] 
#retrieves the coefficient of the classifier for a given class label and then sorts it in ascending order.
topn_class1 = sorted(zip(pac.coef_[0], feature_names))[:30]
topn_class2 = sorted(zip(pac.coef_[0], feature_names))[-30:]
for coef, feat in topn_class1:
 print(class_labels[0], coef, feat)
 print()
for coef, feat in reversed(topn_class2):
  print(class_labels[1], coef, feat)