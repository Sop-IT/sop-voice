<h1 align="center">
    Phone DID<br>
</h1>

## Overview

The `PhoneDID` model represents a range of phone numbers (DIDs) associated with a site or delivery. It ensures integrity and consistency through various constraints and validations.

---

## Attributes

### 1. **Site**

- **Field:** `site`
- **Type:** `ForeignKey` to NetBox `Site` model.
- **Details:**
  - Indicates the site where the DID range belongs.
  - Cannot be `null`.
  - Deletion of the related `Site` cascade.

### 2. **Delivery**

- **Field:** `delivery`
- **Type:** `ForeignKey` to [PhoneDelivery](./phone-delivery.md)
- **Details:**
  - Represents the delivery process associated with the DID range.
  - Can be `null`.
  - Deletion of the related `PhoneDelivery` sets this field to `null`.

### 3. **Start Number**

- **Field:** `start`
- **Type:** `PositiveBigInteger`
- **Details:**
  - Defines the starting number of the DID range.
  - Only numbers in `E.164 format`.
  - Cannot be `null`.

### 4. **End Number**

- **Field:** `end`
- **Type:** `PositiveBigInteger`
- **Details:**
  - Define the ending number of the DID range.
  - Only numbers in `E.164 format`.
  - Can be `null`.
  - Defaults to the `start` value if left empty or `null`.

---

## Constraints

### 1. **Unique Start and End Numbers**

- Ensures that the `start` and `end numbers are unique across the database.

### 2. **Range Validation**

- Verifies that the `end` number is greater than or equal to the `start` number.
- `start` must have the same amount of digits as `end`.

### 3. **Range Overlaps**

- Prevents overlapping DID ranges within others DIDs or across deliveries.

---
