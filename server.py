import os
from sanic import Sanic
from sanic.response import text
import requests
import newspaper
        
app = Sanic()
@app.route("/ping", methods=['POST', 'GET'])
async def ping(request):
    return text('pong!')
    
@app.route("/extract-url", methods=['POST'])
async def extract1(request):
    data = requests.get(request.form.get('url')).text
    content = newspaper.fulltext(data)
    return text(content)
	
@app.route("/extract-html", methods=['POST'])
async def extract6(request):
    return text(newspaper.fulltext(request.form.get('text')))
    
@app.route("/extract-url", methods=['GET'])
async def extract(request):
    return text('API only takes POST requests')

@app.route("/extract-html", methods=['GET'])
async def extract2(request):
    return text('API only takes POST requests')
    
    
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=os.environ['PORT'],
        
    )
