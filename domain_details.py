import whois

def domainDetails(link):
    domain = whois.whois(link)
    print("Server : ", domain.whois_server)
    print("Expiration Date : ", domain.expiration_date)
    print("Organisation : ", domain.org)
    print("State : ", domain.state)
    print("Country : ", domain.country)




url = input("Enter URL : ")

try:
    domain = whois.whois(url)
except:
    print("This domain is available")

else:
    print("This domain is already purchased")
    print("Information Below")
    domainDetails(url)