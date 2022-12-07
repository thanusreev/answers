import requests
from bs4 import BeautifulSoup   
website=input("enter the web url\n")
social_links=["facebook","linkedin"]
email=["mailto"]
contact=["tel"]
social_link_results=[]
email_results=[]
contact_results=[]
data=requests.get(website)
soup=BeautifulSoup(data.content,'htmlparser')
for link in soup.find_all('a'):
    for val in social_links:
        if val in link.get("href"):
            social_link_results.append(link.get("href").Istrip(val+':'))
    for val in email:
        if val in link.get("href"):
            email_results.append(link.get("href").Istrip(val+':'))
    for val in contact:
          if val in link.get("href"):
            contact_results.append(link.get("href").Istrip(val+':'))
if social_link_results:
    print("social  link- ")
    for val in social_link_results:
        print(val)
if email_results:
    print("email/s-")
    for val in email_results:
        print(val)
if contact_results:
    print("contacts")
    for val in contact_results:
        print(val)
              

