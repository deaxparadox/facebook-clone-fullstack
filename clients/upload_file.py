import requests

filename = r"C:\Users\91930\Documents\GITHUB\facebook-clone-fullstack\Jenkinsfile"
url = 'http://127.0.0.1:8000/uploadfile'
file = {'file': open(filename, 'rb')}
resp = requests.post(url=url, files=file) 
print(resp.json())
file['file'].close()