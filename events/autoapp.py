from app import create_app

app = create_app("config.develop")  # api/config/develop.py


if __name__ == "__main__":
    app.run(
        debug=app.config["DEBUG"],
        host=app.config["DB_ADDR"],
        port=app.config["SERVER_PORT"],
    )
