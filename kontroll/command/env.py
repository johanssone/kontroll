import click

from kontroll import logger
from kontroll.command import base

LOG = logger.get_logger(__name__)

@click.group()
def env():
    pass

@env.command()
def list():
    click.echo('lorem ipsum')

@env.command()
@click.argument('env')
def show(env):
    click.echo("lorem ipsum '{}'".format(env))

@env.command()
@click.option('--fromenvfile')
def create():
    click.echo('test')