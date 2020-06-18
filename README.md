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
    python train.py

    
Train your model

    python train.py

Run the sample server

    python app.py

Try the endpoints

    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/request -d '{'short_code':"CBgHs1Xjgin", 'max_comments':"10"}'

or open the web application:
  
    http://127.0.0.1:5000/


# References
https://github.com/abhinavsagar/machine-learning-deployment
