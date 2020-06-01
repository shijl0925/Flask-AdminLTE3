# Flask-AdminLTE3


Flask-AdminLTE3 packages [AdminLTE3](https://adminlte.io/themes/dev/AdminLTE/index.html) into an extension that mostly consists
of a blueprint named 'adminlte'. It can also create links to serve AdminLTE
from a CDN and works with no boilerplate code in your application.

## Installation

Installation using pip:

    pip install Flask-AdminLTE3
    

## Compatibility

This package is compatible Python versions 2.7, 3.4, 3.5 and 3.6.

## Usage

Here is an example:

    from flask_adminlte3 import AdminLTE3
    
    [...]
    
    AdminLTE3()(app)

This makes some new templates available, containing blank pages that include all
bootstrap resources, and have predefined blocks where you can put your content.
    

## Screenshots

Admin Area:
    
* Home :![admin screenshot](https://raw.githubusercontent.com/shijl0925/Flask-AdminLTE3/master/screenshots/home.png)

* Demo Model :![model screenshot](https://raw.githubusercontent.com/shijl0925/Flask-AdminLTE3/master/screenshots/demo-home.png)
