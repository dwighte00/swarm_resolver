from swarm_resolver import SwarmResolver
import requests
import pprint

if __name__ == '__main__':
    domains = [
        "facebook.com",
        "youtube.com",
        "twitter.com",
        "foobar.eu",
        "amazone.com",
        "amazon.com",
        "github.com",
        "thisdomainisnotreal.xyy"
    ]

    #Bigger testing speed
    #d = requests.get("https://raw.githubusercontent.com/opendns/public-domain-lists/master/opendns-random-domains.txt").text
    #for domain in d.split("\n"):
    #    domains.append(domain)


    swarm = SwarmResolver(qtype="NS", num_workers=10)
    pprint.pprint(swarm.resolve_list(domains))
