from flask import Flask,request,render_template_string 
from urllib import unquote 
app = Flask(__name__) 
@app.route("/") 
def hello(): 
	return "python template injection" 
@app.errorhandler(404) 
def page_not_found(error): 
	url = unquote(request.url) 
	return render_template_string("<h1>URL %s not found</h1><br/>"%url), 404 
if __name__ == '__main__': 
	app.run(debug=False, host='0.0.0.0') 
