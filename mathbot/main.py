from website import create_app

app = create_app()

#this insures that it only runs if file is run not imported
if __name__ == '__main__':
	#auto update for debug = true
	app.run(debug=True)
