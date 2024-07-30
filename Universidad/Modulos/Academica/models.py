from django.db import models

# Create your models here.
# creacion de la clase Carrera de la tabla carrera
class Carrera(models.Model):
    codigoCarrera = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.PositiveSmallIntegerField(default=8)

#creacion de la clase Estudiante de la tabla estudiante    
class Estudiante(models.Model):
    codigoEstudiante = models.CharField(max_length=15, primary_key=True)
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