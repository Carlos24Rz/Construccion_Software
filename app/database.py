from peewee import *
from datetime import datetime
from config import db
from config import user
from config import password

database = MySQLDatabase(
    db,
    user=user,
    password=password,
    host='localhost',
    port=3306,
    charset='utf8mb4'
)

# http://docs.peewee-orm.com/en/latest/peewee/models.html?highlight=table%20generation#field-initialization-arguments
class Pregunta(Model):
    # id = AutoField(primary_key=True)
    padre_id = IntegerField()
    nombre = CharField(max_length=80)
    emoji = CharField(max_length=3)
    texto = CharField(max_length=800)
    visitas = IntegerField(default=0)
    is_final = BooleanField(default=False)

    # def __str__(self):
    #     return self.nombre

    class Meta:
        database = database
        table_name = 'pregunta'

class Persona(Model):
    # id = AutoField(primary_key=True)
    nombre = CharField(max_length=60)
    correo = CharField(max_length=50)
    descripcion = CharField(max_length=600)
    fecha = DateTimeField(default=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    def __str__(self):
        return self.nombre

    class Meta:
        database = database
        table_name = 'persona'

class Calificacion(Model):
    id = AutoField(primary_key=True)
    calificacion = IntegerField()
    fecha = DateTimeField(default=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    def __str__(self):
        return self.calificacion

    class Meta:
        database = database
        table_name = 'calificacion'
