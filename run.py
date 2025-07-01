from flask import render_template, request, redirect, url_for


from aplication import aplication
from aplication.controllers import ControllerDefault

import logging
from pythonjsonlogger import jsonlogger

logHandler = logging.FileHandler('security.log')
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
logHandler.setFormatter(formatter)

logger = logging.getLogger('security')
logger.setLevel(logging.INFO)
logger.addHandler(logHandler)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Dummy logic for demonstration:
    if username != "admin" or password != "secret":
        logger.warning('Failed login attempt', extra={'username': username, 'ip': request.remote_addr})
        return "Login failed", 401
    return "Login successful"

@app.route('/admin')
def admin():
    if not request.args.get('is_admin'):
        logger.warning('Unauthorized access attempt', extra={'username': 'anonymous', 'resource': '/admin', 'ip': request.remote_addr})
        return "Unauthorized", 403
    return "Welcome admin!"

if __name__ == '__main__':
    app.run()



if __name__ == '__main__':
    aplication.run(debug=True, port=(5310))
