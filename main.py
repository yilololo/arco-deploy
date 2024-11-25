from os import path
import time
from fabric import Connection
from config import Config
import click
from loguru import logger
# 创建连接并执行命令
@click.command(name="arco-deploy")
@click.option('--service', '-s', 
              type=click.Choice(['backend', 'frontend', 'discord']), 
              required=True,
              help='Service to deploy (backend/frontend/discord)')
@click.option('--env', '-e',
              type=click.Choice(['dev', 'prod']),
              default='dev',
              help='Environment to deploy to (dev/prod)')
@click.option('--identity_file_path', '-i',
              type=click.Path(exists=True),
              help='Path to the key file')
@click.option('--commit', '-c',
              help='Commit version')
def ssh_and_execute(service: str, env: str, identity_file_path: str, commit: str):
    cfg = Config(service_type=service)
    tasks = cfg.get_tasks(env)
    for task in tasks:
        conn = Connection(
            task.host, 
            user="root", 
            port=task.port, 
            connect_kwargs={'key_filename': identity_file_path}
        )
        for cmd_type, cmd in task.command.items():
            try:
                logger.info(f"Executing {cmd_type}")
                conn.sudo(cmd, user='arco', hide=True)
                time.sleep(0.5)
            except Exception as cmd_error:
                logger.error(f"Error executing {cmd_type} command: {cmd}. Error: {cmd_error}")

if __name__ == "__main__":
    ssh_and_execute()