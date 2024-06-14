import os
from DTO.Empleados import Empleados
from DTO.Departamento import Departamento
from DTO.Proyectos import Proyectos
from DTO.Roles import Roles
from DTO.Tiempo import Tiempo
from DTO.Usuario import Usuario
from DAO import Conexion    
from DAO import EmpleadosDAO
from DAO import DepartamentoDAO
from DAO import ProyectosDAO
from DAO import RolesDAO
from DAO import TiempoDAO
from DAO import UsuarioDAO
from DAO import EmpleadoDepartamentoDAO
from DAO import EmpleadoProyectoDAO
from datetime import datetime


import pymysql

class Conexion:
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.contraseña = ''
        self.base_de_datos = 'empresa'

    def conectar(self):
        try:
            self.conexion = pymysql.connect(
                host=self.host,
                user=self.usuario,
                password=self.contraseña,
                database=self.base_de_datos
            )
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a la base de datos.")
            return True
        except pymysql.Error as e:
            print(f"Error de conexión: {e}")
            return False

    def desconectar(self):
        try:
            if self.conexion:
                self.conexion.close()
                self.cursor.close()
                print("Conexión cerrada.")
        except pymysql.Error as e:
            print(f"Error al desconectar: {e}")







def menuprincipalgerente():
    import os
    os.system('cls')
    print("M E N U    P R I N C I P A L")
    print("---------------------------")
    print("1- Menu Departamento")
    print("2- Asignar Empleado a Departamento")
    print("0- Salir")
    print("---------------------------")
    opcion = int(input("Ingrese Opcion: "))
    while opcion >= 0:
        match opcion:
            case 1:
                try:
                    menudepartamentogerente()
                    break  
                except Exception as e:
                        print("Error:", e)
                        
            case 2:
                try:
                    menuempleadodepartamentogerente()
                    break  
                except Exception as e:
                        print("Error:", e)
            case 0:
                break



def menuprincipal():
    import os
    os.system('cls')
    print("M E N U    P R I N C I P A L")
    print("---------------------------")
    print("1- Menu Empleados")
    print("2- Menu Proyectos")
    print("3- Menu Roles")
    print("4- Menu Tiempo")
    print("5- Menu Departamento")
    print("6- Asignar Empleado a Departamento")
    print("7- Asignar Empleado a Proyecto")
    print("8- Generar Informes")
    print("0- Salir")
    print("---------------------------")
    opcion = int(input("Ingrese Opcion: "))
    while opcion >= 0:
        match opcion:
            case 1:
                try:
                    menuempleado()
                    break  
                except Exception as e:
                        print("Error:", e)
                        
            case 2:
                try:
                    menuproyecto()
                    break  
                except Exception as e:
                        print("Error:", e)

            case 3:
                try:
                    menuroles()    
                    break  
                except Exception as e:
                    print("Error:", e)
            case 4:
                try:
                    menutiempo()
                    break
                except Exception as e:
                    print("Error: ",e)
            case 5:
                try:
                    menudepartamento()
                    break
                except Exception as e:
                    print("Error: ",e)
            case 6:
                try:
                    menuaempleadodepartamento()
                    break
                except Exception as e:
                    print("Error: ",e)
            case 7:
                try:
                    menuempleadoproyecto()
                    break
                except Exception as e:
                    print("Error: ",e)
            case 8:
                try:
                    generarinforme()
                    break
                except Exception as e:
                    print("Error ",e)
            case 0:
                break

