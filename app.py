from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return render_template('search.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
