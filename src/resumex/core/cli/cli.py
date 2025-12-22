import click

from dataclasses import dataclass
from rich.console import Console

from resumex.core.di import ServiceProvider
from resumex.core.services import BackupService, JsonService, TemplateService


@dataclass(frozen=True)
class Context:
    console: Console
    json_service: JsonService
    backup_service: BackupService
    template_service: TemplateService


@click.group()
@click.pass_context
def main(ctx):
    service_provider = ServiceProvider.get_instance()
    ctx.obj = Context(
        console=Console(),
        json_service=service_provider.json_service,
        backup_service=service_provider.backup_service,
        template_service=service_provider.template_service,
    )
