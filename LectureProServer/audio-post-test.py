import requests

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

url = "http://localhost:8080/Lecture"
fin = open('test.wav', 'rb')
files = {'file': fin}
try:
  r = requests.post(url, files=files)
  print(r)
  print ("dddd")
finally:
	fin.close()