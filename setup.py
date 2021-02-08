import setuptools
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Flask-AdminLTE3',
    version='1.0.4',
    author='Jialiang Shi',
    author_email='kevin09254930sjl@gmail.com',
    description='AdminLTE3 Theme for Flask-Admin.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shijl0925/Flask-AdminLTE3',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'flask-admin>=1.5.7',
        'Flask>=0.8',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
