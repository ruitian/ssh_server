# -*- coding: utf-8 -*-
from app import app
from views import *  # noqa

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

