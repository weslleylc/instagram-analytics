# instagram-analytics
=================

Basic application to analyzer the sentiment's of Instagram comments for a specific post.

Usage
-----

Clone the repo:

    git clone https://github.com/weslleylc/instagram-analytics
    cd instagram-analytics

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Download the data

     [Sentiment140 Details](http://help.sentiment140.com/for-students)
     [Google Drive](https://docs.google.com/file/d/0B04GJPshIjmPRnZManQwWEdTZjg/edit)

    
Train your model

    python train.py

Run the sample server

    python app.py
    
![alt text](https://github.com/weslleylc/instagram-analytics/blob/master/static/instagram.jpg)

Try the endpoints

    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/request -d '{'short_code':"CBgHs1Xjgin", 'max_comments':"10"}'

or open the web application:
  
    http://127.0.0.1:5000/

Let's text our application. First get the code of a post on instagram.

![alt text](https://github.com/weslleylc/instagram-analytics/blob/master/static/trump.png)
    

Now you need to paste the code and inform the number of comments you want to analyze

![alt text](https://github.com/weslleylc/instagram-analytics/blob/master/static/post.jpg)

You can see the results below

![alt text](https://github.com/weslleylc/instagram-analytics/blob/master/static/comments.jpg)


# References
https://github.com/abhinavsagar/machine-learning-deployment
