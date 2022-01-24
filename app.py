from flask import Flask, render_template
import os
import requests


app=Flask(__name__)

@app.route('/')
def index():
    
    
    text ="ulubione chipsy hydraulika" #open('xd.txt').read()
    print(text)
    
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    
    strona_flag = requests.get('https://zajecia-programowania-xd.pl/flagi')
    
    
    return render_template("xd.html")
    
if __name__=="__main__":
    app.run()
