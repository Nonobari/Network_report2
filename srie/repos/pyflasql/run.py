# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# License: check the LICENSE file.
"""
Run the main application.
"""
from app import PyFlaSQL


if __name__ == "__main__":
    #app.run(debug=True)
    PyFlaSQL.run(host='0.0.0.0', port=4990, debug=True)
