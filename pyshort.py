import pyshorteners

link = input("Please type the link : ")

shortner = pyshorteners.Shortener()

output = shortner.tinyurl.short(link)

print(output)