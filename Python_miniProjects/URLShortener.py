import pyshorteners

print("Welcome to URL Shortener")

url= input("Enter the url : ")

short_url = pyshorteners.Shortener().tinyurl.short(url)

print("Short URL : ", short_url)

