""" DESCRIPTION:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""


def domain_name(url):
    lst = url.split("//")
    for i in lst:
        if i.count(".") >= 1:
            sap = i.split(".")
            for j in sap:
                if j == "www":
                    continue 
                else:
                    return j
        else:
            continue 

            
    pass
