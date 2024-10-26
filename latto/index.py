from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/<filename>')
def home(filename: str):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:     
        return render_template('notfound.html') 


@app.route('/<filename>/<line>')
def write(filename: str, line:str):
    try:
        with open(filename, 'a') as file:
            content = file.write(f"{line}\n")
        return redirect(f"/{filename}") 
    except FileNotFoundError:     
        return render_template('notfound.html') 
  
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

