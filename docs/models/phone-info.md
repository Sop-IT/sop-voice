<h1 align="center">
    Phone Information<br>
</h1>

## Overview

The `PhoneInfo` model provides a one-to-one association between a `Site` and its corresponding [PhoneMaintainer](./phone-maintainer.md). This ensures that each site has accurate information about its maintainer.

---

## Attributes

### 1. **Site**

- **Field:** `site`
- **Type:** `OneToOneField` to NetBox `Site` model
- **Details:**
  - Represents the site associated with the phone maintainer/
  - Mandatory field.

### 1. **Maintainer**

- **Field:** `maintainer`
- **Type:** `ForeignKey` to `PhoneMaintainer`
- **Details:**
  - Represents the maintainer for the site.
  - Can be `null`.

---

## Constraints

### 1. **Unique Site**

- Ensures that each site has only one associated `PhoneInfo` instance.

---
