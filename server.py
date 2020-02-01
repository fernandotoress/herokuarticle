import newspaper
import os
import treq
from klein import Klein
from twisted.internet.defer import inlineCallbacks, returnValue
        
app = Klein()
@app.route("/ping", methods=['POST', 'GET'])
def ping(request):
    return 'pong!'
    
@app.route("/url", methods=['POST'])
@inlineCallbacks
def extract1(request):
    r = yield treq.get(request.args.get('url', [0])[0])
    content = yield r.content()
    text = newspaper.fulltext(content)
    returnValue(text)

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
