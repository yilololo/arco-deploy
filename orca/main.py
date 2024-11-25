from arco_deploy import main as deploy_main
from arco_init import main as init_main
import click

@click.group()
def cli():
    pass

cli.add_command(deploy_main)
cli.add_command(init_main)

if __name__ == '__main__':
    cli() 