def menuempleado():
    os.system('cls')
    print("M E N U    E M P L E A D O S")
    print("---------------------------")
    print("1- Ingresar Empleado")
    print("2- Actualizar Empleado")
    print("3- Buscar Empleado por Id")
    print("4- Eliminar Empleado")
    print("0- Salir")
    print("---------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
        match op:
            case 1:
                try:
                    nombre=input("Ingrese el Nombre:    ")
                    direccion=input("Ingrese la Direccion:     ")
                    fono=input("Ingrese su fono:     ")
                    correo=input("Ingrese su correo:   ")
                    fechacontrato=input("Ingrese la Fecha Contrato:  ")
                    try:
                        fechacontrato = datetime.strptime(fechacontrato, "%Y-%m-%d")
                    except ValueError:
                        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
                    salario=input("Ingrese el salario:    ")
                    empleado=Empleados(nombre,direccion,fono,correo,fechacontrato,salario)
                    EmpleadosDAO.add(empleado)
                    menuempleado()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 2:
                try:
                    id=int(input("Ingrese la Id del Empleado:   "))
                    nombre=input("Ingrese el Nombre:    ")
                    direccion=input("Ingrese la Direccion:     ")
                    fono=input("Ingrese su fono:     ")
                    correo=input("Ingrese su correo:   ")
                    fechacontrato=input("Ingrese la Fecha Contrato:  ")
                    try:
                        fechacontrato = datetime.strptime(fechacontrato, "%Y-%m-%d")
                    except ValueError:
                        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD") 
                    salario=input("Ingrese el salario:    ")
                    empleado=Empleados(nombre,direccion,fono,correo,fechacontrato,salario)
                    empleado.setIdEmpleado(id)
                    EmpleadosDAO.update(empleado)
                    menuempleado()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 3:
                try:
                    id=int(input("Ingrese el Id del Empleado: "))
                    datos=EmpleadosDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print(f"Direccion:  {datos[2]}")
                        print(f"Fono:  {datos[3]}")
                        print(f"Correo:  {datos[4]}")
                        print(f"Fecha Contrato:  {datos[5]}")
                        print(f"Salario:  {datos[6]}")
                        print("--------------------------------")
                    else:
                        print("El Empleado No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menuempleado()
                    op=int(input("Ingrese Opcion: "))
                except ValueError as e:
                    print("Valor ingresado no Corresponde")
            case 4: 
                try:
                    id=int(input("Ingrese el Id del Empleado: "))
                    datos=EmpleadosDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print(f"Direccion:  {datos[2]}")
                        print(f"Fono:  {datos[3]}")
                        print(f"Correo:  {datos[4]}")
                        print(f"Fecha Contrato:  {datos[5]}")
                        print(f"Salario:  {datos[6]}")
                        print("--------------------------------")
                        opcion=input("Confirma la Eliminación S=Si, otra Descarta:")
                        if opcion.upper()=='S':
                            EmpleadosDAO.remove(id)
                        else:
                            print("Se ha cancelado la Eliminación del Empleado..")
                    else:
                        print("Empleado No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menuempleado()
                    op=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                    print("Valor Ingresado no Corresponde")  
                    id=int(input("Ingrese el Id del Empleado: "))
            case 0:
                menuprincipal()
                


def menuempleadodepartamentogerente():
    print("A S I G N A R    E M P L E A D O    A     D E P A R T A M E N T O")
    print("--------------------------------------------------------------------")
    print("1- Asignar un Empleado a un Departamento")
    print("2- Reasignar un Empleado a un Proyecto")
    print("3- Buscar con ID a un Empleado con su Departamento")
    print("4- Eliminar un Empleado con su Respectivo Departamento")
    print("0- Salir")
    print("--------------------------------------------------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
        match op:
            case 1:
                try:
                    id=int(input("Ingrese el Id del Empleado: "))
                    datos=EmpleadosDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print(f"Direccion:  {datos[2]}")
                        print(f"Fono:  {datos[3]}")
                        print(f"Correo:  {datos[4]}")
                        print(f"Fecha Contrato:  {datos[5]}")
                        print(f"Salario:  {datos[6]}")
                        print("--------------------------------")
                    else:
                        print("El Empleado No Existe....")
                    id=int(input("Ingrese el Id del Departamento: "))
                    datodepartamento=DepartamentoDAO.BuscarId(id)
                    if datodepartamento is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datodepartamento[1]}")
                        print("--------------------------------")
                        opcion=input("Confirma la Asignacion S=Si, otra Descarta:")
                        if opcion.upper()=='S':
                            EmpleadoDepartamentoDAO.Asignar_empleado_a_departamento(datos[0],datodepartamento[0])
                        else:
                            print("Asignacion No Existe....")
                            input("pulse cualquier tecla para continuar....")
                    menuaempleadodepartamento()
                    op=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                        print("Valor Ingresado no Corresponde")  
                        id=int(input("Ingrese el Id del Departamento: "))
            case 2:
                try:
                    id=int(input("Ingrese el Id de la Reasignacion que desea realizar: "))
                    datos=EmpleadoDepartamentoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"ID Empleado:  {datos[1]}")
                        print(f"ID Departamento:  {datos[2]}")
                        print("--------------------------------")
                    else:
                        print("El ID No Existe....")
                    id_reasignacion = int(input("Ingrese el ID de la reasignación que desea realizar: "))
                    id_empleado = int(input("Ingrese el nuevo ID del empleado: "))
                    id_departamento = int(input("Ingrese el nuevo ID del departamento: "))
                    EmpleadoDepartamentoDAO.update(id_reasignacion,id_empleado, id_departamento)
                    menuaempleadodepartamento()  # Volver al menú principal
                    op_proyecto = int(input("Ingrese Opcion: "))  # Esperar la siguiente opción
                except ValueError as e:
                    print("Valor ingresado no corresponde")

            case 3: 
                    try:
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
                        datos=EmpleadoDepartamentoDAO.BuscarId(id)
                        if datos is not None:
                            print("--------------------------------")
                            print(f"ID del Empleado:  {datos[1]}")
                            print(f"ID del Departamento:  {datos[2]}")
                            print("--------------------------------")
                        else:
                            print("ID No Existe....")
                        input("pulse cualquier tecla para continuar....")
                        menuaempleadodepartamento()
                    except ValueError as e:
                        print("Valor Ingresado no Corresponde")  
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
            case 4: 
                    try:
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
                        datos=EmpleadoDepartamentoDAO.BuscarId(id)
                        if datos is not None:
                            print("--------------------------------")
                            print(f"ID del Empleado:  {datos[1]}")
                            print(f"ID del Departamento:  {datos[2]}")
                            print("--------------------------------")
                            op_proyecto=input("Confirma la Eliminación S=Si, otra Descarta:")
                            if op_proyecto.upper()=='S':
                                EmpleadoDepartamentoDAO.remove(id)
                            else:
                                print("Se ha cancelado la Eliminación..")
                        else:
                            print("ID No Existe....")
                        input("pulse cualquier tecla para continuar....")
                        menuaempleadodepartamento()
                        op_proyecto=int(input("Ingrese Opcion: ")) 
                    except ValueError as e:
                        print("Valor Ingresado no Corresponde")  
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
            case 0:
                menuprincipalgerente()


def menuproyecto():
    os.system('cls')
    print("M E N U    P R O Y E C T O S")
    print("---------------------------")
    print("1- Ingresar un Proyecto")
    print("2- Actualizar un Proyecto")
    print("3- Buscar un Proyecto")
    print("4- Eliminar un Proyecto")
    print("0- Salir")
    print("---------------------------")
    op_proyecto=int(input("Ingrese Opcion: "))
    while op_proyecto>=0:
        match op_proyecto:
            case 1:
                try:
                    nombre=input("Ingrese el Nombre del Proyecto:    ")
                    descripcion=input("Ingrese una Descripcion al Proyecto:   ")
                    fechainicio=input("Ingrese la Fecha de inicio del Proyecto:  ")
                    try:
                        fechainicio = datetime.strptime(fechainicio, "%Y-%m-%d")
                    except ValueError:
                        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
                    proyecto=Proyectos(nombre,descripcion,fechainicio)
                    ProyectosDAO.add(proyecto)
                    menuproyecto()
                    op_proyecto=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 2:
                try:
                    id=int(input("Ingrese la ID del Proyecto:   "))
                    nombre=input("Ingrese el Nombre del Proyecto:    ")
                    descripcion=input("Ingrese una Descripcion al Proyecto:   ")
                    fechainicio=input("Ingrese la Fecha de inicio del Proyecto:  ")
                    try:
                        fechainicio = datetime.strptime(fechainicio, "%Y-%m-%d")
                    except ValueError:
                        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
                    proyecto=Proyectos(nombre,descripcion,fechainicio)
                    proyecto.setId(id)
                    ProyectosDAO.update(proyecto)
                    menuproyecto()
                    op_proyecto=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 3:
                try:
                    id=int(input("Ingrese el Id del Proyecto: "))
                    datos=ProyectosDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre del Proyecto:  {datos[1]}")
                        print(f"Descripcion:  {datos[2]}")
                        print(f"Fecha de Inicio:  {datos[3]}")
                        print("--------------------------------")
                    else:
                        print("El Proyecto No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menuproyecto()
                    op_proyecto=int(input("Ingrese Opcion: "))
                except ValueError as e:
                    print("Valor ingresado no Corresponde")
            case 4: 
                try:
                    id=int(input("Ingrese el Id del Proyecto: "))
                    datos=ProyectosDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre del Proyecto:  {datos[1]}")
                        print(f"Descripcion:  {datos[2]}")
                        print(f"Fecha de Inicio:  {datos[3]}")
                        print("--------------------------------")
                        op_proyecto=input("Confirma la Eliminación S=Si, otra Descarta:")
                        if op_proyecto.upper()=='S':
                            ProyectosDAO.remove(id)
                        else:
                            print("Se ha cancelado la Eliminación del Proyecto..")
                    else:
                        print("Proyecto No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menuproyecto()
                    op_proyecto=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                    print("Valor Ingresado no Corresponde")  
                    id=int(input("Ingrese el Id del Proyecto: "))
            case 0:
                menuprincipal()


def menuroles():
    os.system('cls')
    print("M E N U   T R A B A J O S")
    print("---------------------------")
    print("1- Ingresar un Trabajo")
    print("2- Actualizar un Trabajo")
    print("3- Buscar un Trabajo por Id")
    print("4- Eliminar un Trabajo")
    print("0- Salir")
    print("---------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
        match op:
            case 1:
                try:
                    nombre=input("Ingrese el Nombre del Trabajo :    ")
                    rol=Roles(nombre)
                    RolesDAO.add(rol)
                    menuroles()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 2:
                try:
                    id=int(input("Ingrese la Id del Trabajo:   "))
                    nombre=input("Ingrese el Nombre:    ")
                    rol=Roles(nombre)
                    rol.setId(id)
                    RolesDAO.update(rol)
                    menuroles()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 3:
                try:
                    id=int(input("Ingrese el Id del Trabajo: "))
                    datos=RolesDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print("--------------------------------")
                    else:
                        print("El Trabajo No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menuroles()
                    op=int(input("Ingrese Opcion: "))
                except ValueError as e:
                    print("Valor ingresado no Corresponde")
            case 4: 
                try:
                    id=int(input("Ingrese el Id del Trabajo: "))
                    datos=RolesDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print("--------------------------------")
                        opcion=input("Confirma la Eliminación S=Si, otra Descarta:")
                        if opcion.upper()=='S':
                            RolesDAO.remove(id)
                        else:
                            print("Se ha cancelado la Eliminación del Trabajo..")
                    else:
                        print("Trabajo No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menuroles()
                    op=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                    print("Valor Ingresado no Corresponde")  
                    id=int(input("Ingrese el Id del Trabajo: "))
            case 0:
                menuprincipal()


def menutiempo():
    os.system('cls')
    print("M E N U    T I E M P O ")
    print("---------------------------")
    print("1- Ingresar Tiempo")
    print("2- Actualizar el Tiempo")
    print("3- Buscar el Tiempo")
    print("4- Eliminar el Tiempo")
    print("0- Salir")
    print("---------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
        match op:
            case 1:
                try:
                    horas=input("Ingrese la cantidad de Horas:    ")
                    tareas=input("Ingrese la Cantidad de Tareas:     ")
                    fecha=input("Ingrese la Fecha :  ")
                    try:
                        fecha = datetime.strptime(fecha, "%Y-%m-%d")
                    except ValueError:
                        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")     
                    descripcion=input("Ingrese una Descripcion:    ")
                    tiempo=Tiempo(horas,tareas,fecha,descripcion)
                    TiempoDAO.add(tiempo)
                    menutiempo()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 2:
                try:
                    id=int(input("Ingrese la ID del Tiempo:   "))
                    horas=input("Ingrese la cantidad de Horas:    ")
                    tareas=input("Ingrese la Cantidad de Tareas:     ")
                    fecha=input("Ingrese la Fecha :  ")
                    try:
                        fecha = datetime.strptime(fecha, "%Y-%m-%d")
                    except ValueError:
                        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")     
                    descripcion=input("Ingrese una Descripcion:    ")
                    tiempo=Tiempo(horas,tareas,fecha,descripcion)
                    tiempo.setId(id)
                    TiempoDAO.update(tiempo)
                    menutiempo()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 3:
                try:
                    id=int(input("Ingrese el Id del Tiempo: "))
                    datos=TiempoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Cantidad de Horas:  {datos[1]}")
                        print(f"Cantidad de Tareas:  {datos[2]}")
                        print(f"Fecha :  {datos[3]}")
                        print(f"Descripcion :  {datos[4]}")
                        print("--------------------------------")
                    else:
                        print("El Tiempo No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menutiempo()
                    op=int(input("Ingrese Opcion: "))
                except ValueError as e:
                    print("Valor ingresado no Corresponde")
            case 4: 
                try:
                    id=int(input("Ingrese el Id del Empleado: "))
                    datos=TiempoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Cantidad de Horas:  {datos[1]}")
                        print(f"Cantidad de Tareas:  {datos[2]}")
                        print(f"Fecha :  {datos[3]}")
                        print(f"Descripcion :  {datos[4]}")
                        print("--------------------------------")
                        opcion=input("Confirma la Eliminación S=Si, otra Descarta:")
                        if opcion.upper()=='S':
                            TiempoDAO.remove(id)
                        else:
                            print("Se ha cancelado la Eliminación del Empleado..")
                    else:
                        print("Empleado No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menutiempo()
                    op=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                    print("Valor Ingresado no Corresponde")  
                    id=int(input("Ingrese el Id del Empleado: "))
            case 0:
                menuprincipal()


def menudepartamentogerente():
    os.system('cls')
    print("M E N U    D E P A R T A M E N T O")
    print("---------------------------")
    print("1- Ingresar un Departamento")
    print("2. Actualizar un Departamento")
    print("3- Buscar un Departamento")
    print("4- Eliminar un Departamento")
    print("0- Salir")
    print("---------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
        match op:
            case 1:
                try:
                    nombredepartamento=input("Ingrese el Nombre:    ")
                    departamento=Departamento(nombredepartamento)
                    DepartamentoDAO.add(departamento)
                    menudepartamento()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 2:
                try:
                    id=int(input("Ingrese la Id del Departamento:   "))
                    nombredepartamento=input("Ingrese el Nombre:    ")
                    departamento=Departamento(nombredepartamento)
                    departamento.setIdDepartamento(id)
                    DepartamentoDAO.update(departamento)
                    menudepartamento()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 3:
                try:
                    id=int(input("Ingrese el Id del Departamento: "))
                    datos=DepartamentoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print("--------------------------------")
                    else:
                        print("El Departamento No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menudepartamento()
                    op=int(input("Ingrese Opcion: "))
                except ValueError as e:
                    print("Valor ingresado no Corresponde")

            case 4: 
                try:
                    id=int(input("Ingrese el Id del Departamento: "))
                    datos=DepartamentoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print("--------------------------------")
                        opcion=input("Confirma la Eliminación S=Si, otra Descarta:")
                        if opcion.upper()=='S':
                            DepartamentoDAO.remove(id)
                        else:
                            print("Se ha cancelado la Eliminación del Departamento..")
                    else:
                        print("Departamento No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menudepartamento()
                    op=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                    print("Valor Ingresado no Corresponde")  
                    id=int(input("Ingrese el Id del Departamento: "))
            case 0:
                menuprincipalgerente()






def menudepartamento():
    os.system('cls')
    print("M E N U    D E P A R T A M E N T O")
    print("---------------------------")
    print("1- Ingresar un Departamento")
    print("2. Actualizar un Departamento")
    print("3- Buscar un Departamento")
    print("4- Eliminar un Departamento")
    print("0- Salir")
    print("---------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
        match op:
            case 1:
                try:
                    nombredepartamento=input("Ingrese el Nombre:    ")
                    departamento=Departamento(nombredepartamento)
                    DepartamentoDAO.add(departamento)
                    menudepartamento()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 2:
                try:
                    id=int(input("Ingrese la Id del Departamento:   "))
                    nombredepartamento=input("Ingrese el Nombre:    ")
                    departamento=Departamento(nombredepartamento)
                    departamento.setIdDepartamento(id)
                    DepartamentoDAO.update(departamento)
                    menudepartamento()
                    op=int(input("Ingrese Opcion:  "))
                except Exception as e:
                    print(f"Error Instruccion SQL: {e}")
            case 3:
                try:
                    id=int(input("Ingrese el Id del Departamento: "))
                    datos=DepartamentoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print("--------------------------------")
                    else:
                        print("El Departamento No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menudepartamento()
                    op=int(input("Ingrese Opcion: "))
                except ValueError as e:
                    print("Valor ingresado no Corresponde")

            case 4: 
                try:
                    id=int(input("Ingrese el Id del Departamento: "))
                    datos=DepartamentoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print("--------------------------------")
                        opcion=input("Confirma la Eliminación S=Si, otra Descarta:")
                        if opcion.upper()=='S':
                            DepartamentoDAO.remove(id)
                        else:
                            print("Se ha cancelado la Eliminación del Departamento..")
                    else:
                        print("Departamento No Existe....")
                    input("pulse cualquier tecla para continuar....")
                    menudepartamento()
                    op=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                    print("Valor Ingresado no Corresponde")  
                    id=int(input("Ingrese el Id del Departamento: "))
            case 0:
                menuprincipal()


def menuaempleadodepartamento():
    print("A S I G N A R    E M P L E A D O    A     D E P A R T A M E N T O")
    print("--------------------------------------------------------------------")
    print("1- Asignar un Empleado a un Departamento")
    print("2- Reasignar un Empleado a un Departamento")
    print("3- Buscar con ID a un Empleado con su Departamento")
    print("4- Eliminar un Empleado con su Respectivo Departamento")
    print("0- Salir")
    print("--------------------------------------------------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
        match op:
            case 1:
                try:
                    id=int(input("Ingrese el Id del Empleado: "))
                    datos=EmpleadosDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datos[1]}")
                        print(f"Direccion:  {datos[2]}")
                        print(f"Fono:  {datos[3]}")
                        print(f"Correo:  {datos[4]}")
                        print(f"Fecha Contrato:  {datos[5]}")
                        print(f"Salario:  {datos[6]}")
                        print("--------------------------------")
                    else:
                        print("El Empleado No Existe....")
                    id=int(input("Ingrese el Id del Departamento: "))
                    datodepartamento=DepartamentoDAO.BuscarId(id)
                    if datodepartamento is not None:
                        print("--------------------------------")
                        print(f"Nombre:  {datodepartamento[1]}")
                        print("--------------------------------")
                        opcion=input("Confirma la Asignacion S=Si, otra Descarta:")
                        if opcion.upper()=='S':
                            EmpleadoDepartamentoDAO.Asignar_empleado_a_departamento(datos[0],datodepartamento[0])
                        else:
                            print("Asignacion No Existe....")
                            input("pulse cualquier tecla para continuar....")
                    menuaempleadodepartamento()
                    op=int(input("Ingrese Opcion: ")) 
                except ValueError as e:
                        print("Valor Ingresado no Corresponde")  
                        id=int(input("Ingrese el Id del Departamento: "))
            case 2:
                try:
                    id=int(input("Ingrese el Id de la Reasignacion que desea realizar: "))
                    datos=EmpleadoDepartamentoDAO.BuscarId(id)
                    if datos is not None:
                        print("--------------------------------")
                        print(f"ID Empleado:  {datos[1]}")
                        print(f"ID Departamento:  {datos[2]}")
                        print("--------------------------------")
                    else:
                        print("El ID No Existe....")
                    id_reasignacion = int(input("Ingrese el ID de la reasignación que desea realizar: "))
                    id_empleado = int(input("Ingrese el nuevo ID del empleado: "))
                    id_departamento = int(input("Ingrese el nuevo ID del departamento: "))
                    EmpleadoDepartamentoDAO.update(id_reasignacion,id_empleado, id_departamento)
                    menuaempleadodepartamento()  # Volver al menú principal
                    op_proyecto = int(input("Ingrese Opcion: "))  # Esperar la siguiente opción
                except ValueError as e:
                    print("Valor ingresado no corresponde")

            case 3: 
                    try:
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
                        datos=EmpleadoDepartamentoDAO.BuscarId(id)
                        if datos is not None:
                            print("--------------------------------")
                            print(f"ID del Empleado:  {datos[1]}")
                            print(f"ID del Departamento:  {datos[2]}")
                            print("--------------------------------")
                        else:
                            print("ID No Existe....")
                        input("pulse cualquier tecla para continuar....")
                        menuaempleadodepartamento()
                    except ValueError as e:
                        print("Valor Ingresado no Corresponde")  
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
            case 4: 
                    try:
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
                        datos=EmpleadoDepartamentoDAO.BuscarId(id)
                        if datos is not None:
                            print("--------------------------------")
                            print(f"ID del Empleado:  {datos[1]}")
                            print(f"ID del Departamento:  {datos[2]}")
                            print("--------------------------------")
                            op_proyecto=input("Confirma la Eliminación S=Si, otra Descarta:")
                            if op_proyecto.upper()=='S':
                                EmpleadoDepartamentoDAO.remove(id)
                            else:
                                print("Se ha cancelado la Eliminación..")
                        else:
                            print("ID No Existe....")
                        input("pulse cualquier tecla para continuar....")
                        menuaempleadodepartamento()
                        op_proyecto=int(input("Ingrese Opcion: ")) 
                    except ValueError as e:
                        print("Valor Ingresado no Corresponde")  
                        id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Departamento: "))
            case 0:
                menuprincipal()

def menuempleadoproyecto():
    print("A S I G N A R    E M P L E A D O    A     P R O Y E C T O ")
    print("--------------------------------------------------------------------")
    print("1- Asignar un Empleado a un Proyecto")
    print("2- Reasignar un Empleado a un Proyecto")
    print("3- Buscar con ID a un Empleado con su Proyecto")
    print("4- Eliminar un Empleado con su Respectivo Proyecto")
    print("0- Salir")
    print("--------------------------------------------------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0:
            match op:
                case 1:
                    try:
                        id=int(input("Ingrese el Id del Empleado: "))
                        datos=EmpleadosDAO.BuscarId(id)
                        if datos is not None:
                            print("--------------------------------")
                            print(f"Nombre:  {datos[1]}")
                            print(f"Direccion:  {datos[2]}")
                            print(f"Fono:  {datos[3]}")
                            print(f"Correo:  {datos[4]}")
                            print(f"Fecha Contrato:  {datos[5]}")
                            print(f"Salario:  {datos[6]}")
                            print("--------------------------------")
                        else:
                            print("El Empleado No Existe....")
                        id=int(input("Ingrese el Id del Proyecto: "))
                        datoproyecto=ProyectosDAO.BuscarId(id)
                        if datoproyecto is not None:
                            print("--------------------------------")
                            print(f"Nombre:  {datoproyecto[1]}")
                            print(f"Descripcion:  {datoproyecto[2]}")
                            print(f"Fecha de inicio:  {datoproyecto[3]}")
                            print("--------------------------------")
                            opcion=input("Confirma la Asignacion S=Si, otra Descarta:")
                            if opcion.upper()=='S':
                                EmpleadoProyectoDAO.Asignar_empleado_a_proyecto(datos[0],datoproyecto[0])
                                print("La Reasignacion fue exitosa......")
                                input("pulse cualquier tecla para continuar....")
                            else:
                                print("Asignacion No Existe....")
                                input("pulse cualquier tecla para continuar....")
                        menuempleadoproyecto()
                        op=int(input("Ingrese Opcion: ")) 
                    except ValueError as e:
                            print("Valor Ingresado no Corresponde")  
                            id=int(input("Ingrese el Id del Proyecto: "))
                case 2:
                    try:
                        id=int(input("Ingrese el Id de la Reasignacion que desea realizar: "))
                        datos=EmpleadoProyectoDAO.BuscarId(id)
                        if datos is not None:
                            print("--------------------------------")
                            print(f"ID Empleado:  {datos[1]}")
                            print(f"ID Proyecto:  {datos[2]}")
                            print("--------------------------------")
                        else:
                            print("El ID No Existe....")
                        id_reasignacion = int(input("Ingrese el ID de la reasignación que desea realizar: "))
                        id_empleado = int(input("Ingrese el nuevo ID del Empleado:   "))
                        id_proyecto = int(input("Ingrese el nuevo ID del Proyecto:   "))
                        EmpleadoProyectoDAO.update(id_reasignacion,id_empleado,id_proyecto)
                        menuempleadoproyecto()  # Volver al menú principal
                        op_proyecto = int(input("Ingrese Opcion: "))  # Esperar la siguiente opción
                    except ValueError as e:
                        print("Valor ingresado no corresponde")
                case 3:
                    try:
                            id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Proyecto: "))
                            datos=EmpleadoProyectoDAO.BuscarId(id)
                            if datos is not None:
                                print("--------------------------------")
                                print(f"ID del Empleado:  {datos[1]}")
                                print(f"ID del Proyecto:  {datos[2]}")
                                print("--------------------------------")
                            else:
                                print("La ID No Existe....")
                            input("pulse cualquier tecla para continuar....")
                            menuempleadoproyecto()
                            op_proyecto=int(input("Ingrese Opcion: "))
                    except ValueError as e:
                        print("Valor ingresado no Corresponde")
                case 4: 
                        try:
                            id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Proyecto: "))
                            datos=EmpleadoProyectoDAO.BuscarId(id)
                            if datos is not None:
                                print("--------------------------------")
                                print(f"ID del Empleado:  {datos[1]}")
                                print(f"ID del Proyecto:  {datos[2]}")
                                print("--------------------------------")
                                op_proyecto=input("Confirma la Eliminación S=Si, otra Descarta:")
                                if op_proyecto.upper()=='S':
                                    EmpleadoProyectoDAO.remove(id)
                                else:
                                    print("Se ha cancelado la Eliminación..")
                            else:
                                print("ID No Existe....")
                            input("pulse cualquier tecla para continuar....")
                            menuempleadoproyecto()
                            op_proyecto=int(input("Ingrese Opcion: ")) 
                        except ValueError as e:
                            print("Valor Ingresado no Corresponde")  
                            id=int(input("Ingrese el Id del que tiene el Dato del Empleado y Proyecto: "))
                case 0:
                    menuprincipal()

def generarinforme():
    print("G E N E R A R     I N F O R M E")
    print("-------------------------------")
    print("1- Generar Informe de Empleados")
    print("2- Generar Informe de Proyectos")
    print("3- Generar Informe de Roles")
    print("4- Generar Informe de Departamentos")
    print("0- Salir")
    print("-------------------------------")
    op=int(input("Ingrese Opcion: "))
    while op>=0 and op<=6:
        match op:
            case 1:
                print("L I S T A D O   D E  E M P L E A D O S ")
                print("=" * 150)
                print("{:<12} {:<20} {:<25} {:<15} {:<30} {:<20} {:<15}".format("Id_Empleado", "Nombre", "Direccion", "Fono", "Correo", "Fecha Contrato", "Salario"))
                print("-" * 150)
                datos = EmpleadosDAO.Listar()
                for dato in datos:
                    formatted_date = dato[5].strftime("%Y-%m-%d") if dato[5] else "N/A"
                    print("{:<12} {:<20} {:<25} {:<15} {:<30} {:<20} {:<15}".format(dato[0], dato[1], dato[2], dato[3], dato[4], formatted_date, dato[6]))
                print("-" * 150)
                input("Pulse cualquier tecla para continuar....")
                generarinforme()
            case 2:
                print("L I S T A D O   D E   P R O Y E C T O S")
                print("=" * 90)
                print("{:<5} {:<25} {:<40} {:<20}".format("Id", "Nombre", "Descripcion", "Fecha de Inicio"))
                print("-" * 90)
                datos = ProyectosDAO.Listar()
                for dato in datos:
                    print(f"{dato[0]:<5} {dato[1]:<25} {dato[2]:<40} {dato[3]}")
                print("-" * 90)
                input("pulse cualquier tecla para continuar....")
                generarinforme()
            case 3:
                print("L I S T A D O   D E  R O L E S")
                print("=============================================")
                print("ID Rol\t  ROL\t")
                print("-----------------------------------------")
                datos=RolesDAO.Listar()
                for dato in datos:
                    print(f"{dato[0]}\t {dato[1]}\t")
                print("-----------------------------------------")
                input("pulse cualquier tecla para continuar....")
                generarinforme()
                op=int(input("Ingrese Opcion: "))
            case 4:
                print("L I S T A D O   D E    D E P A R T A M E N T O S")
                print("=============================================")
                print("ID Departamento\t  Nombre Departamento\t")
                print("-----------------------------------------")
                datos=DepartamentoDAO.Listar()
                for dato in datos:
                    print(f"{dato[0]}\t\t {dato[1]}\t")
                print("-----------------------------------------")
                input("pulse cualquier tecla para continuar....")
                generarinforme()
                op=int(input("Ingrese Opcion: "))
            case 0:
                menuprincipal()






    
def registrar_usuario():
    print("==================================")
    print("R E G I S T R A R     U S U A R I O")
    print("==================================")
    username = input("Ingrese un nombre de usuario: ")
    password_hash = input("Ingrese la contraseña del usuario: ")
    rol=input("Ingrese el rol del usuario:  ")
    print("================================================")
    UsuarioDAO.registrar_usuario(username,password_hash,rol)


def iniciar_sesion():
    intentos=5
    salida=False
    while(intentos>0 and salida==False):
        username=input("Ingrese su Usuario: ")
        password=input("Ingrese su Password: ")
        datos=UsuarioDAO.login(username,password)
        if datos is None:
            print("Usuario No Encontrado o Contraseña Incorrecta!!!!!")
            intentos=intentos-1
            print(f"Te Quedan: {intentos} Intentos")
        else:
            salida=True

    if salida==True:
        os.system('cls')
        print("BIENVENIDO")
        print("-------------------------------------")
        print(f"Usuario Conectado: {datos[1]}")
        print(f"Nombre de Usuario: {datos[3]}")
        print(f"Apellido de Usuario: {datos[4]}")

registrar_usuario()
















