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
    message = [x for x in request.form.values()]
    
    if len(message)>7:
        message = [x for x in request.form.values()].split(", ")
    
    if message==['', '', '', '', '', '', '']:
        return render_template("home.html", result1="Please enter a value in any of the text boxes")
    
    features = np.array([["listed_in", "rating", "release_year", "duration", "cast", "director", "country"], message)
    non_empty = [x for x in features[1] if x != ""]
    non_empty_idx = [list(features[1]).index(x) for x in non_empty]
    features = features.T[non_empty_idx]
    
    if "duration" in features.T[0]:
        idx = list(features.T[0]).index("duration")
        input_ = features.T[1][idx]
        
        if not input_.isnumeric():
            return render_template("home.html", result1="Please enter the duration as a number")
        else:
            features[idx][1] = input_+" min"
            
    if "release_year" in features.T[0]:
        idx = list(features.T[0]).index("release_year")
        input_ = features.T[1][idx]
        
        if not input_.isnumeric():
            return render_template("home.html", result1="Please enter the release year as a number")
    
    result = get_features(features)
    input_features = "Results for "+", ".join([str(item) for item in features.T[0]])
    
    if len(result)==0:
        return render_template("home.html", result1="Your input did not match any movie or TV show in the database")
    elif len(result)==1:
        return render_template("home.html", input_features=input_features, result1=result[0])
    elif len(result)==2:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1])
    elif len(result)==3:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2])
    elif len(result)==4:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2], result4=result[3])
    elif len(result)==5:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4])
    elif len(result)==6:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5])
    elif len(result)==7:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6])
    elif len(result)==8:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6], result8=result[7])
    elif len(result)==9:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6], result8=result[7], result9=result[8])
    elif len(result)>=10:
        return render_template("home.html", input_features=input_features, result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6], result8=result[7], result9=result[8], result10=result[9])
    
if __name__=='__main__':
    app.run(debug=True)
