from api import create_app

# create app
app = create_app()

if __name__ == '__main__':
    # run app
    app.run(host="0.0.0.0", port=5000)