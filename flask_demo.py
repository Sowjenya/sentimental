from flask import Flask, render_template, request, session
import pandas as pd

from main import analysis
app = Flask(__name__)

app.secret_key = 'You Will Never Guess'
@app.route("/")
def hello_world():
    return render_template("home.html");

@app.route('/home',  methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        uploaded_file = request.files['uploaded-file']
        uploaded_df = pd.read_csv(uploaded_file);
        uploaded_df_sentiment = analysis(uploaded_df);
        uploaded_df_html = uploaded_df_sentiment.to_html()
        return render_template('show_data.html', data=uploaded_df_html);
        
@app.route("/home")
def home():
    return render_template("home.html");
=