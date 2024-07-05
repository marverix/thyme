import typer
cli = typer.Typer(no_args_is_help=True)


@cli.command()
def start():
    print("Starting the day")


@cli.command()
def pause():
    print("Pausing the day")


@cli.command()
def resume():
    print("Resuming the day")


@cli.command()
def end():
    print("Ending the day")
