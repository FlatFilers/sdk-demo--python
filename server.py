#! /usr/bin/env python3.6

import os
from flask import Flask, render_template
import jwt

app = Flask(__name__)

EMBED_ID = 'YOUR_EMBED_ID'
PRIVATE_KEY = 'YOUR_PRIVATE_KEY'

@app.route('/')
def index():
  try:
    data = {
      'token': jwt.encode({
        'embed': EMBED_ID,
        'sub': 'max.blank@flatfile.io'
        },
        PRIVATE_KEY,
        algorithm='HS256'
      )
    }

    return render_template('index.html', data=data)
  except Exception as e:
    return str(e)

if __name__ == '__main__':
  app.run(port=4242)
