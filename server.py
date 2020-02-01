import os
from sanic import Sanic
from sanic.response import json
import requests
import newspaper
        
app = Sanic()
@app.route("/ping", methods=['POST', 'GET'])
async def ping(request):
    return text('pong!')
    
@app.route("/url", methods=['POST'])
async def extract1(request):
    data = requests.get(request.body.decode()).text
    content = newspaper.fulltext(data)
    return text(data)
	
@app.route("/text", methods=['POST'])
async def extract6(request):
    return text(newspaper.fulltext(request.body.decode()))
    
@app.route("/url", methods=['GET'])
async def extract(request):
    return text('Post')

@app.route("/text", methods=['GET'])
async def extract2(request):
    return text('Post')
    
    
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=os.environ['PORT'],
        
    )
