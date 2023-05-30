import pyshorteners
s = pyshorteners.Shortener()
url = input("Enter the URL to shorten: ")
shortened_url = s.tinyurl.short(url)
print("Shortened URL:", shortened_url)
