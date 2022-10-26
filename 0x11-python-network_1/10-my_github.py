#!/usr/bin/python3
# python script to get my gityhub Api
import requests
import sys
if __name__ == "__main__":
  headers = {"username": sys.argv[1], "Authorization": "token {}".formaa(sys.argv[2])}
  #payload = {"username":, "password":}
  url = "https://api.github.com/user/{}".format(sys.argv[1])
  req = requests.get(url, headers=headers)
  if req.status_code == 200:
    response = request.json()
    if user['login'] == sys.argv[1]:
      print(user['id'])
    else:
      print('None')
  else:
    print(None)
