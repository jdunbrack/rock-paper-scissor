from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    win = None
    return render_template('index.html')

@app.route('/results', methods=["POST"])
def results():
    p_choice = request.form['p_choice']

    rng = random.randint(1,3)
    if rng == 1:
        computer_choice = "paper"
    if rng == 2:
        computer_choice = "scissors"
    if rng == 3:
        computer_choice = "rock"

    win = None

    if p_choice == "rock":
        if computer_choice == "scissors":
            win = True
        if computer_choice == "paper":
            win = False
    if p_choice == "paper":
        if computer_choice == "rock":
            win = True
        if computer_choice == "scissors":
            win = False
    if p_choice == "scissors":
        if computer_choice == "rock":
            win = False
        if computer_choice == "paper":
            win = True

    return render_template('index.html', player_choice = p_choice, computer_choice = computer_choice, result = win)


if __name__ == "__main__":
    app.run(debug=True)