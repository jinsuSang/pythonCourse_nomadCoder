import pip._vendor.requests as requests
from bs4 import BeautifulSoup
indeed_url = requests.get(
    "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=%EC%9D%B8%EC%B2%9C&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")


indeed_soup = BeautifulSoup(indeed_url.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')
pages = []

for link in links[:-1]:
    pages.append(int(link.string))
max_page = pages[-1]
