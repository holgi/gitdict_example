gitdict example
===============

This is an example project for the [gitdict][] package. 


what does it do?
----------------

This is only a small demonstration. It will install a small [pyramid][] web application, that is able to browse its own downloaded git repository. 


disclaimer
----------

I use [Python 3.5][py3] on a Mac. I didn't test this on any other setup than my own - so the continuous integration status is quite simple: Works For Me.


how to install
--------------

Fire up you favorite terminal and start typing:

### set up a virtual environment and activate it

    python3 -m venv example-env
    cd example-env
    source bin/activate

### install the required packages

Unfortunately this doesn't work automagically by just installing the example.

    pip install cffi
    pip install pygit2
    pip install gitdict

### clone and install the example application

    git clone https://github.com/holgi/gitdict_example.git
    cd gitdict_example
    python setup.py develop

There is a lot of output. You can read it if you like, but if the last line is something like `Finished processing dependencies for GitDictOnPyramid` then you are ready to go.

### run the local development server

    pserve development.ini                                                             

The output of the `pserve` command shows an URL that you should visit with your browser. On my setup it is [http://0.0.0.0:6543][pserve].


[gitdict]: https://github.com/holgi/gitdict
[pyramid]: http://www.pylonsproject.org
[py3]: https://www.python.org
[pserve]: http://0.0.0.0:6543
