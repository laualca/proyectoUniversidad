from django.db import models

# Create your models here.
#MODELO creacion de la clase Carrera de la tabla carrera
class Carrera(models.Model):
    codigoCarrera = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.PositiveSmallIntegerField(default=8)
    
    def __str__(self):
        txt = "{0} (Duracion: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

#MODELO creacion de la clase Estudiante de la tabla estudiante  
class Estudiante(models.Model):
    codigoEstudiante = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=15)
    nombres = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    vigencia = models.BooleanField(default=True)
    #relacion de la tabla estudiante con la tabla carrera llave foranea
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    
    def nombreCompleto(self):
        txt = "{0} {1}, {2}" 
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "RETIRADO"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)
    
#MODELO creacion de la clase Curso de la tabla curso
class Curso(models.Model):
    codigoCurso = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    creditos = models.PositiveSmallIntegerField(default=5)
    docente = models.CharField(max_length=100)
    
    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigoCurso, self.docente)
    
#MODELO creacion de la clase Matricula de la tabla matricula
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
    #relacion de la tabla matricula con la tabla estudiante llave foranea
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == 'F':
            letraSexo = "a"
        else:
            letraSexo = "o"
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.curso, fecMat)