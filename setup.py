from setuptools import setup, find_packages

setup(
    name='arco-deploy',
    version='0.1',
    py_modules=['arco_deploy'],
    packages=find_packages(),
    package_data={
        '': ['*.yml']
    },
    include_package_data=True,
    install_requires=[
        'fabric',
        'click',
        'loguru',
        'omegaconf'
    ],
    entry_points={
        'console_scripts': [
            'arco-deploy=arco_deploy:ssh_and_execute',
        ],
    },
)