from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'Pass'
    else:
        res = 'Fails'
    exp = {'Score': score, 'res': res}
    return render_template('results.html', results=exp)


@app.route('/fails/<int:score>')
def fails(score):
    return f'<h1>Sorry you failed the exam .your score is  {score} Marks<h1>'


@app.route('/results/<int:marks>')
def results(marks):
    # results = ' '
    if marks < 50:
        results = 'fails'
    else:
        results = 'success'
    return redirect(url_for(results, score=marks))


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = ''
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4

    res = ''

    if total_score >= 50:
        res = 'success'

    else:
        res = 'fails'

    return redirect(url_for(res, score=total_score))


if __name__ == '__main__':
    app.run(debug=True)