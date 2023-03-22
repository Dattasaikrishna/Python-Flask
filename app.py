from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome!!!"

@app.route('/Datta')
def Datta():
	return "Welcome Datta!!!"

if __name__=='__main__':
	app.run(debug=True)