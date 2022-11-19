"""
    En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

    Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

    Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""
import sqlite3

connDB = sqlite3.connect('databasestudents.db')

cursorDB = connDB.cursor()
cursorDB.execute("create table Alumnos(Id int, Nombre text not null, Apellido text not null)")
cursorDB.execute("insert into Alumnos values(1,'Debora', 'Rubilar')")
cursorDB.execute("insert into Alumnos values(2,'Luz', 'Rodriguez')")
cursorDB.execute("insert into Alumnos values(3,'Gastón', 'Rodriguez')")
cursorDB.execute("insert into Alumnos values(4,'Gastón', 'Romero')")
cursorDB.execute("insert into Alumnos values(5,'Gastón', 'Cordary')")
cursorDB.execute("insert into Alumnos values(6,'Exequiel', 'Maidana')")
cursorDB.execute("insert into Alumnos values(7,'Elba', 'Gomez')")
cursorDB.execute("insert into Alumnos values(8,'Ezequiel', 'Villalba')")
cursorDB.execute("insert into Alumnos values(8,'Iván', 'Maidana')")
cursorDB.execute("insert into Alumnos values(8,'Gabriela', 'Quizamás')")

connDB.commit()

cursorDB.execute("select * from Alumnos where Nombre = 'Iván'")
data = cursorDB.fetchall()
print(data)

connDB.close()