'''
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

'''

dataStudents = {
    'Debora':7.66,
    'Juan':2.33,
    'Iván':9.5,
    'Exequiel':4,
    'Nora':3.66
}

class Students:
  names = None
  notes = None
  condition = None
  def __init__ (self, parameterNames, parameterNotes):
    self.names = parameterNames
    self.notes = parameterNotes
    if parameterNotes >= 4:
      self.condition = 'Appoved'
    else:
      self.condition = 'Disapproved'

for i in range(len(dataStudents)):
  selectStudent = list(dataStudents.keys())[i]
  studentNotes = dataStudents.get(selectStudent, 0)
  studenties = Students(selectStudent, studentNotes)
  print(f'The student {studenties.names} has a note of: {studenties.notes}/10.\nYour final course condition is: {studenties.condition}.')