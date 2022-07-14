from project import create_app

app = create_app()
#populate_db(app)

if __name__ == "__main__":
    #app.run(ssl_context=('cert.pem', 'key.pem'))
    app.run()