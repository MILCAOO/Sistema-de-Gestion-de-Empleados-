import os
from DTO.Usuario import Usuario
from DAO import Conexion
from DAO import UsuarioDAO

usuario= UsuarioDAO.registrar_usuario('kevin','kevin123','ADMINISTRADOR')