import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='salt-manager',
    version='0.0.1',
    packages=['salt-manager'],
    include_package_data=True,
    license='BSD License',
    description='A Django project for managing salt stack. The goal is to \
                create a ui based configuration management and monitoring \
                platform that uses salt as the underlining framework.',
    long_description=README,
    url='https://github.com/rangertaha/salt-manager',
    author='Rangertaha',
    author_email='rangertaha@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers, DevOps, Sys Admins',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

