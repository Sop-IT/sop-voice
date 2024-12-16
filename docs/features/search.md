<h1 align="center">
    Search<br>
</h1>

## Global search

SOP-voice plugin is compatible with NetBox global search engine. It allows you to search for objects in the exact format as stored in the database, while also supporting indexing for quick lookups.

---

## Filters

Each model in the SOP-phone plugin provides its own set of filters on the `list` view page. The filters enable you to retrieve specific objects based on various criteria, tailored to the model's attributes.

### Shared Location Filters

All models in the plugin share a common set of location-based filters, allowing you to narrow down objects by geographical or organizational context. The supported filters include:

- **Region:** Use the query parameter `?region_id=` to filter objects by their associated Region ID.
- **Site Group:** Use the query parameter `?group_id=` to filter objects by their associated Site Group ID.
- **Site:** Use the query parameters `?site_id=` to filter objects associated with specific Site ID or Name with `?site_name=`.

---

## Partial number

DID model has an additional feature: the **partial number** filter. This search algorithm is designed to quickly return all **DIDs ranges** that match a specific **numeric pattern**.<br>
This tool enables efficient `pattern matching` across large datasets of number ranges, even for numbers that are not explicitly stored.

---

### Key features

- **Pattern matching in number ranges**: Quickly find ranges that include numbers matching a given pattern.
- **Virtual range emulation**: The algorithm effectively emulates the data within the number ranges without needing to store every individual number.
- **High performance**: Optimized to perform rapid searches, even o, extensive datasets.

---

### How it works

The algorithm performs a search across number ranges to find matches based on a specified pattern. For example, given then range:

```plaintext
+33344556778 to +33344556880
```

If the search pattern is `6789`, the filter will return the range because `` falls between +3334455**6778** to +3334455**6880**
