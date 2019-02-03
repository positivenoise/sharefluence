from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'welcome to the jungle'
 
@app.route("/", methods=['GET','POST'])
def main():
    if 'username' in session:
        return render_template('index.html', session_user_name=session['username'])
    else:
        if request.method == 'POST':
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return main()
        return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return main()
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')