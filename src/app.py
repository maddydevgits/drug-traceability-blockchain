from flask import Flask,render_template,request,redirect,session
from web3 import Web3,HTTPProvider
import json

def connect_Blockchain_register(acc):
    blockchain_address="http://127.0.0.1:8545"
    web3=Web3(HTTPProvider(blockchain_address))
    if(acc==0):
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='../build/contracts/register.json'
    contract_address="0x02E5556090ba5e6ab9Ee89b5150183E960eed4Eb"
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    print('connected with blockchain')
    return (contract,web3)

app=Flask(__name__)
app.secret_key='makeskilled'

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
    role=int(request.form['role'])
    walletaddr=request.form['walletaddr']
    password=int(request.form['password'])
    print(walletaddr,password,name,role)
    contract,web3=connect_Blockchain_register(walletaddr)
    tx_hash=contract.functions.registerUser(walletaddr,password,name,role).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return redirect('/login')

@app.route('/loginUser',methods=['GET','POST'])
def loginUser():
    walletaddr=request.form['walletaddr']
    password=int(request.form['password'])
    print(walletaddr,password)
    contract,web3=connect_Blockchain_register(walletaddr)
    state=contract.functions.loginUser(walletaddr,password).call()
    print(state)
    if(state==True):
        session['walletaddr']=walletaddr
        contract,web3=connect_Blockchain_register(walletaddr)
        _users,_passwords,_roles,_names=contract.functions.viewUsers().call()
        userIndex=_users.index(walletaddr)
        role=_roles[userIndex]
        print(role)
        if(role==1):
            return redirect('/labdashboard')
        elif(role==2):
            return redirect('/manudashboard')
        elif(role==3):
            return redirect('/waremdashboard')
        elif(role==4):
            return redirect('/transdashboard')
        elif(role==5):
            return redirect('/waretdashboard')
        elif(role==6):
            return redirect('/hospitalsdashboard')
        elif(role==7):
            return redirect('/retailersdashboard')
    else:
        return redirect('/login')

@app.route('/labdashboard')
def labDashboard():
    return render_template('labdashboard.html')

@app.route('/manudashboard')
def manudashboard():
    return render_template('manudashboard.html')

@app.route('/waremdashboard')
def waremdashboard():
    return render_template('waremdashboard.html')

@app.route('/transdashboard')
def transdashboard():
    return render_template('transdashboard.html')

@app.route('/waretdashboard')
def waretdashboard():
    return render_template('waretdashboard.html')

@app.route('/hospitalsdashboard')
def hospitalsdashboard():
    return render_template('hospitalsdashboard.html')

@app.route('/retailersdashboard')
def retailersdashboard():
    return render_template('retailersdashboard.html')

@app.route('/logout')
def logout():
    session['walletaddr']=''
    return redirect('/')

@app.route('/shareFormula',methods=['POST','GET'])
def shareFormula():
    walletaddr=request.form['walletaddr']
    mformula=request.form['mformula']
    print(walletaddr,mformula)
    return redirect('/viewlabmanufacturers')

@app.route('/viewlabmanufacturers')
def viewlabmanufacturers():
    return render_template('viewlabmanufacturers.html')

@app.route('/viewFeedbackslab')
def viewFeedbackslab():
    return render_template('viewFeedbackslab.html')

if(__name__=="__main__"):
    app.run(debug=True)