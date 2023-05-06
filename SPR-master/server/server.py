from flask import Flask, request, jsonify, render_template
import util
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       age = int(request.form['age'])
       medu = int(request.form['motheredu'])
       fedu = int(request.form['fatheredu'])
       traveltime = float(request.form['travel'])
       studytime = float(request.form['study'])
       freetime = float(request.form['freetime'])
       goout = float(request.form['goout'])
       g1 = int(request.form['g1'])
       g2 = int(request.form['g2'])
       g3 = int(request.form['g3'])
       estimated_grade = util.get_estimated_grades(age, medu, fedu, traveltime, studytime, freetime, goout, g1, g2, g3)

       result = request.form
   return render_template("result.html", estimated_grade=estimated_grade, result=result)



if __name__ == "__main__":
    print("Starting Python Flask Server For Student Grade Prediction...")
    util.load_saved_artifacts()
    app.run()