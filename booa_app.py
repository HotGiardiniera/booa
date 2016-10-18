import os
from flask import Flask

app = Flask(__name__)
app.register_blueprint(main)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.context_processor
def set_static_url():
    return dict(STATIC_URL="http://127.0.0.1:5000/static/")
if __name__ == '__main__':
	app.run()