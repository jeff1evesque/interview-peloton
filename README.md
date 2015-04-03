interview-peloton
================

A coding [exercise](https://github.com/jeff1evesque/interview-peloton/blob/master/data/PelotonCycleBackendTestTask.pdf) was given to me, when I interviewed for a Backend Software Engineer position at [Peloton Cycle](https://www.pelotoncycle.com/).  This exercise was not restricted with a time limit.  However, was recommended to take a few hours.  Since this exercise was premised on the python language, no arbitrary css, or javascipt was coded.

**Note:** the exercise [instructions](https://github.com/jeff1evesque/interview-peloton/blob/master/data/PelotonCycleBackendTestTask.pdf) can be found in the [`data/`](https://github.com/jeff1evesque/interview-peloton/tree/master/data/) subdirectory.

## Installation

###Linux Packages

The following packages are needed to be installed:

```
# General Packages:
sudo apt-get install python-pip
sudo pip install Flask
sudo pip install requests
sudo apt-get install memcached
```

**Note:** This project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system. If another system is preferred, simply download the above requirements, with respect to the systems *package manager* equivalent.

## Configuration

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /var/www/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/interview-peloton.git
```

Then, change the *file permissions* for the entire project by issuing the command:

```
cd /var/www/interview-peloton/
sudo chown -R jeffrey:sudo interview-peloton
```

**Note:** change 'jeffrey' to the user account YOU use.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```
cd /var/www/interview-usnews/
git remote add upstream https://github.com/[YOUR-USERNAME]/interview-peloton.git
```

###Memcached

This project implements [memcached](http://memcached.org/) as a means to store in-memory, key-value pairs of data.  Specifically, the result of the python [`requests`](https://github.com/jeff1evesque/interview-peloton/blob/master/README.md#requests), is converted into a json object, then stored within a memcached object.  This process can be seen within [`cached_stream.py`](https://github.com/jeff1evesque/interview-peloton/blob/master/logic/cached_stream.py), which contains the `cached_stream` function, implemented within [`app.py`](https://github.com/jeff1evesque/interview-peloton/blob/master/app.py).

###Flask

Python's [Flask](http://flask.pocoo.org/), is a microframework based on [Werkzeug](http://werkzeug.pocoo.org/).  Specifically, it is a [web framework](http://en.wikipedia.org/wiki/Web_application_framework), which includes, a development server, integrated support for [unit testing](http://en.wikipedia.org/wiki/Unit_testing), [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) API, and [Jinja2](http://jinja.pocoo.org/) templating.

This project implements flask, by requiring [`app.py`](https://github.com/jeff1evesque/interview-peloton/blob/master/app.py) to be running:

```
cd /var/www/html/interview-us-news/
python app.py
```

**Note:** the [`run()`](http://flask.pocoo.org/docs/0.10/api/#flask.Flask.run) method within `app.py`, runs the local developement server, and has the ability of defining the host, port, debug feature, and several other options. If none of these attributes are passed into the method, the server will default to running `localhost` on port `5000`, with no [`debug`](http://flask.pocoo.org/docs/0.10/quickstart/#debug-mode) features enabled.

**Note:** when running the above `app.py`, ensure that the terminal window is not used for any other processes, while the web application is available to others.

###Requests

Python's [`requests`](http://docs.python-requests.org/) API, provides an elegant, yet easy implementation for making various [HTTP requests](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods).  This project implements the `get` request, to parse the supplied `json` response, from the [Peloton API](ttps://api.pelotoncycle.com/quiz/next/stream_name), from a specified external webpage.

The following `requests` implementation is made within [`parser.py`](https://github.com/jeff1evesque/interview-peloton/blob/master/logic/parser.py):

```
  response = requests.get('https://api.pelotoncycle.com/quiz/next/' + stream)
  return r.json()
```

**Note:** the above `json()` method, decodes the `response` as a json object.

##Execution

Once `app.py` is running on a dedicated terminal window, this application can be accessed via any web-browser:

```
http://localhost:5000/
```
