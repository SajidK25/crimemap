from flask import Flask,request,render_template
from dbhelper import DBhelper

app=Flask(__name__)
DB=DBhelper()

@app.route('/')
def home():
    try:
        data=DB.get_all_inputs()
    except Exception as e:
        print e
        data=None
    return render_template('home.html',data=data)

@app.route('/add')
def add():
    try:
        data=request.form.get("user_input")
        DB.add_input(data)
    except Exception as e:
        print e
    return home()

@app.route('/clear')
def add():
    try:

        DB.clear_all()
    except Exception as e:
        print e
    return home()

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5009)
