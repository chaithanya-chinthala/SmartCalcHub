from flask import Flask
from routes.main import main

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)