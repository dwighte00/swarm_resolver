import codecs
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version():
    return re.search(r"""__version__\s+=\s+(?P<quote>['"])(?P<version>.+?)(?P=quote)""", open('swarm_resolver/__init__.py').read()).group('version')


setup(name             = "swarm_resolver",
      version          = get_version(),
      author           = "Adam",
      author_email     = "adam@threathive.com",
      url              = "https://github.com/threathive/swarm_resolver",
      description      = "Simple bulk domain resolver for asyncio",
      long_description = codecs.open("README.md", encoding="utf-8").read(),
      install_requires = [
       'aiodns==1.1.1',
       'uvloop==0.11.3'
      ],
      extras_require = {
      },

      packages         = ['swarm_resolver'],
      classifiers      = [
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.6",
      ]
)
