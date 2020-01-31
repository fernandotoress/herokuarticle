from newspaper import Article
from flask import Flask, render_template, request, make_response, g

def particle(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return str(e)
        
app = Flask(__name__)
@app.route("/ping", methods=['POST', 'GET'])
def ping():
    return 'pong!'
    
@app.route("/run", methods=['POST'])
def extract():
    return particle(request.form['url'])
    
@app.route("/run", methods=['GET'])
def extract():
    return 'Post'
    
if __name__ == '__main__':
    app.run()
