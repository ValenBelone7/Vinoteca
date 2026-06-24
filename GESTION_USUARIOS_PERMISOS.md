# Gestión de Usuarios y Permisos en Django

## Introducción

Este documento explica cómo gestionar usuarios y permisos en el proyecto Vinoteca Django. Cubre cómo crear usuarios, asignarlos a grupos, y cómo los grupos otorgan permisos a los usuarios.

## Gestión Básica de Usuarios

### Crear un Usuario Normal

Puedes crear un usuario normal usando el shell de Django:

```python
from django.contrib.auth import get_user_model

User = get_user_model()

# Crear un usuario normal
user, created = User.objects.get_or_create(
    username='empleado1',
    email='empleado1@example.com'
)

if created:
    user.set_password('empleado123')
    user.save()
    print(f'✅ Usuario {user.username} creado')
```

### Crear un Usuario Admin

Puedes crear un usuario admin (superusuario) de dos maneras:

#### Método 1: Usando el comando manage.py

```bash
python manage.py createsuperuser
# Seguir las instrucciones para crear un usuario admin
```

#### Método 2: Usando el shell de Django

```python
from django.contrib.auth import get_user_model

User = get_user_model()

# Crear un usuario admin
admin_user, created = User.objects.get_or_create(
    username='admin',
    email='admin@example.com'
)

if created:
    admin_user.set_password('admin123')
    admin_user.is_superuser = True
    admin_user.save()
    print(f'✅ Usuario admin {admin_user.username} creado')
```

## Grupos y Permisos

### Grupos Predefinidos

El proyecto ya tiene dos grupos predefinidos:

1. **Administradores**: Tiene todos los permisos sobre Vino, Bodega, Proveedor, Compra
2. **Empleados**: Tiene solo permisos `view` y `add` sobre Vino y Compra

### Asignar Usuarios a Grupos

Puedes asignar un usuario a un grupo usando el shell de Django:

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

# Obtener el usuario y el grupo
user = User.objects.get(username='empleado1')
group = Group.objects.get(name='Empleados')

# Asignar el usuario al grupo
user.groups.add(group)
print(f'✅ Usuario {user.username} asignado al grupo {group.name}')
```

### Verificar Permisos de un Usuario

Puedes verificar los permisos de un usuario usando el shell de Django:

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

# Obtener el usuario
user = User.objects.get(username='empleado1')

# Verificar si el usuario tiene un permiso específico
if user.has_perm('vinoteca.add_vino'):
    print('✅ Usuario puede crear vinos')
else:
    print('❌ Usuario no puede crear vinos')

# Verificar si el usuario pertenece a un grupo
if user.groups.filter(name='Empleados').exists():
    print('✅ Usuario pertenece al grupo Empleados')
else:
    print('❌ Usuario no pertenece al grupo Empleados')
```

## Flujo de Trabajo Completo

### Paso 1: Crear Usuarios

```python
# Crear un usuario normal
user, created = User.objects.get_or_create(
    username='empleado1',
    email='empleado1@example.com'
)
if created:
    user.set_password('empleado123')
    user.save()

# Crear un usuario admin
admin_user, created = User.objects.get_or_create(
    username='admin',
    email='admin@example.com'
)
if created:
    admin_user.set_password('admin123')
    admin_user.is_superuser = True
    admin_user.save()
```

### Paso 2: Asignar Usuarios a Grupos

```python
# Asignar usuario normal al grupo Empleados
empleado = User.objects.get(username='empleado1')
empleados_group = Group.objects.get(name='Empleados')
empleado.groups.add(empleados_group)

# Asignar usuario admin al grupo Administradores
admin_user = User.objects.get(username='admin')
administradores_group = Group.objects.get(name='Administradores')
admin_user.groups.add(administradores_group)
```

### Paso 3: Verificar Permisos

