import click

from datetime import date
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.padding import Padding

from resumex.core.cli import cli, Context
from resumex.core.models import Company, Experience


@cli.group()
def xp():
    pass


@xp.command()
@click.pass_obj
def ls(ctx: Context):
    def construct_table() -> Table:
        table = Table(title="Experiences")
        table.add_column("Company")
        table.add_column("Location")
        table.add_column("Duration")
        return table

    table: Table = construct_table()
    resume = ctx.json_service.validate()
    for xp in ctx.json_service.get_experiences(resume):
        table.add_row(xp.company.name.upper(), xp.company.location, xp.duration)
    ctx.console.print(Padding(table, pad=(1, 0, 0, 4)))


@xp.command()
@click.pass_obj
def add(ctx: Context):
    rprint("\n")
    ## where ##
    ctx.console.rule("[bold]Company[/bold]")
    company = prompt_for_company()
    ## when ##
    ctx.console.rule("[bold]Duration[/bold]")
    start, end = prompt_for_date("Start", console=ctx.console), None
    if not click.confirm("Are you still working there?", default=True):
        end = prompt_for_date("End", console=ctx.console)
    ## what ##
    ctx.console.rule("[bold]Purpose[/bold]")
    position = Prompt.ask("Position")
    achievements = prompt_for_achievements() if should_prompt_for_achievements() else []

    ctx.backup_service.backup()
    xp = Experience(
        company=company,
        position=position,
        start_date=start,
        end_date=end,
        achievements=achievements,
    )
    ctx.json_service.add_experience(xp)


def should_prompt_for_achievements():
    msg = f"{click.style('Achievements', bold=True)} to add?"
    return click.confirm(msg, default=True)


def prompt_for_achievements():
    achievements: list[str] = []
    rprint("\n  Press <Enter> to finish\n")
    while True:
        achievement = Prompt.ask(
            "  :trophy: Achievement", default="", show_default=False
        )
        if achievement.strip() == "":
            break
        achievements.append(achievement)

    count = len(achievements)
    panel = Panel(f"Total: [bold green]{count}[/bold green]", expand=False)
    rprint(Padding(panel, pad=(0, 0, 0, 4)))
    return achievements


def prompt_for_date(label: str, console: Console) -> date:
    while True:
        date = Prompt.ask(label, console=console, default="", show_default=False)
        try:
            dt = click.DateTime(formats=["%Y-%m-%d", "%Y/%m/%d"])(date)
            return dt.date()
        except click.BadParameter:
            rprint("[red]Invalid format. Use YYYY-MM-DD or YYYY/MM/DD.[/red]")


def prompt_for_company() -> Company:
    return Company(name=Prompt.ask("Company"), location=Prompt.ask("Location"))
