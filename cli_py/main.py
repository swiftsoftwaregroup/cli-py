import click
import sys

def read_name_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError:
        click.echo(f"Error: Unable to read file '{file_path}'", err=True)
        sys.exit(1)

def generate_greeting(name, language):
    greetings = {
        'en': f"Hello, {name}!",
        'es': f"¡Hola, {name}!",
        'bg': f"Здравей, {name}!"
    }
    return greetings.get(language, f"Unsupported language: {language}")

@click.group()
def cli():
    """CLI tool for greeting users in different languages"""
    pass

@cli.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-l', '--language', type=click.Choice(['en', 'es', 'bg']), default='en',
              help="Language for the greeting (en: English, es: Spanish, bg: Bulgarian)")
def greet(file, language):
    """Greet a user based on a name in a file"""
    name = read_name_from_file(file)
    greeting = generate_greeting(name, language)
    click.echo(greeting)

if __name__ == "__main__":
    cli()
