import typer
cli = typer.Typer(no_args_is_help=True)


@cli.command()
def init():


    print("Starting the day")


@cli.command()
def reset():
    print("Ending the day")
