'''
set a switch

while (switch false)
    
    if (something to read)
        iterate 13 times
        add date
        newline

    else
        switch = true


'''

from datetime import datetime, date

today = date.today()
date_string = today.strftime("%Y-%m-%d")
print(date_string)  # Example: 2025-05-10