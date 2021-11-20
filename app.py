import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

df = pd.read_csv("amazon_prime.csv")
df = df.fillna("NaN")
df["release_year"] = [str(x) for x in df['release_year']]

def get_features(feats):
    input_columns = feats.T[0]
    inputs = feats.T[1]
    results = []
    
    for sample in df.iloc:
        if len(results)==10:
            break
        for col in input_columns:
            features_idx = list(input_columns).index(col)
            input_ = inputs[features_idx].lower()
            split = sample[col].lower().split(", ")
            if input_ not in split:
                break
        else:
            results.append(sample["title"])
    
    return results

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get_data", methods=["POST"])
def get_data():
    print([x for x in request.form.values()])
    return render_template("home.html", result1=[x for x in request.form.values()]==['', '', '', '', '', '', ''])
    #if [x for x in request.form.values()]==['', '', '', '', '', '', '']:
     #   return render_template("home.html", result1="Please enter a value in any of the text boxes")
    
    """features = np.array([["listed_in", "rating", "release_year", "duration", "cast", "director", "country"],
                         [x for x in request.form.values()]])
    non_empty = [x for x in features[1] if x != ""]
    non_empty_idx = [list(features[1]).index(x) for x in non_empty]
    features = features.T[non_empty_idx]"""
    
if __name__=='__main__':
    app.run(debug=True)
