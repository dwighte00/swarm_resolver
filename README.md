swarm_resolver
=========

Simple bulk domain resolver based on aiodns and asyncio

```
This is a simple wrapper for aiodns. Initially I wanted to be able to asynchronously resolve a list of domains and this is what I did.
Makes use of https://github.com/saghul/aiodns and takes a list of domains to resolve. A queue of workers will try and resolve the list passed to them.
This library returns a dictionary of domain, [ pycares result types ] see https://github.com/saghul/pycares . In the case of an error the response type will 
be returned instead.
```

From the pycares docs:

The result type varies depending on the query type:

        A and AAAA: ares_query_simple_result, fields:
            host
            ttl
        CNAME: ares_query_cname_result, fields:
            cname
            ttl
        MX: ares_query_mx_result, fields:
            host
            priority
            ttl
        NAPTR: ares_query_naptr_result, fields:
            order
            preference
            flags
            service
            regex
            replacement
            ttl
        NS: ares_query_ns_result, fields:
            host
            ttl
        PTR: ares_query_ptr_result, fields:
            name
            ttl
        SOA: ares_query_soa_result, fields:
            nsmane
            hostmaster
            serial
            refresh
            retry
            expires
            minttl
            ttl
        SRV: ares_query_srv_result, fields:
            host
            port
            priority
            weight
            ttl
        TXT: ares_query_txt_result, fields:
            text
            ttl



 

Example output:

```
{'amazon.com': [ares_query_ns_result(host='pdns1.ultradns.net', ttl=None),
                ares_query_ns_result(host='ns4.p31.dynect.net', ttl=None),
                ares_query_ns_result(host='ns3.p31.dynect.net', ttl=None),
                ares_query_ns_result(host='ns2.p31.dynect.net', ttl=None),
                ares_query_ns_result(host='ns1.p31.dynect.net', ttl=None),
                ares_query_ns_result(host='pdns6.ultradns.co.uk', ttl=None)],
 'amazone.com': [ares_query_ns_result(host='ns-3.amazon.com', ttl=None),
                 ares_query_ns_result(host='ns-1.amazon.com', ttl=None),
                 ares_query_ns_result(host='ns-2.amazon.com', ttl=None)],
 'facebook.com': [ares_query_ns_result(host='a.ns.facebook.com', ttl=None),
                  ares_query_ns_result(host='b.ns.facebook.com', ttl=None)],
 'foobar.eu': [ares_query_ns_result(host='ns2.fo0bar.org', ttl=None),
               ares_query_ns_result(host='ns1.fo0bar.org', ttl=None)],
 'github.com': [ares_query_ns_result(host='ns-1283.awsdns-32.org', ttl=None),
                ares_query_ns_result(host='ns-1707.awsdns-21.co.uk', ttl=None),
                ares_query_ns_result(host='ns-421.awsdns-52.com', ttl=None),
                ares_query_ns_result(host='ns-520.awsdns-01.net', ttl=None),
                ares_query_ns_result(host='ns1.p16.dynect.net', ttl=None),
                ares_query_ns_result(host='ns2.p16.dynect.net', ttl=None),
                ares_query_ns_result(host='ns3.p16.dynect.net', ttl=None),
                ares_query_ns_result(host='ns4.p16.dynect.net', ttl=None)],
 'thisdomainisnotreal.xyy': 'NXDOMAIN',
 'twitter.com': [ares_query_ns_result(host='d01-01.ns.twtrdns.net', ttl=None),
                 ares_query_ns_result(host='ns4.p34.dynect.net', ttl=None),
                 ares_query_ns_result(host='d01-02.ns.twtrdns.net', ttl=None),
                 ares_query_ns_result(host='ns3.p34.dynect.net', ttl=None),
                 ares_query_ns_result(host='r01-01.ns.twtrdns.net', ttl=None),
                 ares_query_ns_result(host='r01-02.ns.twtrdns.net', ttl=None),
                 ares_query_ns_result(host='ns1.p34.dynect.net', ttl=None),
                 ares_query_ns_result(host='ns2.p34.dynect.net', ttl=None)],
 'youtube.com': [ares_query_ns_result(host='ns2.google.com', ttl=None),
                 ares_query_ns_result(host='ns4.google.com', ttl=None),
                 ares_query_ns_result(host='ns1.google.com', ttl=None),
                 ares_query_ns_result(host='ns3.google.com', ttl=None)]}


```


Running the test code
======================

To run the test code: ``python3 tests.py``


Author
======

adam <adam@threathive.com>


License
=======

aiodns uses the MIT license, check LICENSE file.


Python versions
===============
Python >= 3.6 should have no problems.

Contributing
============

If you'd like to contribute, fork the project, make a patch and send a pull request.

