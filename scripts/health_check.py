import urllib.request

url = "http://localhost:8080"

try:
    response = urllib.request.urlopen(url, timeout=5)

    if response.status == 200:
        print("SUCCESS: Application is running!")
    else:
        print("WARNING: Application returned an error!")

except Exception as error:
    print("ERROR: Application is not responding!")
    print(error)
