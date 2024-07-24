import pytest
from click.testing import CliRunner
from cli_py.main import cli, generate_greeting

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_greet(runner, tmp_path):
    name_file = tmp_path / "name.txt"
    name_file.write_text("John")

    result = runner.invoke(cli, ['greet', str(name_file)])
    assert result.exit_code == 0
    assert "Hello, John!" in result.output

def test_cli_greet_spanish(runner, tmp_path):
    name_file = tmp_path / "name.txt"
    name_file.write_text("Maria")

    result = runner.invoke(cli, ['greet', '-l', 'es', str(name_file)])
    assert result.exit_code == 0
    assert "¡Hola, Maria!" in result.output

def test_cli_greet_bulgarian(runner, tmp_path):
    name_file = tmp_path / "name.txt"
    name_file.write_text("Ivan")

    result = runner.invoke(cli, ['greet', '--language', 'bg', str(name_file)])
    assert result.exit_code == 0
    assert "Здравей, Ivan!" in result.output

def test_cli_greet_file_not_found(runner):
    result = runner.invoke(cli, ['greet', 'nonexistent.txt'])
    assert result.exit_code == 2
    assert "'nonexistent.txt' does not exist." in result.output

def test_cli_greet_file_unreadable(runner, tmp_path):
    unreadable_file = tmp_path / "unreadable.txt"
    unreadable_file.write_text("Test")
    unreadable_file.chmod(0o000)  # Remove all permissions

    result = runner.invoke(cli, ['greet', str(unreadable_file)])
    assert result.exit_code == 2
    assert "unreadable.txt' is not readable." in result.output

    # Clean up: restore permissions so the file can be deleted
    unreadable_file.chmod(0o666)

def test_generate_greeting():
    assert generate_greeting("Alice", "en") == "Hello, Alice!"
    assert generate_greeting("Carlos", "es") == "¡Hola, Carlos!"
    assert generate_greeting("Ivana", "bg") == "Здравей, Ivana!"
    assert "Unsupported language" in generate_greeting("Test", "fr")