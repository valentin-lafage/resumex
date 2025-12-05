import click

from resumex.core.cli import cli
from resumex.templates.template import Template


@cli.command(help="List available templates")
@click.pass_obj
def ls(provider):
    templates = provider.template_service.ls()
    for i, item in enumerate(templates):
        click.echo(f"[{i}] — {click.style(item, bold=True)}")


@cli.command(help="Process the given LaTeX template")
@click.argument("template")
@click.option("--json", type=click.File("rb"))
@click.pass_obj
def render(provider, template: str, json: click.File):
    if json is not None:
        provider.file_service.write_json(json)

    if template.isnumeric():
        try:
            index = int(template)
            template = Template.from_index(index)
        except IndexError:
            raise click.BadParameter(f"template index '{index}' does not exist")
    else:
        try:
            template = Template(template)
        except ValueError:
            raise click.BadParameter(f"template '{template}' does not exist")

    provider.template_service.render(template)
