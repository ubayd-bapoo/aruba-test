import os
import click
import logging
import uvicorn

from fastapi import FastAPI

from service_app.routers import RouterRegister

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create a logger
logger = logging.getLogger(__name__)
app = FastAPI(title='Aruba Test',
              description="A FastAPI application with custom Swagger documentation for Aruba test.",
              version="1.0.0")


@app.on_event("startup")
def startup_events():
    RouterRegister.register(app)


@click.command()
@click.option("--port", default=8000, type=click.INT, help="Port to serve on.")
@click.option("--host", default="0.0.0.0", type=click.STRING, help="Host to serve on.")
def serve(port, host):
    uvicorn.run(
        "service:app",
        host=host,
        port=port,
    )


if __name__ in "__main__":
    # Pre check
    logging.info('Starting Pre checks')
    if not os.environ.get('KEY'):
        logging.error('No key found, exiting application')
    else:
        serve()
