import json
from django.shortcuts import render
from eth_utils import address
import web3
from web3 import Web3

# Create your views here.

# ganache_url = "https://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
# web3.eth.default_account = web3.eth.accounts[0]
# abi = json.loads('')
# address = web3.toChecksumAddress("")

# contract = web3.eth.contract(address=address, abi=abi)

cand = 0

def index(request):
    return render(request,'index.html')

def userLogin(request):
    return render(request,'userLogin.html')

def userRegister(request):
    return render(request,'userRegister.html')

def adminLogin(request):
    return render(request, 'adminLogin.html')

def main (request):
    return render(request, 'admin.html')

def result(request):
    return render(request, 'result.html')

def vote(request):
    global cand
    cand = 0
    return render(request, 'vote.html',{'cand':cand})

def conform1(request):
    global cand
    cand = 1
    return render(request, 'conform.html',{'cand':cand})

def conform2(request):
    global cand
    cand = 2
    return render(request, 'conform.html',{'cand':cand})

def conform3(request):
    global cand
    cand = 3
    return render(request, 'conform.html',{'cand':cand})