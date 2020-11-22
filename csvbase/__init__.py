import click
from .data_server import *


@click.command()
@click.option(
    "--port",
    "port",
    default=5000,
    type=click.INT,
    show_default=True,
    help="Port for Flask to run",
)
@click.option(
    "--dir",
    "dir",
    default=None,
    type=click.STRING,
    show_default=True,
    help="Directory to be mapped",
)
@click.option("--debug/--no-debug", default=False)
def main(port, dir, debug):
    if dir is None:
        BASE_DIR = os.getcwd()
    else:
        BASE_DIR = dir

    app = Flask(__name__)
    app.config["DEBUG"] = debug

    @app.route("/", methods=["GET"])
    def home_app():
        return home()

    @app.route("/", defaults={"req_path": ""})
    @app.route("/<path:req_path>")
    def dir_listing_app(req_path):
        return dir_listing(req_path)

    @app.route("/SQL", defaults={"query": ""}, methods=["GET"])
    def sql_app(query=""):
        return sql(query)

    app.run()


if __name__ == "__main__":
    main()
