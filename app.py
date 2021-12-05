from flask import Flask, request, jsonify, render_template
import pandas as pd
from pandas_profiling import ProfileReport

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


@app.route('/EDA', methods=['POST'])
def eda_demo():
    if(request.method == 'POST'):
        location = request.form['location']
        d = "D:\\CSV_READER\\templates\\out.html"
        df = pd.read_csv(location)
        prof = ProfileReport(df)
        result = prof.to_file(output_file = d)
        return render_template('out.html')


if __name__ == '__main__':
    app.run(debug=True)