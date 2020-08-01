import os

from flask import Flask
from flask import render_template
from flask import request

from fastai.vision import load_learner, Path, open_image

import pickle

path = Path()

model = load_learner(path, 'model/export.pkl')

app = Flask(__name__)

upload_folder = "/home/ritobrata/ML/mini-projects/ifd-athakur/static"

@app.route("/", methods=["GET", "POST"])

def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(
                upload_folder,
                image_file.filename
            )
            image_file.save(image_location)
            img = open_image(image_location)
            prediction, _, _ = model.predict(img)

            return render_template("predict.html", output=prediction.obj)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)