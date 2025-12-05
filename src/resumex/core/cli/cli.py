import click

from resumex.core.di import ServiceProvider


@click.group()
@click.pass_context
def main(ctx):
    ctx.obj = ServiceProvider.get_instance()
