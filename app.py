from flask import Flask, render_template

# change from termux
app = Flask(__name__)

@app.route('/')
def index():
	name = 'zue zue'
	return render_template ('index.html', name = name)
	
	
