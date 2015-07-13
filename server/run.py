'''
Run the SportStat REST Server
'''

from flask import url_for
from server import app

if __name__ == '__main__':
    import sys
    port = 3000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except Exception as e:
            print('Must specify valid port, or use default ({0})'.format(port))
            sys.exit()

    # testing request url context
    with app.test_request_context():
        print(url_for('home'))
        print(url_for('api_help'))

    # enables hot reload
    app.debug = True
    # TODO: dangerous: 0.0.0.0 will run on public IP--don't run this on public network
    app.run(host='0.0.0.0', port=port)

