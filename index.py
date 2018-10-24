from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author': 'Previn Wong',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'September 17, 2018'
	},
	{
		'author': 'Dan P',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'September 18, 2018'
	},
	{
		'author': 'Mike Lee',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'September 19, 2018'
	},
	{
		'author': 'Conrad',
		'title': 'Blog Post 4',
		'content': 'Forth post content',
		'date_posted': 'September 20, 2018'
	},
	{
		'author': 'Josh',
		'title': 'Blog Post 5',
		'content': 'Fifth post content',
		'date_posted': 'September 21, 2018'
	}
]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
	return render_template('details.html', posts=posts, title='Details')

if __name__ == '__main__':
	app.run(debug=True)

