import typer
cli = typer.Typer(no_args_is_help=True)


@cli.command()
def start():
    print("Starting the service")


@cli.command()
def stop():
    print("Stopping the service")
