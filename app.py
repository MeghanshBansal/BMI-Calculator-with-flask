from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def showForm():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    height = 0
    weight = 1
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        print(height, weight)
        if height == None:
            height = 0
        if weight == None:
            weight = 1
    BMI = ((int(height)**2)/int(weight))
    return render_template('index.html', BMI=BMI)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
