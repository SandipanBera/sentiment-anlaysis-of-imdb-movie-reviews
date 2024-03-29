# Importing essential libraries
from flask import Flask, render_template, request
import pickle

# Load the Naive Bayes model and TfidfVectorizer object from disk
filename = 'review-classification.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('tfid-vectorizer.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
      message=request.form['message']
      data =[message]
      vect =cv.transform(data).toarray()
      my_prediction=classifier.predict(vect)
      return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)