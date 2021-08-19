# PClub Mookit Scraping Task

This repository contains my implementaion of PClub mookit scraping task.

- I used **Requests** to create a session with my login credentials and to make requests.
- I used **json** to parse tha data make data readable.
- I used **BeautifulSoup** also to make html readable.
- Used **csv** to write csv file and save it.

<hr>

## My Steps

I had no idea of scraping the data and this was my implementation of these scraping tasks.

So then How I reached to the solution?

- First I tried to search to the web and find out some tools to perform data scraping.
- Then i tried to know about how mookit is fetching data and working on it.
- Then i found out i have to create a session and work on make some requests on the sites to get the data.
- Then after lot of research i found mookit is calling some API's to fetch the data from a server and feeding it on the HTML.
- Then i used these api to get the lecture details and parsed it and write it on the csv file using *csv* library.

<hr>

## How To Use

Download the hello.py file feed your IITK credentials in the payload and just run this file using 
<br>

1. Run `pip3 install -r requirements.txt` to install dependencies
2. Then use command `python hello.py`

Then Prompt appers
```
Enter how many lectures you want to scrap:
```

Just Put in the numberand then you can see the result in the **result.csv** file

Sample Output:
```
lecture name,week,link

Bracketing Methods,Week 2,https://hello.iitk.ac.in/eso208121/#lecture/19
...
```

Note - Currently this will only fetch ESO 208 latest lectures.
