import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

df = pd.read_csv("amazon_prime_titles.csv")
df = df.fillna("NaN")

def get_features(feature, input_, inp_data):
    indices = []
    idx = 0

    for item in inp_data[feature]:
        for element in item.split(", "):
            print(element, input_)
            if input_ == element:
                indices.append(idx)
        idx += 1
    data = inp_data.iloc[indices].reset_index(drop=True)
    return data

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/get_data', methods=['POST'])
def get_data():
    feature_names = ["listed_in", "rating", "release_year", "duration", "cast", "director", "country"]
    features = np.array([["listed_in", "rating", "release_year", "duration", "cast", "director", "country"],
                        [x for x in request.form.values()]]).T
    data = df
    for i in features:
        category = i[0]
        value = i[1]
        data = get_features(category, value, data)
   
    result = list(data["title"])
    
    if [x for x in request.form.values()]==['', '', '', '', '', '', '']:
        return render_template("home.html")
    elif len(result)==0:
        return render_template("home.html")
    elif len(result)==1:
        return render_template("home.html", result1=result[0])
    elif len(result)==2:
        return render_template("home.html", result1=result[0], result2=result[1])
    elif len(result)==3:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2])
    elif len(result)==4:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2], result4=result[3])
    elif len(result)==5:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4])
    elif len(result)==6:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5])
    elif len(result)==7:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6])
    elif len(result)==8:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6], result8=result[7])
    elif len(result)==9:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6], result8=result[7], result9=result[8])
    elif len(result)>=10:
        return render_template("home.html", result1=result[0], result2=result[1], result3=result[2], result4=result[3], result5=result[4], result6=result[5], result7=result[6], result8=result[7], result9=result[8], result10=result[9])
    
if __name__=='__main__':
    app.run(debug=True)