<h1 align="center">
    Phone Maintainer<br>
</h1>

## Overview

The `PhoneMaintainer` model represents organizations responsible for maintaining phone services. It includes attributes such as name, status, address details and geolocation information. It ensures accurate representation and management of maintainers across different sites.

---

## Attributes

### 1. **Name**

- **Field:** `name`
- **Type:** `CharField`
- **Details:**
  - Represents the unique name of the maintainer.
  - Cannot be `null`.

### 2. **Slug**

- **Field:** `slug`
- **Type:** `SlugField`
- **Details:**
  - Unique identifier for the maintainer.
  - Used for URL-friendly representation.

### 3. **Status**

- **Field:** `status`
- **Type** `CharField` with choices.
- **Details:**
  - Represents the current status of the maintainer.
    - Active
    - Retired
    - Unknown

### 4. **Physical Address**

- **Field:** `physical_address`
- **Type:** `CharField`
- **Details:**
  - Represents the physical location of the maintainer.
  - Address must be multi-line and each line must end with a space.
  - Optional field.

### 5. **Shipping Address**

- **Field:** `shipping_address`
- **Type:** `CharField`
- **Details:**
  - Represents the shipping if different from the physical address.
  - Address must be multi-line and each line must end with a space.
  - Optional field.

### 6. **Latitude**

- **Field:** `latitude`
- **Type:** `DecimalField`
- **Details:**
  - GPS latitude in decimal format (e.g., 48.123456).
  - Optional field.

### 7. **Longitude**

- **Field:** `longitude`
- **Type:** `DecimalField`
- **Details:**
  - GPS longitude in decimal format (e.g., 7.123456).
  - Optional field.

### 8. **Time Zone**

- **Field:** `time_zone`
- **Type:** `TimeZoneField`
- **Details:**
  - Indicates the time zone of the maintainer
  - Optional field

---

## Constraints

### 1. **Unique Name**

- Ensures that the `name` field is unique across all maintainers.

### 2. **Unique Slug**

- Ensures that the `slug` field is unique across all maintainers.

---
