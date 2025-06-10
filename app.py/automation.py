
from flask import Flask, render_template, request
import pywhatkit

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    number = request.form['number']
    message = request.form['message']
    hour = int(request.form['hour'])
    minute = int(request.form['minute'])

    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        return "Message scheduled successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
