from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def Checker_Board_template():

    return render_template('index.html', row=8, col=8, color_one='red', color_two='black')



@app.route('/<int:a>')
def row(a):

    return render_template('index.html', row=a, col=8, color_one='red', color_two='black')



@app.route('/<int:a>/<int:b>')
def row_col(a,b):

    return render_template('index.html', row=a, col=b, color_one='red', color_two='black')



@app.route('/<int:a>/<int:b>/<string:one>/')
def row_color(a,b,one):

    return render_template('index.html', row=a, col=b, color_one=one, color_two='black')




@app.route('/<int:a>/<int:b>/<string:one>/<string:two>')
def row_col_color(a,b,one,two):

    return render_template('index.html', row=a, col=b, color_one=one, color_two=two)




if __name__=="__main__":
    app.run(debug=True)