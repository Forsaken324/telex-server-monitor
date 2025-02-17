from setuptools import setup, find_packages

setup(
    name="telex_server_health",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "psutil",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "start-health-monitor=telex_health_monitor.main:run_server"
        ]
    },
)
