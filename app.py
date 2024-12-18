from flask import Flask, render_template, request

app = Flask(__name__)

app.route('/')
def index():

    videos = [
        {
            'src': '/static/RealMadrid.mp4',
            'label': 'Real Madrid',
            'link': 'https://www.realmadrid.com/en-US'
        },

        {
            'src': '/static/ManUtd.mp4',
            'label': 'Manchester United',
            'link': 'https://www.manutd.com/'
        },

        {
            'src': '/static/Sporting.mp4',
            'label': 'Sporting CP',
            'link': 'https://www.sporting.pt/en'
        }
    ]
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)