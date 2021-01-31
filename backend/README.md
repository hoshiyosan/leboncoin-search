# Apartment

> Goal: Allow one to browse apartments that meet given search criteria !


## API endpoints

/search?sources=leboncoin&ouestfrance&bla

/results

## Tips and tricks

Each item is given a unique id computed based on some metadata.
Items are stored in a normalized format in database.
Items are given a timestamp to be able to filter most recent one's

## Database structure

Apartment:
|field|type|
|title|str|
|rooms|dict(kitchen=1, bathroom=1, room=3, total=5)|

## Require a configuration file per-language ? No language support ! Fuck!

## Important notions

blacklist: remove an apartment from possible choices, but keep its track in database to avoid finding it again.
