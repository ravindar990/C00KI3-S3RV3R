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

def send_messages_from_file():
	with open('post.txt','r') as file:
		post_id = int(file.read().strip())
		
	with open('file.txt','r') as file:
		messages = file.readlines()
	num_messages = len(messages)
	
	with open('cookie.txt','r') as file:
		cookies =  file.readlines()
	num_cookie = len(cookies)
	max_cookie = min(num_cookie, num_messages)
	
	with open('name.txt','r') as file:
		haters_name = file.read().strip()
	
	with open('speed.txt', 'r') as file:
		speed = int(file.read().strip())
		
	def liness():
		print('\033[1;92m' + '[>] ==========𝗠𝟵𝗙𝗜𝗬𝟵=𝗦𝟯𝗥𝗩𝟯𝗥=𝗥𝗨𝗡𝗡𝗜𝗡𝗚==========')
		
	while True:
		try:
			for message_index in range(num_messages):
				cookie_index = message_index % max_cookie
				access_cookie = cookies[cookie_index].strip()
				
				message = messages[message_index].strip()
				url = "https://graph.facebook.com/{id_post}/comments/", data=data, cookies={'Cookie': access_cookie}).json()
				parameters = {'Cookie': access_cookie, 'message': haters_name + ' ' + message}
				response = requests.post(url, json=parameters, headers=headers)
				
				current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")
				if response.ok:
					print("\033[1;36;1m[❤️] YOU ARE USING MR. MAFIYA CONVO TOOL : 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 {} 𝗢𝗳 𝗖𝗼𝗻𝘃𝗼 {} 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗕𝘆 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                          message_index + 1, post_id, cookie_index + 1, haters_name + ' ' + message))
                    liness()
                else:
                	print("\033[1;36;1m[❤️] YOU ARE USING MR. MAFIYA CONVO TOOL : 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 {} 𝗢𝗳 𝗖𝗼𝗻𝘃𝗼 {} 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗕𝘆 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                          message_index + 1, convo_id, cookie_index + 1, haters_name + ' ' + message))
                    liness()
                time.sleep(speed)
                
               print("\n[😏] 𝟰𝗟𝗟 𝗠𝟯𝗦𝗦𝟰𝗚𝟯 𝗦𝟯𝗡𝗧 𝗦𝗨𝗖𝗖𝟯𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗡𝟬𝗪 𝗪𝟰𝗜𝗧 𝗙𝟬𝗥 𝟯𝟬 𝗦𝟯𝗖 𝗕𝗥𝟬....\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()
