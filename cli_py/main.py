"""
This module contains the main functions and CLI commands for the CLI-PY tool.
"""

import click

def read_name_from_file(file_path: str) -> str:
    """
    Read a name from the specified file.

    Args:
        file_path (str): The path to the file containing the name.

    Returns:
        str: The name read from the file, stripped of leading/trailing whitespace.

    Raises:
        click.FileError: If the file cannot be read.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def generate_greeting(name: str, language: str) -> str:
    """
    Generate a greeting for the given name in the specified language.

    Args:
        name (str): The name to include in the greeting.
        language (str): The language code for the greeting ('en', 'es', or 'bg').

    Returns:
        str: The generated greeting.
    """
    greetings = {
        'en': f"Hello, {name}!",
        'es': f"¡Hola, {name}!",
        'bg': f"Здравей, {name}!"
    }
    return greetings.get(language, f"Unsupported language: {language}")

@click.group()
def cli():
    """CLI tool for greeting users in different languages."""

@cli.command()
@click.argument('file', type=click.Path(exists=True, readable=True))
@click.option('-l', '--language', type=click.Choice(['en', 'es', 'bg']), default='en',
              help="Language for the greeting (en: English, es: Spanish, bg: Bulgarian)")
def greet(file: str, language: str):
    """
    Greet a user based on a name in a file.

    Args:
        file (str): Path to the file containing the name.
        language (str): Language code for the greeting.
    """
    name = read_name_from_file(file)
    greeting = generate_greeting(name, language)
    click.echo(greeting)

if __name__ == "__main__":
    cli()
