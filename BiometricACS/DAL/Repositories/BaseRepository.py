class BaseRepository:
    def create(self, item):
        item = self._type().update(item)
        self._db.sess.add(item)

    def update(self, item):
        self.get(item.id).update(item)

    def delete(self, item):
        self._db.sess.delete(item)
