from setuptools import setup

execfile('magicalbum/version.py')

setup(
    name='django-magic-album',
    version=__version__,
    description="Django Magic Album is an album that picks picutes from " +
    "Twitter, sends emails and posts to Facebook",
    long_description=open('README.md').read(),
    author="Ivan Neto",
    author_email="ivan.cr.neto@gmail.com",
    url="http://github.com/ivancrneto/django-magic-album",
    packages=['magicalbum'],
    include_package_data=True,
    install_requires=[
        'celery',
        'django-jsonfield',
        'South',
    ]
)
