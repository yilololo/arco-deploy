from setuptools import setup, find_packages

setup(
    name='orca',
    version='0.1.0',
    description='A deployment tool for Arco services',
    author='yilo',
    author_email='lylhaha01@outlook.com',
    packages=find_packages(),
    package_data={
        'config': ['*.yml'],
    },
    include_package_data=True,
    install_requires=[
        'fabric>=2.5.0',
        'click>=7.0',
        'loguru>=0.5.0',
        'omegaconf>=2.1.0',
    ],
    entry_points={
        'console_scripts': [
            'orca=orca.main:cli'
        ]
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)