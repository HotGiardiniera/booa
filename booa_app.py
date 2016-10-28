import os
from flask import Flask
from flask.ext.mail import Mail
from booa.main.views import *

app = Flask(__name__)
app.register_blueprint(main)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', "change_this")

app.config.update(
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME=os.environ['APP_EMAIL'],
	MAIL_PASSWORD=os.environ['EMAIL_PASS']
	)

mail = Mail(app)

@app.context_processor
def set_static_url():
    return dict(STATIC_URL="/static/")

if __name__ == '__main__':
	app.run()
