pre-commit-hooks
================

Some hooks for pre-commit.

See also original repo: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/mircodariol/pre-commit-hooks
    rev: v1.0.0  # Use the ref you want to point at
    hooks:
    -   id: disable-periodic-background-checks
    -   id: erase-data-loader-keys
    -   id: erase-vendor-code
    # -   id: ...
```

### Hooks available

#### `disable-periodic-background-checks`
Disable sentinel periodic background checks to avoid the error sentinel hasp not found when a tablet/PC is resumed from the hybernation.

#### `erase-data-loader-keys`
Remove all data loader keys from envelope project files.

#### `erase-vendor-code`
Remove all vendor code related secret from envelope project files.

### Usage
After configuring your `.pre-commit-config.yaml`, run the following command to install the pre-commit hooks:

```script
pre-commit install
```

Now, the hooks will run automatically on every commit. You can also run the hooks manually on all files:

```script
pre-commit run --all-files
```

### Development
To develop and test the hooks locally, you can use the following commands:

```script
pip install -r requirements-dev.txt
```

#### Running Tests
To run the tests, you need to have pytest installed. You can install it using pip:

```script
pip install pytest
```

Then, run the tests using the following command:
```script
pytest
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request.

### Contact
For any questions or suggestions, please contact Mirco Dariol at [dariol.mirco@gmail.com](mailto:dariol.mirco@gmail.com).
