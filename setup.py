from setuptools import setup, find_packages

setup(
    name='arco-deploy',
    version='0.1',
    py_modules=['main'],
    packages=find_packages(),
    install_requires=[
        'fabric',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'arloy=main:ssh_and_execute',
        ],
    },
)