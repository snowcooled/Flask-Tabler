===============
Flask-Tabler
===============

.. image:: https://travis-ci.org/mbr/flask-tabler.png?branch=master
   :target: https://travis-ci.org/mbr/flask-tabler

Flask-Tabler packages `Tabler
<http://gettabler.com>`_ into an extension that mostly consists
of a blueprint named 'tabler'. It can also create links to serve Tabler
from a CDN and works with no boilerplate code in your application.

Usage
-----

Here is an example::

  from flask_tabler import Tabler

  [...]

  Tabler(app)

This makes some new templates available, containing blank pages that include all
tabler resources, and have predefined blocks where you can put your content.

As of version 3, Flask-Tabler has a `proper documentation
<http://pythonhosted.org /Flask-Tabler>`_, which you can check for more
details.
