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


    def tearDown(self):
        self.swarm = None

    def test_domain_list(self):
        f = self.swarm.resolve_list(self.domains)
        self.assertTrue(f)

if __name__ == "__main__":
    unittest.main(verbosity=2)

