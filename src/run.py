from server.instance import server
import sys, os

from resources.book import book
app, api = server.app, server.api

@app.route('/api')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    server.run()