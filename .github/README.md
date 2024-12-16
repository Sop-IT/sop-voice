<h1 align="center">
    NetBox - SOP-Phone plugin<br>
</h1>
<p align="center">
    <a href="https://github.com/netbox-community/netbox">NetBox</a> plugin to manage phone informations for each site.
</p>

---

## 🚀 Features

- [**Counting**](/docs/features/counting.md)
- [**Format**](/docs/features/format.md)
- [**Search**](/docs/features/search.md)

---

## 📦 Installation

### Prerequisites

Ensure you have the following requirements:

- NetBox 4.1.0+
- Python 3.x
- `phonenumbers` library

### Installation Steps

1. **Add Requirements**

   ```bash
   # add phonenumbers library
   echo "phonenumbers" >> local_requirements.txt

   # add SOP-Phone plugin
   echo "sop-phone" >> local_requirements.txt
   ```

2. **Configure NetBox**
   Edit `netbox/netbox/configuration.py` to include the plugin:

   ```python
   PLUGINS = [
       # ... other plugins
       'sop-phone',
   ]
   ```

3. **Upgrade NetBox**
   ```bash
   sudo ./upgrade.sh
   ```

## 📋 Models

The SOP-Phone plugin provides four core models:

- [**Phone Maintainer**](/docs/models/phone-maintainer.md)
- [**Phone Info**](/docs/models/phone-info.md)
- [**Phone Delivery**](/docs/models/phone-delivery.md)
- [**Phone DIDs**](/docs/models/phone-did.md)

---

## 🛠️ Development

- [**Deploy**](/docs/development/deploy.md)
- [**Unit-Tests**](/docs/development/unit-test.md)
