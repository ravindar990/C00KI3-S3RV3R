import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"   MR MAFIYA INXIDE")
def execute_server():
      PORT = int(os.environ.get('PORT', 4000))

      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()

def lines():
	print("[[>]] ===================M4FIY4=S3RV3R=RUNNING===================")

with open('password.txt','r') as file:
	pwd = file.read().strip()
mmm = requests.get('https://pastebin.com/raw/wEiJXrN3').text
if mmm not in pwd:
	print("PASSWORD CHANGED BY MAFIYA PLS CONTACT")
	sys.exit()
	
def cookie_file():
	try:
		lines()
		with open('cookie.txt','r') as f:
			cookie = f.read().splitlines()
		return cookie
	except FileNotFoundError:
		print("PLS SELECT VALID FILE")
		return None

def make_request(url, headers, cookie):
    try:
        response = requests.get(url, headers=headers, cookies={'Cookie': cookie}).text
        return response
    except RequestException as e:
        print("\033[1;31m[!] Error making request:", e)
        return None

def time():
    print("\033[1;36mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))

    while True:
        try:
            cookies_data = cookie_file()
            if cookies_data is None:
                break

            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
            }

            valid_cookies = []
            for cookie in cookies_data:
                response = make_request('https://business.facebook.com/business_locations', headers=headers, cookie=cookie)
                if response and 'EAAG' in response:
                    try:
                        token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
                        valid_cookies.append((cookie, token_eaag))
                    except AttributeError:
                        continue

            if not valid_cookies:
                print("\033[1;31m[!] No valid cookie found. Exiting...")
                break

            id_post = int(open("post.txt").readline().strip())
            commenter_name = open("name.txt").readline().strip()
            delay = int(open("speed.txt").readline().strip())

            comment_file_path = "file.txt"

            with open(comment_file_path, 'r') as file:
                comments = file.readlines()

            x, y, cookie_index = 0, 0, 0

            while True:
                try:
                    time.sleep(delay)
                    teks = comments[x].strip()
                    comment_with_name = f"{commenter_name}: {teks}"

                    current_cookie, token_eaag = valid_cookies[cookie_index]
                    data = {
                        'message': comment_with_name,
                        'access_token': token_eaag
                    }
                    response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={'Cookie': current_cookie}).json()

                    if 'id' in response2:
                        print("\033[1;32mPost id ::", id_post)
                        print("\033[1;32mDate time ::", time.strftime("%Y-%m-%d %H:%M:%S"))
                        print("\033[1;32mCOOKIE NUMBER : {}" , cookie_index +1)
                        print("\033[1;32mComment sent ::", comment_with_name)
                        lines()
                        x = (x + 1) % len(comments)
                        cookie_index = (cookie_index + 1) % len(valid_cookies)
                    else:
                        y += 1
                        print("\033[1;31m[{}] Status : Failure".format(y))
                        print("\033[1;32COOKIE NUMBER : {}" , cookie_index +1)
                        print("\033[1;31m[/]Link : https://m.basic.facebook.com//{}".format(id_post))
                        print("\033[1;31m[/]Comments : {}\n".format(comment_with_name))
                        

                except RequestException as e:
                    print("\033[1;31m[!] Error making request:", e)
                    time.sleep(5.5)
                    continue

        except Exception as e:
            print("\033[1;31m[!] An unexpected error occurred:", e)
            break

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      time()

if __name__ == "__main__":
    main()
