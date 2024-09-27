# API

Sop-Voice provides an API to manage voice informations at /api/plugins/sop-voice/

## Filter-search

You can filter the results using the following parameters:

| Prefix | Description | Example |
| ------- | ----------- | ---- |
| ?q | search in the name of the object | ?q=pbx |
| ?site_id | search in the site id | ?site_id=1 |
| ?site_name | search in the site name | ?site_name=SHQ |
| ?maintainer_id | search object related to the maintainer id | ?maintainer_id=1 |
| ?maintainer_name | search object related to the maintainer name | ?maintainer_name=Quonex |
| ?partial_number | specific to Voice SDA, search partial match in all the range | ?partial_number=4307 |
