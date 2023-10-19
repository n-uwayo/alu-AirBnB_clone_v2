#!/usr/bin/python3
"""
script to start Flash web application
listens on 0.0.0.0, port 5000
uses storage to fetch data from storage engine
declares method to teardown SQLAlchemy session
routes:
/states_list: displays HTML page with State and list of all state objects
/cities_by_states: displays HTML page with list of cities by state from storage
"""
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template
    from models import storage
    from operator import attrgetter
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """
        fetches data from storage engine and displays rendered HTML page
        """
        states = storage.all("State")
        result = states.values()
        states_result = sorted(result, key=attrgetter('name'))
        return render_template('7-states_list.html',
                               states_result=states_result)

    @app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        """
        fetches data from storage engine and displays rendered HTML page
        uses cities relationship or getter to list cities by state
        """
        states = storage.all("State")
        result = states.values()
        states_result = sorted(result, key=attrgetter('name'))
        return render_template('8-cities_by_states.html',
                               states_result=states_result)

    @app.teardown_appcontext
    def teardown(self):
        """
        removes current SQLAlchemy Session after each request
        """
        storage.close()

    app.run(host='0.0.0.0', port='5000')
