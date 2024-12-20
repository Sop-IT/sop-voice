<h1 align="center">
    Deploy<br>
</h1>

## Overview

SOP-Phone plugin is deployed as a PyPi package.

---

## Deploy a new version

1. **Private Key**

In order to deploy a new version of the SOP-Phone plugin, you will need a `PyPi account` and SOP-Phone plugin `API key`.<br>
Export it in your shell and **never** push your these privates informations.<br>
According to [**documentation**](https://pypi.org/help/#apitoken), You now have to set your username as "`__token__`" to use an API token.

```bash
export phone_api="pypi-PRIVATE-API-KEY"
```

2. **Create a new version**

Edit the new plugin version in [**\_\_init\_\_**](/sop_phone/__init__.py)

```python
from netbox.plugins import PluginConfig


class SopPhoneConfig(PluginConfig):
    ...
    # others plugin informations
    ...
    version="0.4.3" # cannot be lower than the current
    ...
    # others plugin informations
    ...
    min_version="4.1.0" # change NetBox compatible minimum version if needed
    max_version="5.0" # and select a max_version if needed


config = SopPhoneConfig
```

Edit the [**setup.py**](/setup.py) version with the same version entered in the `__init__.py` file.

```python
from setuptools import setup, find_packages


setup(
    ...
    # others package informations
    ...
    version="0.4.3",
    ...
    # others package informations
    ...
    install_requires=[
        'phonenumbers',
        # plugin dependencies
    ],
    ...
    # others package informations
    ...
)
```

3. **Track all folders**

Ensure [**MANIFEST.in**](/MANIFEST.in) tracks all folders needed by the plugin. Here is the intended syntax:

```bash
recursive-include sop_phone/<folder_name>/ *
```

4. **Deploy the plugin on PyPi**

Create a Python `virtual environment` with the following packages:

```bash
# creates a virtual environment
python3 -m venv venv
# source your shell to it
source venv/bin/activate
# install PyPi dependencies
pip install twine setuptools
```

Run the [**deploy.sh**](/deploy.sh) script to create a new version of the SOP-Phone plugin.

```bash
./deploy.sh
# or if the shebang is incompatible
bash deploy.sh
```

---
