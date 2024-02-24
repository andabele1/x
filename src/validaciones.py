def validar_id(id: str) -> bool:
    return (id.isnumeric() and len(id) >= 11)

def validar_usuario(usuario: str) -> bool:
    usuario = usuario.strip()
    return (len(usuario) > 0 and len(usuario) <= 30)

def validar_email(email: str) -> bool:
    email = email.strip()
    return (len(email) > 0 and len(email) <= 50)

def validar_contraseña(contraseña: str) -> bool:
    contraseña = contraseña.strip()
    return (len(contraseña) > 8 and len(contraseña) <= 30)

def validar_rol(rol: str) -> bool:
    rol = rol.strip()
    return (len(rol) > 8 and len(rol) <= 30)
