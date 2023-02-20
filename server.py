from flask import Flask, render_template, request, redirect
from flask_frozen import Freezer
import sys

app = Flask(__name__)
freezer = Freezer(app)


@app.get('/')
def index():
  return render_template('index.html')


@app.post('/')
def send():
  data = request.form.to_dict()
  return redirect('/')


if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
  else:
    app.run(debug=True)
