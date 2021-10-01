#what the user sees
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#when type / that calls function
@views.route('/')
def home():
# allows for html within python
	return render_template('home.html')
@views.route('/basicalgebra')
def basicalgebra():
# allows for html within python
	return render_template('basicalgebra.html')

@views.route('/quadraticequations')
def quadraticequations():
# allows for html within python
	return render_template('quadraticequations.html')

@views.route('/quadraticfactor')
def quadraticfactor():
# allows for html within python
	return render_template('quadraticfactor.html')

@views.route('/foil')
def foil():
# allows for html within python
	return render_template('foil.html')

@views.route('/foil2')
def foil2():
# allows for html within python
	return render_template('foil2.html')

@views.route('/slopestuff')
def slopestuff():
# allows for html within python
	return render_template('slopestuff.html')

@views.route('/inequalities')
def inequalities():
# allows for html within python
	return render_template('basicinequalities.html')

@views.route('/2x2systems')
def systemsOfEquations():
# allows for html within python
	return render_template('2x2systems.html')

@views.route('/triangle') 
def triangle():
# allows for html within python
	return render_template('trianglegenerator.html')

@views.route('/rectangle') 
def rectangle():
# allows for html within python
	return render_template('rectangle.html')

@views.route('/circle') 
def circle():
# allows for html within python
	return render_template('circle.html')

@views.route('/rectangularprism') 
def rectangularprism():
# allows for html within python
	return render_template('rectangularprism.html')

@views.route('/cylinder') 
def cylinder():
# allows for html within python
	return render_template('cylinder.html')

@views.route('/sphere') 
def sphere():
# allows for html within python
	return render_template('sphere.html')

@views.route('/gtriangle') 
def gtriangle():
# allows for html within python
	return render_template('gtriangle.html')

@views.route('/trapazoid') 
def trapazoid():
# allows for html within python
	return render_template('trapazoid.html')
