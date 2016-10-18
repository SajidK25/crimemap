from flask import Flask,request,render_template,url_for
import json
import dbconfig
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBhelper
else:
    from dbhelper import DBhelper

app=Flask(__name__)
DB=DBhelper()

@app.route("/")
def home():
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template("home.html", crimes=crimes)

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    date = request.form.get("date")
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    description = request.form.get("description")
    DB.add_crime(category, date, latitude, longitude, description)
    return home()



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5009)
