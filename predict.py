import os
import pickle
from flask import Flask, request, jsonify
import xgboost as xgb

model_file = "{}/model.bin".format(os.path.dirname(os.path.realpath(__file__)))

with open(model_file, "rb") as mf:
    model, dv = pickle.load(mf)

app = Flask("bank-marketing-system")


@app.route("/")
def home():
    return "Bank Marketing System"


@app.route("/predict", methods=["POST"])
def predict():
    record = request.get_json()

    X = dv.transform(record)
    features = dv.get_feature_names()
    dX = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dX)

    subscribe_term_deposit = y_pred >= 0.4

    result = {
        "subscribe_term_deposit_probability": float(y_pred),
        "subscribe_term_deposit": bool(subscribe_term_deposit),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)