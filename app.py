import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
import pickle
from processing import preprocess_sentence
import instaloader

app = Flask(__name__, template_folder="templates/")
bootstrap = Bootstrap(app)
cache = pickle.load(open('./cache/predict_param.pickle', 'rb'))
model = cache['clf']
tfdf = cache['tfdf']

def predict_sentiment_post(short_code="CBgHs1Xjgin", max_comments=10):
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, short_code)
    results = []
    comments = []
    count = 0
    for i in post.get_comments():
        print(i.text)
        input = preprocess_sentence(i.text)
        input = tfdf.transform([input])
        value = int(model.predict(input)[0])
        results.append(value)
        comments.append({'text': i.text, 'predict': value})
        if count > max_comments:
            break
        count = count + 1
    total = int(len(results))
    positive = int(sum(results))
    negative = int(total - positive)
    return positive, negative, total,  comments


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    short_code, max_comments = list(request.form.values())
    positive, negative, total, comments = predict_sentiment_post(short_code, int(max_comments))
    content = {}
    content["prediction_text"] = 'Your comments are  {:.2f}% positive'.format(positive/total)
    content["negative"] = negative
    content["positive"] = positive
    content["comments"] = comments

    return render_template('index.html', content=content)

@app.route('/results',methods=['POST'])
def results():

    dict_json = request.get_json(force=True)
    positive, negative, total, comments = predict_sentiment_post(dict_json['short_code'], int(dict_json['max_comments']))

    return jsonify({'positive': positive, 'negative': negative, 'total': total, 'comments': comments})

if __name__ == "__main__":
    app.run(debug=True)


