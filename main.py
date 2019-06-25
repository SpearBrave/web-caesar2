from caesar import rotate_string
from flask import Flask, request 

app = Flask(__name__)
app.config['DEBUG'] = True
form = '''<!DOCTYPE html>


<html>
    <head>WEB CAESAR
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method="post">
    <label for ="rot"> Rotate by :</label>
    <input id= "rot" type="text" name = "rot" value = 0  >

    <textarea name= "text">{0}</textarea>
    <input type = "submit" value ="Send it !"/>
               
      </form>
      
    </body>
</html>  '''
@app.route("/")
def index():
    return form.format("")


@app.route("/", methods =["POST"])
def encrypt():
    a = request.form["text"]
    
    b= request.form["rot"]
    b= int(b)
    c= rotate_string(a,b) 
    
    return form.format(c)
 




app.run()