try:
    from googlesearch import search
except ImportError:
    print("Import Failed")

query = input(" Enter your Query : ")

for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)
