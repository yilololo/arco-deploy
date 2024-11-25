from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from fabric import task
from omegaconf import OmegaConf, DictConfig
import re

@dataclass
class DeployTask:
    path: str
    host: str
    port: int
    command: Dict[str, str]


class Config:
    def __init__(self, service_type: str, config_path: Optional[str] = None):
        if config_path is None:
            config_path = str(Path(__file__).parent / "global.yml")
        
        self.cfg = OmegaConf.load(config_path)
        self.service_type = service_type
        
    def get_tasks(self, env: str = "dev", commit: str = None) -> List[DeployTask]:
        """获取指定环境的服务器配置列表"""
        if env not in ["prod", "dev"]:
            raise ValueError(f"Invalid environment: {env}. Must be 'prod' or 'dev'")
        if commit is None:
            commit = "HEAD"
        service_cfg = self.cfg.get(self.service_type, {})
        instances = service_cfg.get(env, [])
        tasks = []
        for ins in instances:
            command = ins.get("command", {})
            for k, v in command.items():
                placeholders = parse_command_placeholders(v)
                if placeholders:
                    for placeholder in placeholders:
                        if placeholder == 'env':
                            v = v.replace(f'{{{placeholder}}}', env)
                            continue
                        if placeholder == 'commit':
                            v = v.replace(f'{{{placeholder}}}', commit)
                            continue
                        v = v.replace(f'{{{placeholder}}}', ins[placeholder])
                command[k] = v
            tasks.append(
                DeployTask(
                    path=ins['path'], 
                    host=ins['host'], 
                    port=ins['port'],
                    command=command
                )
            )
        return tasks

def parse_command_placeholders(command: str) -> list[str]:
    # Find all matches of {placeholder} pattern
    pattern = r'\{([^}]+)\}'
    matches = re.findall(pattern, command)
    return matches

if __name__ == "__main__":
    a = dict()
    a["my name"] = 1
    print(a)