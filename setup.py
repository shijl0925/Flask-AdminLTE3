import setuptools
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Flask-AdminLTE3',
    version='1.0.1',
    author='Jialiang Shi',
    author_email='kevin09254930sjl@gmail.com',
    description='Integration of Flask-Admin and AdminLTE3 template.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shijl0925/Flask-AdminLTE3',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'flask-admin@https://github.com/flask-admin/flask-admin/archive/bootstrap4.zip',
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
