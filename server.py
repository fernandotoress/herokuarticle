import newspaper
import os
from klein import Klein
 


def particle(rul):
    try:
        article = newspaper.Article(rul)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return str(e)
        
app = Klein()
@app.route("/ping", methods=['POST', 'GET'])
def ping(request):
    return 'pong!'
    
@app.route("/url", methods=['POST'])
def extract1(request):
    return particle(request.args.get('url', [0])[0])

@app.route("/text", methods=['POST'])
def extract6(request):
    return newspaper.fulltext(request.args.get('text', [0])[0])
    
@app.route("/url", methods=['GET'])
def extract(request):
    return 'Post'

@app.route("/text", methods=['GET'])
def extract2(request):
    return 'Post'
    
    
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=os.environ['PORT'],
        
    )
