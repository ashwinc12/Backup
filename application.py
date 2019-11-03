from flask import Flask, render_template, url_for, request, redirect, session, g

app = Flask(__name__)
app.secret_key = 'a random key that no one will ever guess because why would they bother'

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		s = request.form.get("semester")
		s_c = request.form.get("subject-code")
		c_n = request.form.get("course-number")
		n = ""
		c = []
		# Access the database and do all checking here
		# Hard-coded this process for now
		link = "https://storage.googleapis.com/class-hub-bucket/Lecture%2001%20Functions%20of%20several%20variables.mp4"
		if s_c == "MATH" and c_n == "2010":
			n = "Multivariable Calulus and Matrix Algebra"
			c = [
				("Stevenson", [(link, "9/5/19", 1), (link, "9/9/19", 2)]),
				("McLaughlin", [(link, "9/6/19", 1), (link, "9/10/19", 2)])
			]	
		elif s_c == "CSCI" and c_n == "1200":
			n = "Data Structures"
			c = [
				("Cutler", [(link, "9/5/19", 1), (link, "9/9/19", 2), (link, "9/12/19", 3)])
			]
		else:
			return render_template("index.html", error_message="Invalid course selection")
		return render_template("course_page.html", subject_code = s_c, course_number = c_n, course_name = n, content = c)
	else:
		return render_template("index.html")