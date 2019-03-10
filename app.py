from flask import (Flask, render_template, redirect, url_for, make_response, flash, request, session)
# from flask.sessions import *
# from flask.sessions import Session
import mongoengine
from pymongo import MongoClient 
from mongoengine import (Document, connect, StringField)
from flask_mongoengine import QuerySet
import utility, os
from nth_order_markov_for_web import Dictogram
import config_module

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

if(os.environ['SETTINGS'] == 'DevelopmentConfig'):
    connect('markov_data', host=config_module.DevelopmentConfig.DATABASE_URI)
elif(os.environ['SETTINGS'] == 'ProductionConfig'):
    connect('markov_data', host=config_module.ProductionConfig.DATABASE_URI)
else:
    connect('markov_data', host=config_module.Config.DATABASE_URI)
    

class sources(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)

class sentences(Document):
    content = StringField(required=True)
    # source = StringField(required=True)

@app.route('/')
def home():
    for source in sources.objects:
        source = source.to_mongo().to_dict()
        if source['title'] == 'sources/frankenstein.txt\n':
            words = source['content']
            break
    words = utility.cleanse(words)
    histogram = Dictogram(words, 3)
    histogram.count_to_possibility()
    # session['chain'] = histogram
    # return redirect('/sentence', code=302)
    histogram.get_sentence()
    sentence = histogram.print_sentence()
    return render_template('index.html', test = sentence)

@app.route('/', methods=['POST'])
def save():
    data = request.form
    possible_sent = sentences(content= data['sentence'])#, source = source['title'])
    print(possible_sent.content)
    possible_sent.save()
    return redirect('/', code=302)

# @app.route('/sentence')
# def runner():
#     histogram = session['chain']
#     histogram.get_sentence()
#     sentence = histogram.print_sentence()
#     return render_template('index.html', test = sentence)

@app.route('/saved')
def show():
    saved = []
    for sentence in sentences.objects:
        sentence = sentence.to_mongo().to_dict()
        saved.append(sentence['content'])
    return render_template('saved.html', sentences = saved)


# @app.route('/load_sources')
# def load_sources():
#     texts_list, word_list = [], []
#     f = open('texts.txt', 'r')
#     texts_list = f.readlines()
#     f.close()
#     for text in texts_list:
#         g = open(text.strip(), 'r')
#         word_list = g.readlines()
#         g.close()
#         new_text = sources(title=text, content=" ".join(word_list))
#         new_text.save()
#     return redirect('/', code=302)
