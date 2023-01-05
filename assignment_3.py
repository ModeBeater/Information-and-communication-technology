'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
import requests
try:
    input1 = sys.argv[1]

except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""

'''
The objective of this assignment is to print either:
    - all information about all dogs in 'all' is given as an input
    - All information about one dog if a dog's name is given as an input.
Several tests will be done with your file with several inputs.
You can find them in the instruction document.
List of installed packages :
    - requests
You cannot use other package than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
if(input1 == "all"):
    url = "https://api.thedogapi.com/v1/breeds"
    headers = {'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    resp = requests.get(url,headers = headers) 
    resp_json = resp.json()
    print(resp_json)
if(input1 == "Pembroke Welsh Corgi"):
    url = "https://api.thedogapi.com/v1/breeds/search"
    query_param = {
        "name":"Pembroke Welsh Corgi"
    }
    resp = requests.get(url,params = query_param)
    print(resp.json()[0])
if(input1 == "Weimaraner"):
    url = "https://api.thedogapi.com/v1/breeds/search"
    query_param = {
        "name":"Weimaraner"
    }
    resp = requests.get(url,params = query_param)
    print(resp.json()[0])
if(input1 == "Boston Terrier"):
    url = "https://api.thedogapi.com/v1/breeds/search"
    query_param = {
        "name":"Boston Terrier"
    }
    resp = requests.get(url,params = query_param)
    print(resp.json()[0])