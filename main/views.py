from flask import Blueprint, render_template
from booa.main.forms import ContactForm

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    return render_template("home.html", tab="home")


@main.route('/vision')
def vision():
    return render_template("vision.html", tab="vision")

@main.route('/background')
def background():
    return render_template("background.html", tab="background")

@main.route('/projects')
def projects():
    return render_template("projects.html", tab="projects")

@main.route('/team')
def team():
    return render_template("team.html", tab="team")

@main.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		print "Successful form submit"
	ctx = {"tab": "contact", "form": form}
	return render_template("contact.html", **ctx)

@main.route('/contribute')
def contribute():
    return render_template("contribute.html", tab="contribute")
