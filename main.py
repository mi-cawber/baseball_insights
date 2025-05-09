import requests as req

# use baseballmusings.com
#  the url is going to need to be dynamic
res = req.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py?EndDate=05%2F07%2F2025')

# shows html of the page
print(res.text)
