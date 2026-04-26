from setuptools import setup, find_packages

setup(
    name="devai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer",
        "rich",
        "google-genai",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "devai=devai.main:app"
        ]
    }
)
