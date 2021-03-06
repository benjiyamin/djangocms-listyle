
import os
from setuptools import setup, find_packages

from djangocms_listyle import __version__


REQUIREMENTS = [
    'django-cms',
    'djangocms-style',
    # 'django-filer'
]


# def read(filename):
#     return open(os.path.join(os.path.dirname(__file__), filename)).read()

# def readlines(filename):
#     with open(os.path.join(os.path.dirname(__file__), filename)) as open_file:
#         return [l.split("==")[0] for l in open_file.readlines()]


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    name='djangocms-listyle',
    version=__version__,
    author='Ben Miller',
    author_email='mail@benkmiller.com',
    description='Adds a plugin to embed an ordered or unordered list to Django CMS. Children are automatically wrapped in <li> tags.',
    license='GNU General Public License v3 (GPLv3), see LICENSE.md',
    url='https://github.com/djangocms-listyle',
    packages=find_packages(exclude=["tests"]),
    long_description=open('README.md').read(),
    # install_requires=readlines('requirements/production.txt'),
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    test_suite='tests.settings.run',
)
