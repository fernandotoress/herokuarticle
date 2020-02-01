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
def extract1(request):
    r = treq.get(request.args[b'url'][0].decode())
    r.addCallback(treq.content)
    content = newspaper.fulltext(r)
    return content

@app.route("/text", methods=['POST'])
def extract6(request):
    return newspaper.fulltext(request.args[b'text'][0].decode())
    
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
