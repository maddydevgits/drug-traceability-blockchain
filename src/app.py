from flask import Flask,render_template,request,redirect,session

app=Flask(__name__)
# app.secret_key('makeskilled')

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/register')
def registerPage():
    return render_template('register.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/registerUser',methods=['GET','POST'])
def registerUser():
    name=request.form['name']
    role=request.form['role']
    walletaddr=request.form['walletaddr']
    password=request.form['password']
    print(walletaddr,password,name,role)
    return redirect('/login')

@app.route('/loginUser',methods=['GET','POST'])
def loginUser():
    walletaddr=request.form['walletaddr']
    password=request.form['login']
    print(walletaddr,password)
    return redirect('/dashboard')

if(__name__=="__main__"):
    app.run(debug=True)