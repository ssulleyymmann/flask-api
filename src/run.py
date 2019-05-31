import os
import sys
# for docker 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from flask import jsonify, Flask

from server.instance import server
from resources.book import book
app, api = server.app, server.api

@app.route('/api')
def hello():
    return "hello! welcome to api.."

if __name__ == '__main__':
    server.run()