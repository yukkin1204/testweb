from flask import Flask, render_template
from main import app

@app.route('/')
def show_hello():
    return render_template('index.html')


