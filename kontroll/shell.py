import click
import click_completion

click_completion.init()

LOCAL_CONFIG = os.path.expanduser('~/.config/kontroll/config.yml')

def _validate(ctx, param, value):
    # For possible later validation
    return value
@click.group()
@click.option(
    '--debug/--no-debug',
    default=False,
    callback=_validate,
    help="Enable debug or disable debug, default is disabled"
)
@click.option(
    '--config',
    '-c',
    default=LOCAL_CONFIG,
    help="Configuration file to read from"
)
@click.version_option(version=kontroll.__version__)

@click.pass_context
def main(ctx, debug, config):
    ctx.obj = {}
    ctx.obj['args'] = {}
    ctx.obj['args']['debug'] = debug
    ctx.obj['args']['config'] = config

main.add_command(command.set.set)
