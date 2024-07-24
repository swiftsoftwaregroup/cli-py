# Usage

CLI-PY provides a simple interface for generating greetings. The main command is `greet`.

## Basic Usage

```bash
cli-py greet <filename> [-l <language>]

- <filename>: Path to a text file containing a name
- -l, --language: Optional. Language for the greeting (en, es, or bg). Default is English.
```

## Examples

1. Greet in English (default):

    ```bash
    cli-py greet name.txt
    ```
2. Greet in Spanish:

    ```bash
    cli-py greet name.txt -l es
    ```

3. Greet in Bulgarian:

    ```bash
    cli-py greet name.txt --language bg
    ```

## Error Handling

- If the specified file does not exist, CLI-PY will display an error message.
- If the file is not readable, an appropriate error message will be shown.
