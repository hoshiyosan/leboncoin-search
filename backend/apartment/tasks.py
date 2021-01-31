from celery import Celery, group
from datetime import datetime
from .leboncoin import Leboncoin
from . import schemas
from .addons import anounces_db

celery = Celery(
    __name__,
    backend="redis://default@localhost:6379/",
    broker="redis://default@localhost:6379/",
)


@celery.task
def search_leboncoin(min_rooms=1, max_rooms=10, min_price=0, max_price=1000000):
    leboncoin = Leboncoin()
    anounces = leboncoin.search(
        min_rooms=min_rooms,
        max_rooms=max_rooms,
        min_price=min_price,
        max_price=max_price,
    )
    for anounce in anounces:
        anounce["decision"] = "inbox"
        anounces_db.insert(anounce)
    return "Leboncoin anounces updated successfully."


@celery.task
def search(**kwargs):
    search_filters = schemas.SearchFilters().load(kwargs)
    tasks_group = group([search_leboncoin.signature(**search_filters)])
    result = tasks_group.apply_async()

    if result.successful():
        return result.get()
    else:
        return {"error": "an error occured while processing group of tasks"}
