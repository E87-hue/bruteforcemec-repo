from flask import Flask 

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Welcome To BruteforceMec'  
app.run(host='0.0.0.0', debug=True) 



