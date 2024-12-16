<h1 align="center">
    Phone DID<br>
</h1>

## Overview

The `PhoneDelivery` model defines the structure for managing phone delivery services associated with sites and providers. It includes key attributes such as NDI (Main Billing Number), DTO (Data Transfer Object), status and channel count. The model enforces validations and constraints to ensure data integrity.

---

## Attributes

### 1. **Delivery Method**

- **Field:** `delivery`
- **Type:** `CharField`
- **Details:**
  - Represents the delivery method (e.g., type of phone service).
  - Can be `null`.

### 2. **Provider**

- **Field:** `provider`
- **Type:** `ForeignKey` to NetBox `Provider` model.
- **Details:**
  - Refers to the telecom provider associated with the delivery.
  - Can be `null`.

### 3. **Site**

- **Field:** `site`
- **Type:** `ForeignKey` to NetBox `Site` model.
- **Details:**
  - Indicates the site associated with the delivery.
  - Cannot be `null`.

### 4. **Channel Count**

- **Field:** `channel_count`
- **Type:** `PositiveBigInteger`
- **Details:**
  - Represents the number of channels available in the delivery.
  - Can be `null`.

### 5. **Status**

- **Field:** `status`
- **Type:** `CharField` with choices
- **Details:**
  - Represents the current status of the delivery.
    - Active
    - Planned
    - Staging
    - Retired
    - Unknown

### 6. **NDI (Main Billing Number)**

- **Field:** `ndi`
- **Type:** `PositiveBigInteger`
- **Details:**
  - Defines the main billing number for the delivery.
  - Only numbers in `E.164 format`.
  - Unique across all deliveries.
  - Can be `null`

### 7. **DTO (Data Transfer Object)**

- **Field:** `dto`
- **Type:** `PositiveBigInteger`
- **Details:**
  - Defines the data transfer object number for the delivery.
  - Only numbers in `E.164 format`.
  - Can be `null`

### 8. **Description**

- **Field:** `description`
- **Type:** `CharField`
- **Details:**
  - Optional text field for additional information about the delivery.

### 9. **Comments**

- **Field:** `comments`
- **Type:** `TextField`
- **Details:**
  - Free-text field for storing notes or comments about the delivery.

---

## Constraints

### 1. **Unique NDI**

- Ensures the `NDI` field is unique across all deliveries.

### 2. **Unique Delivery Method per Site**

- Enforces that a delivery method is unique within a site.

### 3. **Consistency**

- Ensure the `NDI` and `DTO` are in E.164 format and do not overlap existing DIDs or deliveries.

---
