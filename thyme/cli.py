import typer

import thyme.commands.service as command_service
import thyme.commands.workday as command_workday
import thyme.commands.month as command_month
from .version import version as __version__


cli = typer.Typer(no_args_is_help=True)
cli.add_typer(command_service.cli, name="service")
cli.add_typer(command_workday.cli, name="workday")
cli.add_typer(command_month.cli, name="month")


def version_callback(value: bool):
    if value:
        typer.echo(f"Thyme version {__version__}")
        raise typer.Exit()


@cli.callback()
def main(
    version: bool = typer.Option(None, "--version", callback=version_callback, is_eager=True),
):
    # Do other global stuff, handle other global options here
    return


def run():
    cli(prog_name="thyme")


# if __name__ == "__main__":
#     run()
