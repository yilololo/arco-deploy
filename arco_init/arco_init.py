import os
from fabric import Connection
import click
import json
from loguru import logger

CONFIG_DIR = os.path.expanduser("~/.deploy_arco")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config(config_data):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_data, f)


@click.command(name="init")
@click.option('--identity_file_path', '-i',
              type=click.Path(exists=True),
              required=True,
              help='Path to the key file')
def main(identity_file_path: str):
    custom_config = load_config()
    # 如果提供了新的 identity_file_path，就更新配置
    if identity_file_path:
        custom_config['identity_file_path'] = identity_file_path
        save_config(custom_config)
    # 如果没有提供，就用保存的配置
    elif 'identify_file_path' in custom_config:
        identify_file_path = custom_config['identify_file_path']
    else:
        raise click.UsageError("Please provide --identity_file_path (-i) for the first time use")

if __name__ == "__main__":
    main()