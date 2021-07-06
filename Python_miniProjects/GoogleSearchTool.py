# import module
from googlesearch import search

print("Welcome to Google search tool")

# Taking query
query = input("What do you want to search on google ? : ")

for i in search(query, start=0, stop=10):
    print(i)