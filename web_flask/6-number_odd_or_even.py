#!/usr/bin/python3
"""
script to start Flash web application
listens on 0.0.0.0, port 5000
routes:
/: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C" followed by value of text variable
/python/(<text>): display "Python" followed by value of text
/number/<n>: display "n is a number" only if n is int
/number_template/<n>: display HTML page only if n is int
/number_odd_or_even/<n>: display HTML page only if n is int
"""
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """
        displays "Hello HBNB!"
        """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """
        displays "HBNB"
        """
        return "HBNB"

    @app.route('/c/<path:text>', strict_slashes=False)
    def c(text):
        """
        displays "C" followed by value of variable list text
        underscores in <text> replaced with spaces
        """
        for i in range(len(text)):
            if text[i] == '_':
                text = text[:i] + ' ' + text[i+1:]
        c_message = "C " + text
        return c_message

    @app.route('/python', strict_slashes=False)
    @app.route('/python/<path:text>', strict_slashes=False)
    def python(text=None):
        """
        displays "Python" followed by value of variable list text
        underscores in <text> replaced with spaces
        default if no text given is "is cool"
        """
        if text is None:
            text = "is cool"
        else:
            for i in range(len(text)):
                if text[i] == '_':
                    text = text[:i] + ' ' + text[i+1:]
        python_message = "Python " + text
        return python_message

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        """
        displays "n is a number" where n is int argument
        only displays if n is integer
        """
        if type(n) is int:
            n_message = str(n) + " is a number"
            return n_message

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """
        displays HTML page with H1 tag: "Number: n"
        only displays if n is integer
        """
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        """
        displays HTML page with H1 tag: "Number: n is even|odd"
        only displays if n is integer
        """
        if n % 2 is 0:
            value = "even"
        else:
            value = "odd"
        return render_template('6-number_odd_or_even.html', n=n, value=value)

    app.run(host='0.0.0.0', port='5000')
