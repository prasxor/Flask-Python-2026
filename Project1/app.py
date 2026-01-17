from flask import Flask,render_template,request

studentsData = {
    "vishnu": {
        "password": "teja@123",
        "is_topper": True,
        "subjects": ["Maths", "Physics", "Chemistry"]
    },
    "saboor": {
        "password": "abdul@456",
        "is_topper": False,
        "subjects": ["Biology", "Chemistry", "English"]
    },
    "rahul": {
        "password": "rahul@789",
        "is_topper": False,
        "subjects": ["Maths", "Computer Science", "Physics"]
    },
    "priya": {
        "password": "priya@321",
        "is_topper": True,
        "subjects": ["English", "History", "Political Science"]
    },
    "aman": {
        "password": "aman@654",
        "is_topper": False,
        "subjects": ["Economics", "Maths", "Statistics"]
    },
    "kiran": {
        "password": "kiran@987",
        "is_topper": True,
        "subjects": ["Computer Science", "Maths", "AI"]
    },
    "sneha": {
        "password": "sneha@147",
        "is_topper": False,
        "subjects": ["Biology", "Zoology", "Botany"]
    },
    "rohit": {
        "password": "rohit@258",
        "is_topper": False,
        "subjects": ["Physics", "Maths", "Electronics"]
    },
    "anita": {
        "password": "anita@369",
        "is_topper": True,
        "subjects": ["English", "Sociology", "Psychology"]
    },
    "vikas": {
        "password": "vikas@159",
        "is_topper": False,
        "subjects": ["Accounts", "Business Studies", "Economics"]
    }
}

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template("login.html")
    
@app.route("/submit", methods=["POST"])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in studentsData and password == studentsData[username]["password"]:
        return render_template("index.html", name = username, is_topper = studentsData[username]["is_topper"], subjects = studentsData[username]["subjects"])
    else:
        return "Invalid email or password"