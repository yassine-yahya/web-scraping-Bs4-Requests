import requests
from bs4 import BeautifulSoup
import socket
from colorama import Fore, init

init()



#function check http security headers
def check_http_security_headers(response):
    
    headers = response.headers
    
    print("http headers check: ...")
    
    security_headers = [
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-XSS-Protection",
        "Content-Security-Policy",
        "X-Frame-Options",
        "Referrer-Policy"
    ]
    #loop in security headers list and pick the header
    for header in security_headers:
        if header in headers:
            print(f"{Fore.YELLOW}{header}: {headers[header]}")
        else:
            print(f"{Fore.RED}{header}: Missing")
    
    


#function Scraping
def Scraping():
    try:
        #send request to the website and validate url
        url = input("enter url: ")
        if not url.startswith(("http://", "https://")):
            print("Invalid URL, make sure to include http or https")
            return
         
            
        response = requests.get(url)
        
        if response.status_code !=200:
            print(f"Error: Received a {response.status_code} response")
            
            #call the function
        check_http_security_headers(response)
        
        
        print(f"{Fore.GREEN}Scraping...{url}{Fore.RESET}")
        #parse the html of webpage
        soup = BeautifulSoup(response.content, "html.parser")
        
        #extract the title
        title = soup.title.string if soup.title else "No Title found!"
        
        print(f"{Fore.LIGHTMAGENTA_EX}Title: {title}")
        
        #extract the Links
        links = soup.find_all("a", href=True)
        for link in links:
            href = link.get("href")
            print(f"Link: => {href}")
            
        #handle errors
    except socket.error as e:
        print(f"Error scraping: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


Scraping()

