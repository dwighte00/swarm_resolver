import asyncio
import aiodns

__version__ = '0.1.1'


class SwarmResolver:
    """ A simple class which will resolve a list of domains asyncrionously """

    def __init__(self, num_workers=5, nameservers = [ '8.8.8.8' , '8.8.4.4' ] , loop = None, qtype = "A"):
        self.loop = loop or asyncio.get_event_loop()
        assert self.loop is not None

        self.num_workers = num_workers
        self.nameservers = nameservers
        self.qtype = qtype
        self.results = {}

    #Creates a task queue made up of all the domains within the passed list.
    #Will startup an event loop and split up the list amongst num_workers worth of workers. 
    #Returns the list of domains within domain_list as well as the results of their dns lookup.
    def resolve_list(self , domain_list):
        tasks = []
        q = asyncio.Queue()

        for domain in domain_list:
            q.put_nowait(domain)

        for i in range(self.num_workers):
            tasks.append(self.do_work(q))

        self.loop.run_until_complete(asyncio.wait(tasks))
        return(self.results)

    #Will asynchronously perform a DNS lookup for the qtype and for the domains within the current shared Queue.
    #Will populate the shared results dictionary with results for each performed dns lookup.
    async def do_work(self, work_queue):
            resolver = aiodns.DNSResolver(loop=self.loop, nameservers=self.nameservers , timeout=2 , tries=1)

            while not work_queue.empty():
                domain = await work_queue.get()
                try:
                    res = await resolver.query(domain, self.qtype)
                    self.results[domain] = res
                except aiodns.error.DNSError as e:
                    error_code = e.args[0]
                    if error_code == aiodns.error.ARES_ECONNREFUSED:
                        self.results[domain] = "CONNECTION_REFUSED"
                    elif error_code == aiodns.error.ARES_ENODATA:
                        self.results[domain] = "NODATA"
                    elif error_code == aiodns.error.ARES_ENOTFOUND:
                        self.results[domain] = "NXDOMAIN"
                    elif error_code == aiodns.error.ARES_EREFUSED:
                        self.results[domain] = "REFUSED"
                    elif error_code == aiodns.error.ARES_ESERVFAIL:
                        self.results[domain] = "SERVFAIL"
                    elif error_code == aiodns.error.ARES_ETIMEOUT:
                        self.results[domain] = "TIMEOUT"
                    else:
                        self.results[domain] = "UNKNOWN_STATUS"
                
                except Exception as e:
                    print(e)

                work_queue.task_done()

    #Heloper for handling exceptions.
    async def handle_exception():
        try:
            await bug()
        except Exception:
            print("exception consumed")
