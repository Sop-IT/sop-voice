<h1 align="center">
    Format<br>
</h1>

## Overview

The plugin ensures consistent and user-friendly display of phone numbers. While DIDs are stored in the database using the standardized **E.164 format**, the `backend` automatically determines the country of origin and formats the number into a readable **international format** for the `frontend`.

---

## Input and Output example

### Database Input (E.164 Format):

```plaintext
33344556778
33344556880
```

### Frontend Display:

```plaintext
🇫🇷   +33 3 44 55 67 78    >>    🇫🇷   +33 3 44 55 68 80
```

> [!NOTE]
> if your browser doesn't support emoji display, install an extension that does

---
