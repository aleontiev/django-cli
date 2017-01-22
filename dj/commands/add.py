from __future__ import absolute_import
import click
from dj.application import get_current_application
from dj.dependency import Dependency
from dj.utils import style
from .base import stdout


@click.argument('addon')
@click.option('--dev', is_flag=True)
@click.command()
def add(addon, dev):
    """Add a dependency.

    Examples:

    $ django add dynamic-rest==1.5.0

    + dynamic-rest == 1.5.0
    """
    stdout.write(style.format_command('Adding', Dependency(addon).to_stdout()))
    application = get_current_application()
    application.add(addon, dev=dev)