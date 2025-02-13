from bs4 import BeautifulSoup
import requests
import time

print("put some skills that you are familiar with")
unfamiliar = input('>')
print(f'filtering out {unfamiliar}')

def find_jobs():
    response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
    soup = BeautifulSoup(response.text, features="html.parser")
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        date = job.find('span',class_ = 'sim-posted').span.text
        if 'few' in date:
            name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
    
            if unfamiliar not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f" job : {name.strip()}\n")
                    f.write(f" req_skills : {skills.strip()}\n")
                    f.write(f" more_info : {more_info}\n")
                print('file saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} seconds...')
        time.sleep(time_wait)
  






