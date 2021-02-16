from view import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # debug=True so everytime something has changed, it will get automatically updated
                            # remove this argument after deployment
