import newspaper
import os
from flask import Flask, render_template, request, make_response, g

def particle(rul):
    try:
        article = newspaper.Article(rul)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return str(e)
        
app = Flask(__name__)
@app.route("/ping", methods=['POST', 'GET'])
def ping():
    return 'pong!'
    
@app.route("/url", methods=['POST'])
def extract1():
    return particle(request.form['url'])

@app.route("/text", methods=['POST'])
def extract6():
    return newspaper.fulltext(request.form['text']))
    
@app.route("/url", methods=['GET'])
def extract():
    return 'Post'

@app.route("/text", methods=['GET'])
def extract2():
    return 'Post'
    
    
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=os.environ['PORT'],
        
    )
