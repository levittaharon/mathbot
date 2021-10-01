from flask import Flask




#initializes flask for all files
def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secret'
	
	
	from .views import views
	from .auth import auth
	#easiest prefix
	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')
	return(app)
	

