# cli-py

Template for Command Line Interface (CLI) tool in Python

## Development

### Setup for macOS

#### Xcode Command Line Tools

Install Command Line Tools (CLT) for Xcode:

```bash
xcode-select --install
```

#### Homebrew

Install [Homebrew](https://brew.sh/):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### pyenv

Install Python version manager [pyenv](https://github.com/pyenv/pyenv)

```bash
brew install pyenv
```

### Work on macOS

Configure project:

```bash
source configure.sh
```

Open the project in Visual Studio Code:

```bash
code .
```

###  Run

```bash
echo "John" > name.txt

cli-py greet name.txt
cli-py greet --language es name.txt
cli-py greet -l bg name.txt
```

### How to create a new project

```bash
# init the project
poetry init \
  --no-interaction \
  --name "cli-py" \
  --description "CLI tool for greeting users in different languages" \
  --license "Apache-2.0" \
  --python "^3.12"
  
# add `click` package
poetry add click
```

Create the following project structure:

```sh
cli-py/
├── cli_py/
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── README.md
└── LICENSE
```

