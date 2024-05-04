from flask import Flask, render_template, request
from src.pipelines.prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        customeData = CustomData()
        predict_pipeline = PredictPipeline()
        pred = 0

        data = request.form.to_dict()
        data['carat'] = float(data['carat'])
        data['depth'] = float(data['depth'])
        data['table'] = float(data['table'])
        data['x'] = float(data['x'])
        data['y'] = float(data['y'])
        data['z'] = float(data['z'])
        data = customeData.get_data_as_df(data)

        print(data)
        
        pred = predict_pipeline.predict(data)
        pred = round(pred[0], 2)

        return render_template("result.html", final_result=pred)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
