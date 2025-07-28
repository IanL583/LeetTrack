from flask import Flask
from flask_cors import CORS
from routes.problems import problem_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(problem_blueprint)

@app.route("/")
def home():
    return {"message": "LeetTrack is running!"}

if __name__ == "__main__":
    app.run(debug=True)