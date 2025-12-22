import click

from rich.table import Table
from rich.padding import Padding

from resumex.core.cli import cli, Context
from resumex.templates.template import Template


@cli.group()
def template():
    pass


@template.command(help="List available templates")
@click.pass_obj
def ls(ctx: Context):
    def construct_table() -> Table:
        table = Table(title="Templates")
        table.add_column("Index")
        table.add_column("Name")
        return table

    table: Table = construct_table()
    templates = ctx.template_service.ls()
    for i, item in enumerate(templates):
        table.add_row(str(i), f"[bold cyan]{item}[/bold cyan]")
    ctx.console.print(Padding(table, pad=(1, 0, 0, 4)))


@template.command(help="Process the given LaTeX template")
@click.argument("template")
@click.option("--json", type=click.File("rb"))
@click.pass_obj
def render(ctx: Context, template: str, json: click.File):
    ctx.backup_service.backup()
    if json is not None:
        ctx.json_service.copy(json)

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

    ctx.template_service.render(template)
