import re
text="hello tea, ,our new product launch is planned for 24/03/2026 at10.30AM please contact marketingteam@startupAI.com or support@startupAI.com #product the price 20022$ #one" 
hashtags=re.findall(r"#\+",text)
mentions=re.findall(r"@\w+",text)
emails= re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b",text)
urls=re.findall(r"https?:/^s+",text)
dates = re.findall(r"\b\d{1,2}^d{1,2}^d{4}\b",text)
tokens=re.findall(r"\b\w+\b",text)
print(hashtags)
print(mentions)
print(emails)
print(urls)
print(dates)
print(tokens)
