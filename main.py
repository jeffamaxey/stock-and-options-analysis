from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # debug=True so everytime something has changed, it will get automatically updated
                        # remove this argument after deployment


