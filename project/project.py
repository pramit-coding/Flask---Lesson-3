from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/calculate', methods=['GET','POST'])

def calculate():
    bmi=''
    if request.method == 'POST' and 'Weight' in request.form and 'Height' in request.form:
        weight = float(request.form.get('Weight'))
        height = float(request.form.get('Height'))
        bmi = round(weight/((height/100)**2),2)
        return render_template("project.html",bmi=bmi)
