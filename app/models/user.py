from peewee import CharField, DateTimeField, IntegerField

from app.models.base_model import BaseModel


class User(BaseModel):
    class Meta:
        table_name = 't_user'

    user_code = CharField(unique=True)
    user_no = IntegerField(unique=True)
    username = CharField()
    nickname = CharField()
    password = CharField()
    salt = CharField()
    email = CharField()
    phone = CharField(index=True)
    open_id = CharField()
    client_ip = CharField()
    login_at = DateTimeField()
    login_token = CharField()
    avatar = CharField()
    status = IntegerField() # 0: Unactivated, 1: Active, 2: Frozen, 3: Deleted

    def is_enabled(self):
        return self.status == 1
