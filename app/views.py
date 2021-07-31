from django.shortcuts import redirect, render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from web3 import Web3
import json
import web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]
abi = json.loads('[{"constant":false,"inputs":[{"name":"voterIndex","type":"uint256"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_first_name","type":"string"},{"name":"_last_name","type":"string"},{"name":"_email","type":"string"},{"name":"_username","type":"string"},{"name":"_phone_number","type":"string"},{"name":"_password","type":"string"}],"name":"register","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"auctionEnd","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"canditates","outputs":[{"name":"name","type":"string"},{"name":"voteCount","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_username","type":"string"},{"name":"_password","type":"string"}],"name":"login","outputs":[{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getInfo","outputs":[{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"voter","type":"address"}],"name":"authorize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"candInfo","outputs":[{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"nbOfVoters","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"end","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"duraitonMinutes","type":"uint256"},{"name":"canditate1","type":"string"},{"name":"canditate2","type":"string"},{"name":"canditate3","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"name","type":"string"},{"indexed":false,"name":"voteCount","type":"uint256"}],"name":"ElectionResult","type":"event"}]')
address = web3.toChecksumAddress("0xD8595399d47Fe05D151A2DFD41C78e19759724DF")

contract = web3.eth.contract(address=address, abi=abi)

cand = 0
cand_names = []
userDetails = []
main_info = []

def index(request):
    global userDetails
    if userDetails:
        return render(request,'index.html',{'log':1, 'name':userDetails[0]})
    else:
        return render(request,'index.html',{'log':0})

def userLogin(request):

    global userDetails
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userDetails = contract.functions.login(username, password).call()
        print(userDetails)
        if(username==userDetails[0] and password == userDetails[5]):
            return redirect('vote')
    else:
        return render(request,'userLogin.html')

def userRegister(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            tx_hash = contract.functions.register(first_name,last_name,email,username,phone_number,password1).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
            print('User created')
            return redirect('userLogin')
        else:
            messages.info(request,'Phone Number or Password Not Matching')
            return redirect('userRegister')
    else:
        return render(request, "userRegister.html")

def logout(request):
    global userDetails
    userDetails = []
    return redirect('vote')

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            return redirect('main')
    else:
        return render(request, 'adminLogin.html')

def main (request):
    for i in range(3):
        main_info.append([])
    for i in range(3):
        main_info[i] = contract.functions.getInfo().call()
    print(main_info)
    return render(request, 'admin.html',{'main_info':main_info})

def result(request):
    return render(request, 'result.html')

def vote(request):
    global cand
    cand = 0
    if userDetails:
        return render(request, 'vote.html',{'cand':cand,'log':1,'name':userDetails[0]})
    else:
        return render(request, 'vote.html',{'cand':cand,'log':0})

def conform1(request):
    global cand
    global cand_names
    cand = 1
    cand_names = contract.functions.candInfo().call()
    print(cand_names)
    if userDetails:
        return render(request, 'conform.html',{'cand':cand, 'cand_name':cand_names[0]})
    else:
        return render(request, 'userLogin.html')

def conform2(request):
    global cand
    global cand_names
    cand = 2
    cand_names = contract.functions.candInfo().call()
    if userDetails:
        return render(request, 'conform.html',{'cand':cand, 'cand_name':cand_names[1]})
    else:
        return render(request, 'userLogin.html')
        

def conform3(request):
    global cand
    global cand_names
    cand = 3
    cand_names = contract.functions.candInfo().call()
    if userDetails:
        return render(request, 'conform.html',{'cand':cand, 'cand_name':cand_names[2]})
    else:
        return render(request, 'userLogin.html')