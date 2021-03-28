"""
Author: Sahngwoo Kim
"""

import os
from view import create_app

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))   # The absolute path for the project

if __name__ == "__main__":
    app = create_app()

    # Running the website in local machine (use this statement for development)
    app.run(debug=True)
