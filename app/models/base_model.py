from ast import Delete
import datetime

from peewee import IntegerField, DateTimeField, Model, SQL, CharField, BooleanField, AutoField

from app.providers.database import db


class BaseModel(Model):
    id = AutoField()
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField()
    deleted_at = DateTimeField()
    created_by = CharField("777")
    updated_by = CharField()
    version = IntegerField(default=1)

    class Meta:
        database = db


class BaseModelWithSoftDelete(BaseModel):
    deleted_at = DateTimeField(null=True)

    @classmethod
    def undelete(cls):
        return cls.select().where(SQL("deleted_at is NULL"))
