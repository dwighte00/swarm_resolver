from swarm_resolver import SwarmResolver
import pprint
import unittest


class SwarmTest(unittest.TestCase):
    def setUp(self):
        self. domains = [
            "facebook.com",
            "youtube.com",
            "twitter.com",
            "foobar.eu",
            "amazone.com",
            "amazon.com",
            "github.com",
            "thisdomainisnotreal.xyy"
        ]
        self.swarm = SwarmResolver(qtype="NS", num_workers=10)
        self.swarm2 = SwarmResolver(qtype="A", num_workers=10)


    def tearDown(self):
        self.swarm = None
        self.swarm2 = None

    def test_domain_list_resolve_ns(self):
        f = self.swarm.resolve_list(self.domains)
        self.assertTrue(f)

    def test_domains_resolve_a(self):
        f = self.swarm2.resolve_list(self.domains)
        self.assertTrue(f)

if __name__ == "__main__":
    unittest.main(verbosity=2)

