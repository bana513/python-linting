# Linting: **flake8**
- Style Guide Enforcement
- Check code syntax
- Provide instructions on how to clean it
- Prevent things like syntax errors, typos, bad formatting, incorrect styling, etc
- If you working in the team, it saves time for people who are reviewing your code (no need to distrust for typos and formatting issues).
[Read more](https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2)

1.  
    ```sh
    pip install flake8
    ```

2. 
    Install VSCode plugin: *cornflakes-linter*

3. Settings.json:
    ```json
    {
        "cornflakes.linter.executablePath": "path/to/venvs/myvenv/bin/flake8",
        "cornflakes.linter.run": "onType"
    }
    ```

# Import formatting: **isort**
- Sort imports alphabetically
- Automatically separated into sections and by type.

1. 
    ```sh
    pip install isort
    ```

2. 
    ```sh
    isort mypythonfile.py mypythonfile2.py
    
    isort .

    isort **/*.py

    isort mypythonfile.py --diff

    #  only applying changes if they don't introduce syntax errors
    isort --atomic .
    ```

# Code formatter: **black**
- Can be forced to check with GitHub Actions on push or pull requests
1. 
    ```sh
    pip install black
    ```
2. 
    - VSCode: Right click + Format Document  
    - 
        ```sh
        black my_file.py
        black .
        ```
        Sometimes needs to refresh project in VSCode
3. [**isort** compatibility](https://pycqa.github.io/isort/docs/configuration/black_compatibility/)  
    *pyproject.toml*:
    ```toml
        [tool.isort]
        profile = "black"
        multi_line_output = 3
    ```

# Static type checker: **mypy**
1. 
    ```sh
    pip install mypy
    ```
2.     
    ```sh
    mypy .
    ```

