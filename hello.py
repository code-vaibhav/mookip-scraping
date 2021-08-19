from bs4 import BeautifulSoup
import requests
import csv
import json

def scrap_mookit(n):
  login_url = 'https://hello.iitk.ac.in/index.php/user/login'
  course_url = 'https://hello.iitk.ac.in/api/eso208a21/lectures/summary'
  filename = 'result.csv'
  payload = {
    'name': "",
    'pass': "",
    'form_id': 'user_login_form'
  }

  with open(filename, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["lecture name", "week", "link"])

  with requests.Session() as s:
    s.post(login_url, data=payload)
    s.headers.update({'referrer': "https://hello.iitk.ac.in/eso208a21/"})
    token, uid = s.cookies.values()[2], s.cookies.values()[3]
    
    r = s.get(course_url, headers={'token': token, 'uid': uid})
    soup = BeautifulSoup(r.content, 'html.parser')
    data = json.loads(soup.text)

  for i in range(1, min(int(n), len(data))+1):
    l = data[-i]
    output = []
    name = l['title']
    week = l['week']
    link = 'https://hello.iitk.ac.in/eso208121/#lecture/' +  str(l['lid'])

    output.append(tuple((name, week, link)))

    with open(filename, 'a') as file:
      writer =csv.writer(file)
      writer.writerows(output)

def main():
  n = input('Enter how many lectures you want to scrap: ')
  scrap_mookit(n)
  
if __name__ == '__main__':
  main()