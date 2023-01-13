from project.core import db


def commit(obj):
    """
    Function for convenient commit
    """
    db.session.add(obj)
    db.session.commit()
    db.session.refresh(obj)
    return obj


class Model(object):
    @classmethod
    def create(cls, **kwargs):
        """
        Create new record

        cls: class
        kwargs: dict with object parameters
        """
        obj = cls(**kwargs)
        return commit(obj)

    @classmethod
    def update(cls, row_id, **kwargs):
        """
        Update record by id

        cls: class
        row_id: record id
        kwargs: dict with object parameters
        """
        cls.query.filter_by(id=row_id).update(kwargs)
        db.session.commit()
        return cls.query.filter_by(id=row_id).first()

    @classmethod
    def add_person_topic_xref(cls, row_id, rel_obj):
        """
        Add person's topic

        cls: class
        row_id: record id
        rel_obj: related object
        """
        obj = cls.query.filter_by(id=row_id).first()
        obj.person_topic_xref.append(rel_obj)
        return commit(obj)
