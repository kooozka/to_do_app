from setuptools import setup, find_packages

setup(
    name='to_do_app',
    version='1.0.1',
    description='Simple app created in order to manage users tasks',
    author='Jakub Kozanecki',
    packages=find_packages(),
    install_requires=[
        "datetime"
    ],
    entry_points={
        'console_scripts': [
            'to_do_app = main:main'
        ]
    }
)

