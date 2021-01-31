import json
import redis


class Database:
    def __init__(self, host="localhost", port=6379, db=2):
        self.connexion = redis.Redis(host=host, port=port, db=db)

    def insert(self, uid, value):
        self.connexion.set(uid, json.dumps(value))

    def update(self, uid, value):
        print("inserted uid", uid)
        self.connexion.delete(uid)
        self.connexion.set(uid, json.dumps(value))

    def find_by_uid(self, uid):
        raw_result = self.connexion.get(uid)
        if raw_result is None:
            return None
        return json.loads(raw_result)

    def search(self, prefix):
        keys = tuple(self.connexion.scan_iter(f"{prefix}:*"))
        return [self.find_by_uid(key) for key in keys]


class AnounceDatabase(Database):
    def insert(self, anounce):
        anounce_uid = f"anounce:{anounce['uid']}"
        existing = super().find_by_uid(anounce_uid)
        if existing is None:
            super().insert(anounce_uid, anounce)

    def search(self, prefix=None):
        prefix = "anounce" if prefix is None else f"anounce:{prefix}"
        return super().search(prefix)

    def set_decision(self, anounce_uid, decision):
        obj_uid = f"anounce:{anounce_uid}"
        anounce = self.find_by_uid(obj_uid)
        anounce["decision"] = decision
        print(anounce)
        self.update(obj_uid, anounce)
