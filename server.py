from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'kfj93290fj230u293-fjiofh923yfu239-fh0348h79423hr92fv83bh75y283'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	session['name'] = request.form['your_name']
	session['location'] = request.form['dojo_location']
	session['language'] = request.form['favorite_language']
	session['comment'] = request.form['comment']

	if len(session['name']) > 0 and len(session['comment']) > 0 and len(session['comment']) <= 120:
		return render_template('result.html')
	elif len(session['name']) < 1 or len(session['comment']) < 1 or len(session['comment']) > 120:
		if len(session['name']) < 1:
			flash("Name cannot be empty!")
		if len(session['comment']) < 1:
			flash("Comment cannot be empty!")
		elif len(session['comment']) > 120:
			flash("Comment must be less than 120 characters")
		return redirect('/')


@app.route('/go_back')
def go_back():
	session.clear()
	return redirect('/')

app.run(debug=True)