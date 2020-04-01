# sesHTTPD

sesHTTPD is a static-file webserver written in Python 3. It uses sockets and does **not** rely on the SimpleHTTPServer module.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x or newer
- The os, sys, mimetypes, and socket modules installed (you can get them with `python3 -m pip install <module>`)

### Installing

1. Download the repository (or clone it with `git clone`)
2. Run the script (`python3 seshttpd.py`) in the directory where your webpages live
3. Visit the address in your browser (it will be some form of `localhost:<PORT>` or similar)
4. Done!

You may want to run sesHTTPD behind nginx or some other proxy.

### Command-Line Arguments

sesHTTPD takes one (optional) argument. This is the port you want to bind the webserver to. For example, you would run `python3 seshttpd.py 8080` if you wanted to bind sesHTTPD to port 8080.

If you do not provide a port, or sesHTTPD cannot bind to the port you requested, it will choose a random one.

## Built With

* [Python 3](http://www.python.org)

## Authors

* **Nitin Seshadri** - *Initial work*

See also the list of [contributors](https://github.com/nitinseshadri/seshttpd/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
