from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.get('/')
def index():
  return render_template('index.html')


@app.post('/')
def send():
  data = request.form.to_dict()
  return redirect('/')


if __name__ == "__main__":
  app.run(debug=True)
