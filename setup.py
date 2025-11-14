# setup.py

from setuptools import setup, find_packages

setup(
    name="comrade-web-ip",
    version="0.1",
    packages=find_packages(),  # will include comrade_web_ip
    install_requires=[
        "pyfiglet",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "comrade_web_ip=comrade_web_ip.cli:main",
        ],
    },
)
