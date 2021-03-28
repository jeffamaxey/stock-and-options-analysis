from view import create_app

if __name__ == "__main__":
    app = create_app()

    # Running the website in local machine (use this statement for development)
    app.run(debug=True)
