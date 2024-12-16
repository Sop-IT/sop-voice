<h1 align="center">
    Counting<br>
</h1>

## Overview

This feature provides detailed counting capabilities for phone number-related objects. It tracks the number of phone numbers (DIDs) within each object and offers aggregated metrics.

---

## Counting details

### 1. **Phone DID Counts**

- **Description:** Counts the number of phone numbers (DIDs) present within a single object.
- **Use Case:** Quickly determine the size of a DID range or batch.

  **Example:**

  - Input: a DID range from `33344556778` to `33344556880`
  - Output: `103 numbers`.

### 2. **Phone Delivery Counts**

- **Description:** Tracks the total number of delivered phone numbers (DIDs) and the number of phone DID objects delivered.
- **Use Case:** Monitor the distribution of DIDs in a delivery process.

  **Example:**

  - Input: `3` Phone DID objects with a total of `300` DIDs.
  - Output: `Delivers 3 ranges (300 numbers)`

### 3. **Phone Maintainer Counts**

- **Description:** Monitors the number of DIDs currently maintained and track the associated `Phone DID` objects and their `Site`.
- **Use Case**: Analyzed ongoing operations and ensure accurate reporting of active DIDs and their site.

  **Example:**

  - Input: `470`Phone DID with a total of `4724` numbers for `129` sites.
  - Output:
    - Phone numbers maintained: 4724 numbers
    - DIDs: 470
    - Sites: 129

---
