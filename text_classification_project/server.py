import numpy as np
from flask import Flask, request, jsonify,render_template
import pickle
import os

# print(os.chdir('nlp_for_git'))
print("PWD:::__>>>",os.getcwd())

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))



@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')  # Render the HTML form


@app.route('/classify',methods=['GET','POST'])
def predict():
    # render_template('index.html')  # Render the HTML template
    # data = request.get_json(force=True)
    data = request.form.get('text')
    # text = data['text']
    print(data)
    # print(text)
    prediction = model.predict(tfidf.transform([data]))
    # output = prediction[0]
    output = prediction[0]
    if output == 'no':
        output = "Article not relevant to the US economy "
    elif output == "yes":
        output = "Article relevant to the US economy "
    else:
        pass    

    return render_template('result.html', prediction=output)


if __name__ == '__main__':
    app.run(port=5000,debug=True)