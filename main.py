def greet(name):
    return f"hello,{name}!"

if  __name__ =="__main__":
    print (greet("python class"))


import requests

r= requests.get("https://api.github.com")
print("github status:",r.status_code)