from flask import Flask, render_template, request, redirect, url_for, session, flash
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for sessions

# In-memory user store: {username: password}
users = {}

# Load trained model
model = joblib.load("pv_fault_model.pkl")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            flash("Username already exists. Please choose another.")
            return redirect(url_for("register"))
        else:
            users[username] = password
            flash("Registration successful! Please log in.")
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["username"] = username
            flash(f"Welcome, {username}!")
            return redirect(url_for("prediction"))
        else:
            flash("Invalid username or password. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.")
    return redirect(url_for("login"))





@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if "username" not in session:
        flash("Please login to access prediction page.")
        return redirect(url_for("login"))

    prediction = None
    if request.method == "POST":
        try:
            V = float(request.form["V"])
            I = float(request.form["I"])
            G = float(request.form["G"])
            P = float(request.form["P"])

            input_data = np.array([[V, I, G, P]])
            output = model.predict(input_data)[0]

            labels = ["No Module Fault", "Generic Fault", "Partial Shading"]
            prediction = {label: "Yes" if val == 1 else "No" for label, val in zip(labels, output)}

            return render_template("result.html", prediction=prediction)

        except Exception as e:
            return render_template("prediction.html", error=str(e))

    return render_template("prediction.html")


@app.route("/result")
def result():
    if "username" not in session:
        flash("Please login to view results.")
        return redirect(url_for("login"))

    return render_template("result.html")



if __name__ == "__main__":
    app.run(debug=True)
