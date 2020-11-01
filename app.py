from flask import Flask, request, render_template,redirect, url_for
import time
app = Flask(__name__)

import easydbio

db = easydbio.DB({
  "database": "4a4e6a86-1fbe-45d1-a3c8-6fefa2b6e499",
  "token": "c06a2b02-898d-4dce-beb9-61db4ed3177a"
})

@app.route('/')
def hello_world():
    return render_template("index.html", items = db.List().items())
    

@app.route('/add')
def add():
    
    data = request.args.get('data')
    db.Put(time.time(), data)
    return redirect("/")

@app.route('/deleteAll')
def deleteAll():
    keys = db.List().keys()
    for key in keys:
        db.Delete(key)
    return redirect("/")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)