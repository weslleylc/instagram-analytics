import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from processing import preprocess_tweet
import instaloader

app = Flask(__name__, template_folder="templates/")

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
        input = preprocess_tweet(i.text)
        input = tfdf.transform([input])
        value = model.predict(input)[0]
        results.append(value)
        comments.append({'text': i.text, 'predict': value})
        if count == max_comments:
            break
        else:
            count = count + 1
    total = len(results)
    positive = sum(results)
    negative = total - positive
    return positive/total, negative/total, comments


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    short_code, max_comments = list(request.form.values())

    positive, negative, comments = predict_sentiment_post()
    return render_template('index.html', prediction_text='Your comments are  {}% positive'.format(positive),
                                        predict_comments=comments)

@app.route('/results',methods=['POST'])
def results():

    short_code = list(request.get_json(force=True))[0]
    positive, negative, comments = predict_sentiment_post(short_code)

    return jsonify({'positive': positive, 'negative': negative, 'comments': comments})

if __name__ == "__main__":
    app.run(debug=True)