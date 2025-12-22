import click

from dataclasses import dataclass
from rich.console import Console
from rich.table import Table
from rich.padding import Padding

from resumex.core.cli import cli
from resumex.core.di import ServiceProvider
from resumex.core.services import BackupService, JsonService, TemplateService
from resumex.templates.template import Template


@dataclass
class Context:
    console: Console
    json_service: JsonService
    backup_service: BackupService
    template_service: TemplateService


@cli.group
@click.pass_context
def template(ctx):
    service_provider = ServiceProvider.get_instance()
    ctx.obj = Context(
        console=Console(),
        json_service=service_provider.json_service,
        backup_service=service_provider.backup_service,
        template_service=service_provider.template_service,
    )


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
