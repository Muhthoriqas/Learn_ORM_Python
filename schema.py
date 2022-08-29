from peewee import SqliteDatabase, Model, TextField, DateField, IntegerField

db = SqliteDatabase("movies.db")

class BaseTable(Model):
    class Meta:
        database = db

class Movie(BaseTable):
    title = TextField(null=False, index=True)
    release_date = TextField(null=False, index=True)
    rating= IntegerField(null=True)