```python
# Verificar permisos del usuario normal
empleado = User.objects.get(username='empleado1')
print(f'Permisos del empleado: {empleado.get_all_permissions()}')
print(f'Grupos del empleado: {[g.name for g in empleado.groups.all()]}')

# Verificar permisos del usuario admin
admin_user = User.objects.get(username='admin')
print(f'Permisos del admin: {admin_user.get_all_permissions()}')
print(f'Grupos del admin: {[g.name for g in admin_user.groups.all()]}')
```

## Uso en Templates

Puedes usar los permisos en los templates para mostrar/ocultar botones según los permisos del usuario:

```html
<!-- Mostrar botón de crear vino solo si el usuario tiene permiso -->
{% if perms.vinoteca.add_vino %}
    <a href="{% url 'crear_vino' %}">Crear vino</a>
{% endif %}

<!-- Mostrar botón de editar vino solo si el usuario tiene permiso -->
{% if perms.vinoteca.change_vino %}
    <a href="{% url 'editar_vino' vino.pk %}">Editar vino</a>
{% endif %}

<!-- Mostrar botón de eliminar vino solo si el usuario tiene permiso -->
{% if perms.vinoteca.delete_vino %}
    <a href="{% url 'eliminar_vino' vino.pk %}">Eliminar vino</a>
{% endif %}
```

## API de Permisos

Django proporciona varias formas de verificar los permisos de un usuario:

### 1. Usando `has_perm()`

```python
# Verificar si el usuario tiene un permiso específico
if user.has_perm('vinoteca.add_vino'):
    print('Usuario puede crear vinos')
```

### 2. Usando `get_all_permissions()`

```python
# Obtener todos los permisos del usuario
all_perms = user.get_all_permissions()
print(f'Total de permisos: {len(all_perms)}')
```

### 3. Usando `groups` y `user_permissions`

```python
# Obtener todos los grupos del usuario
for group in user.groups.all():
    print(f'Grupo: {group.name}')
    print(f'Permisos del grupo: {group.permissions.count()}')

# Obtener todos los permisos directos del usuario
for permiso in user.user_permissions.all():
    print(f'Permiso directo: {permiso}')
```

## Ejemplo de Flujo de Trabajo Completo

```python
# 1. Crear usuarios
user1, created = User.objects.get_or_create(username='empleado1', email='empleado1@example.com')
if created:
    user1.set_password('empleado123')
    user1.save()

user2, created = User.objects.get_or_create(username='admin', email='admin@example.com')
if created:
    user2.set_password('admin123')
    user2.is_superuser = True
    user2.save()

# 2. Asignar usuarios a grupos
empleado = User.objects.get(username='empleado1')
administradores = Group.objects.get(name='Administradores')
empleado.groups.add(administradores)

admin_user = User.objects.get(username='admin')
empleados = Group.objects.get(name='Empleados')
admin_user.groups.add(empleados)

# 3. Verificar permisos
print(f'Permisos del empleado: {empleado.get_all_permissions()}')
print(f'Permisos del admin: {admin_user.get_all_permissions()}')

# 4. Probar la vista protegida
from django.test import RequestFactory
from vinoteca.views import crear_vino

factory = RequestFactory()
request = factory.get('/vinos/crear/')
request.user = empleado

# Intentar acceder a la vista protegida
try:
    response = crear_vino(request)
    print('✅ Empleado puede acceder a la vista crear_vino')
except PermissionDenied:
    print('❌ Empleado no puede acceder a la vista crear_vino')
```

## Resumen

1. **Crear usuarios** usando `User.objects.get_or_create()` o `createsuperuser`
2. **Asignar usuarios a grupos** usando `user.groups.add(group)`
3. **Verificar permisos** usando `user.has_perm('app_label.codename')`
4. **Usar permisos en templates** con `{% if perms.app_label.codename %}`
5. **Los grupos otorgan permisos** automáticamente a todos sus miembros

El sistema de grupos y permisos en Django es flexible y permite un control granular sobre quién puede hacer qué en el sistema.
