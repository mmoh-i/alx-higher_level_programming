#!usr/bin/python3
# Python script that fetches data

if __name__ == "__main__":
    import urllib.request
    with urllib.request.Request("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(body)))
        print("\t - contrnt: {}".format(body))
        print("\t - utf8 content: {}".format(body.decode("utf-8")))
