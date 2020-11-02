from flask import Flask, request, render_template,redirect, url_for
import time
import os
app = Flask(__name__)

import pymongo
import time, threading

#connect to mongoDB client
client = pymongo.MongoClient(os.environ['key']) #insert connection string
db2 = client.get_database('CLOUDCLUSTER')
p = db2.test_collection

#default route
@app.route('/')
def hello_world():
    return render_template("index.html", items = list(p.find()))
    
#add an item
@app.route('/add')
def add():    
    data = request.args.get('data')
    post = {data: data}
    #query for adding an item to MongoDb collection
    p.insert_one(post)
    return redirect("/")

#delete all items
@app.route('/deleteAll')
def deleteAll():
    #query for removing all items from MongoDB collection
    p.remove({})
    return redirect("/")

#remove items after every 1800 seconds
def foo():
    p.remove({})
    threading.Timer(1800, foo).start()


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    foo()
    app.run(threaded=True, port=5000)