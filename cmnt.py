from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pythonosc import udp_client

 # change ip to your own ipv4 address
ip = "192.168.0.101"
port = 2000

client = udp_client.SimpleUDPClient(ip, port)  # Create client

 # change this to your own webdriver
browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

 # change the link below to your preference
browser.get('https://www.twitch.tv/asmongold')

while True:
    # get source code
    # set some wait time to load page content properly
    time.sleep(2)
    html = browser.page_source

    soup_file = browser.page_source

    soup = BeautifulSoup(soup_file, 'html.parser')
 
    # get all 'text-fragment' classes
    cmnt = [x.get_text() for x in soup.find_all('span', attrs={'class': 'text-fragment'})]

    client.send_message("/some/address", [cmnt])  # Send message with int, float and string

    print(cmnt)
