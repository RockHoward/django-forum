from setuptools import setup, find_packages
 
version = '0.1'
 
LONG_DESCRIPTION = """
This is a basic forum component that can plug into any existing Django installation
and use its' existing templates, users, and admin interface. Perfect for adding
forum functionality to an existing website.
"""
 
setup(
    name='django-forum',
    version=version,
    description="django-forum",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Other/Nonlisted Topic",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='forum,django',
    author='Ross Poulton',
    author_email='ross@rossp.org',
    url='http://django-forum.googlecode.com/',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
