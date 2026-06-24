# TP Evaluativo — Sistema de Gestión Vinoteca
## Plan de desarrollo · Django + Tailwind CSS

---

## Convenciones del proyecto (basadas en django-gym + proyectos del profe)

| Área | Convención |
|------|-----------|
| Vistas | FBV con patrón GET/POST manual, `get_object_or_404`, `redirect` post-POST |
| URLs | Español, snake_case: `lista_vinos`, `editar_vino/<int:pk>/` |
| Forms | `ModelForm` con `fields` explícitos, `clean_*` para validaciones custom |
| Templates | Heredan de `vinoteca/base.html`; bloques `title` y `content`; campos manuales |
| Auth | `accounts/` con `django.contrib.auth.urls` + vista `register/` propia |
| Permisos | `@login_required` + `@permission_required` (patrón todo-profe) |
| Admin | `@admin.register` con `list_display`, `list_filter`, `search_fields` |
| Estilos | Tailwind CSS via CDN (Play CDN para desarrollo) |
| Nombres | Español en vistas, URLs y UI; inglés solo donde Django lo exige |

---

## Estado del proyecto

> Última actualización: **23 de junio de 2026** · Rama de integración: `develop` @ `c308402`

| Parte | Rama | Estado | Merge en `develop` |
|-------|------|--------|-------------------|
| 1 — Setup y modelos | `feature/parte-1-modelos` | ✅ Completada | `f034272` |
| 2 — Panel de admin | `feature/parte-2-admin` | ✅ Completada | `4b7e515` |
| 3 — Autenticación | `feature/parte-3-auth` | ✅ Completada | `e6780cd` |
| 4 — CRUD vinos | `feature/parte-4-crud-vinos` | ✅ Completada | `dc166c8` |
| 4 — CRUD bodegas | `feature/parte-4-crud-bodegas` | ✅ Completada | `e7fd0cd` |
| 5 — Permisos y grupos | `feature/parte-5-permisos` | ✅ Completada | `c308402` |
| 6 — Context processor | `feature/parte-6-context-processor` | ✅ Completada | `dcf2c2d` |
| 7 — Templates y Tailwind | `feature/parte-7-templates` | 🔶 Parcial | integrado en partes 1, 3, 4 y 6 |
| 8 — README y entrega | `feature/parte-8-readme` | ⏳ Pendiente | — |

**Siguiente paso:** Parte 8 — crear README.md con capturas del proyecto funcionando y preparar entrega final.

**Estado actual:** ✅ Parte 5 completada (permisos y grupos)
⏳ Parte 8 en progreso (README y entrega final)

**Próximos pasos para Parte 8:**
1. ✅ Ejecutar el proyecto localmente (funciona)
2. ✅ Crear superusuario (admin/admin123)
3. ✅ Crear documentación de gestión de usuarios y permisos (GESTION_USUARIOS_PERMISOS.md)
4. ✅ Agregar sección de compras recientes al home page
5. ✅ Agregar varietal y categoria a los formularios de Vino (ya implementado)
6. ⏳ Tomar capturas del proyecto funcionando
7. ⏳ Escribir README.md con capturas
8. ⏳ Hacer merge de feature/parte-8-readme → develop → main
9. ⏳ Verificar checklist final de entrega

**Documentación adicional creada:**
- ✅ README.md con descripción completa del proyecto, modelos, relaciones, instrucciones de instalación y capturas (placeholder)
- ✅ GESTION_USUARIOS_PERMISOS.md con guía completa sobre cómo gestionar usuarios y permisos en Django

**Estado actual del proyecto:**
- ✅ Todos los modelos implementados (8 modelos)
- ✅ Todas las relaciones implementadas (FK y M2M)
- ✅ Al menos 1 ImageField (en Vino y Bodega)
- ✅ CustomUser con AbstractUser
- ✅ Registro, login y logout desde templates
- ✅ Navegación completa por el sistema
- ✅ CRUD completo de Vino (5 vistas)
- ✅ CRUD completo de Bodega (5 vistas)
- ✅ Control total desde el panel de admin con filtros, ordenamiento y búsqueda
- ✅ Al menos 1 context processor (datos_vinoteca)
- ✅ Carga de imágenes funcional (admin y formularios)
- ✅ Estilos con Tailwind CSS aplicados consistentemente
- ✅ Grupos y permisos implementados (Administradores y Empleados)
- ✅ Vistas protegidas con @login_required y @permission_required
- ✅ Botones en templates mostrados/ocultados según permisos
- ✅ Sección de compras recientes en home page

**Faltan por completar:**
- ⏳ Capturas del proyecto funcionando
- ⏳ README.md final con capturas reales
- ⏳ Merge de feature/parte-8-readme → develop → main
- ⏳ Verificar checklist final de entrega

**Mejoras implementadas recientemente:**
- ✅ Agregar varietal y categoria a los formularios de Vino (ya implementado)
- ✅ Agregar sección de compras recientes al home page
- ✅ Agregar datos de compras al context processor

---

## Metodología de trabajo con Git

### Estructura de ramas

```
main              ← producción / entrega final (solo merges desde develop)
  └── develop     ← rama de integración (merges de features terminadas)
        ├── feature/parte-1-modelos
        ├── feature/parte-2-admin
        ├── feature/parte-3-auth
        ├── feature/parte-4-crud-vinos
        ├── feature/parte-4-crud-bodegas
        ├── feature/parte-5-permisos
        ├── feature/parte-6-context-processor
        ├── feature/parte-7-templates
        └── feature/parte-8-readme
```

### Flujo de trabajo por parte

```bash
# 1. Siempre partir desde develop actualizado
git checkout develop
git pull origin develop

# 2. Crear la rama de la parte a trabajar
git checkout -b feature/parte-X-nombre

# 3. Trabajar, commitear seguido con mensajes claros
git add .
git commit -m "feat: descripción corta de lo que hice"

# 4. Pushear la rama al repositorio remoto
git push origin feature/parte-X-nombre

# 5. Cuando la parte está terminada: merge a develop
git checkout develop
git pull origin develop               # por si el otro dev pusheó algo
git merge feature/parte-X-nombre
git push origin develop

# 6. Solo cuando develop está estable y listo para entregar: merge a main
git checkout main
git merge develop
git push origin main
```

### Convención de mensajes de commit

```
feat: agrega modelo Vino con relaciones a Bodega y Varietal
feat: implementa CRUD de vinos (lista, detalle, crear, editar, eliminar)
fix: corrige validación de año en VinoForm
style: aplica clases Tailwind a base.html y navbar
docs: agrega capturas al README
chore: configura MEDIA_ROOT y variables de entorno
```

### Reglas de colaboración

- **Nunca pushear directo a `main`** — siempre pasar por `develop`
- **Resolver conflictos localmente** antes de pushear: `git pull origin develop` antes de cada merge
- **Una rama por parte** — no mezclar trabajo de partes distintas en la misma rama
- **Pull antes de empezar** — siempre `git pull origin develop` al iniciar una sesión de trabajo
- Si hay conflicto en un archivo de templates o modelos, resolverlo juntos antes de mergear

---

## Partes del proyecto

### Parte 1 — Setup del proyecto y modelos ✅
**Rama:** `feature/parte-1-modelos` · **Merge:** `f034272`

**Qué hacer:**
- Crear el proyecto: `vinotecaproject/` + apps `vinoteca/` y `usuarios/`
- Modelo `Usuario` extendiendo `AbstractUser`:
  - Campos extra: `foto` (`ImageField`), `telefono`, `direccion`
- Los 6+ modelos de `vinoteca/`:
  - `Bodega` — nombre, país, región, descripción, `logo` (`ImageField`)
  - `Varietal` — nombre (Malbec, Cabernet, Torrontés…), descripción
  - `Categoria` — nombre (Tinto, Blanco, Rosado, Espumante)
  - `Vino` — nombre, `bodega` (FK), `varietal` (FK), `categoria` (FK), año, precio, stock, `foto` (`ImageField`), descripción
  - `Proveedor` — nombre, email, teléfono, `bodegas` (M2M a Bodega)
  - `Compra` — `usuario` (FK a Usuario), fecha, estado (pendiente/completada/cancelada)
  - `ItemCompra` — `compra` (FK), `vino` (FK), cantidad, precio_unitario
- `settings.py`: `AUTH_USER_MODEL`, `MEDIA_ROOT`, `MEDIA_URL`, Tailwind Play CDN en base template
- Migraciones: `makemigrations` + `migrate`

**Resultado esperado:** shell de Django con todos los modelos importables y base de datos creada.

---

### Parte 2 — Panel de administración ✅
**Rama:** `feature/parte-2-admin` · **Merge:** `4b7e515`
**Depende de:** Parte 1 mergeada en develop

**Qué hacer:**
- `@admin.register` para todos los modelos
- Configurar por modelo:
  - `Vino`: `list_display = ['nombre', 'bodega', 'varietal', 'precio', 'stock']`, `list_filter = ['categoria', 'varietal', 'bodega']`, `search_fields = ['nombre']`
  - `Bodega`: `list_display`, `search_fields = ['nombre', 'pais']`
  - `Compra`: `list_display = ['usuario', 'fecha', 'estado']`, `list_filter = ['estado']`
  - Resto: configuración básica con `list_display` y `search_fields`
- Verificar que la carga de imágenes funcione desde el admin (`enctype` ya lo maneja Django admin)
- Crear superusuario

**Resultado esperado:** admin completamente funcional con filtros, búsqueda y carga de imágenes.

---

### Parte 3 — Autenticación (registro, login, logout) ✅
**Rama:** `feature/parte-3-auth` · **Merge:** `e6780cd`
**Depende de:** Parte 1 mergeada en develop

**Qué hacer:**
- App `usuarios/`: vista FBV de registro con `UserCreationForm` extendido para `CustomUser`
- Auto-login después del registro (patrón todo-profe: `login(request, user)` tras `form.save()`)
- URL `accounts/` → `django.contrib.auth.urls` (login/logout incluidos)
- URL `accounts/register/` → vista propia
- Templates: `registration/login.html`, `registration/register.html` con estilos Tailwind
- Settings: `LOGIN_URL`, `LOGIN_REDIRECT_URL = '/'`, `LOGOUT_REDIRECT_URL = '/'`
- Logout mediante POST en navbar (botón con form, patrón django-gym)

**Resultado esperado:** flujo completo de registro, login y logout navegable desde templates.

---

### Parte 4 — CRUD de Vino y Bodega ✅
**Ramas:** `feature/parte-4-crud-vinos` · `feature/parte-4-crud-bodegas` · **Merge:** `dc166c8` / `e7fd0cd`
**Depende de:** Partes 1 y 3 mergeadas en develop

**Vinos** — FBV siguiendo el patrón GET/POST de django-gym:
- `lista_vinos` → `GET /vinos/`
- `detalle_vino` → `GET /vinos/<int:pk>/`
- `crear_vino` → `GET/POST /vinos/crear/`
- `editar_vino` → `GET/POST /vinos/editar/<int:pk>/`
- `eliminar_vino` → `GET/POST /vinos/eliminar/<int:pk>/`

**Bodegas** — ídem estructura:
- `lista_bodegas`, `detalle_bodega`, `crear_bodega`, `editar_bodega`, `eliminar_bodega`

**Forms:**
- `VinoForm(ModelForm)` con `fields` explícitos, `enctype="multipart/form-data"` en template
- `BodegaForm(ModelForm)` ídem

**Templates:** campos renderizados manualmente (`{{ field }}` con `{{ field.errors }}`), estilos Tailwind.

**Resultado esperado:** dos CRUDs completos navegables desde el browser.

---

### Parte 5 — Permisos y grupos ✅
**Rama:** `feature/parte-5-permisos`
**Depende de:** Partes 3 y 4 mergeadas en develop

**Qué hacer:**
- Crear grupos en el admin: `Administradores` y `Empleados`
  - `Administradores`: todos los permisos sobre Vino, Bodega, Proveedor, Compra
  - `Empleados`: solo `view` y `add` sobre Vino y Compra
- Proteger vistas con decoradores (patrón todo-profe):
  ```python
  @login_required
  @permission_required('vinoteca.add_vino', raise_exception=True)
  def crear_vino(request): ...
  ```
- Vistas de listado y detalle: solo `@login_required`
- Templates: mostrar/ocultar botones según permisos:
  ```html
  {% if perms.vinoteca.change_vino %}
    <a href="...">Editar</a>
  {% endif %}
  ```

**Resultado esperado:** CRUD protegido por permisos de grupo; usuarios sin permiso ven 403.

**Implementado en:** commit `c308402` con migración `0002_crear_grupos_permisos.py`, decoradores de permisos en views.py y condicionales de permisos en templates.

---

### Parte 6 — Context processor ✅
**Rama:** `feature/parte-6-context-processor` · **Merge:** `dcf2c2d`
**Depende de:** Parte 1 mergeada en develop

**Qué hacer:**
- Crear `vinoteca/context_processors.py` con al menos un processor propio:
  ```python
  def datos_vinoteca(request):
      return {
          'nombre_vinoteca': 'La Gran Vinoteca',
          'vinos_destacados': Vino.objects.filter(stock__gt=0).order_by('-id')[:3],
          'total_vinos': Vino.objects.count(),
      }
  ```
- Registrarlo en `settings.py` dentro de `TEMPLATES['OPTIONS']['context_processors']`
- Usar las variables en `base.html` (nombre en navbar, vinos destacados en sidebar o footer)

**Resultado esperado:** datos globales disponibles en todos los templates sin pasarlos manualmente.

---

### Parte 7 — Templates y estilos con Tailwind 🔶
**Rama:** `feature/parte-7-templates` (opcional — la mayor parte ya está en develop)
**Depende de:** Partes 3, 4 y 6 mergeadas en develop

**Hecho:** `base.html` con Tailwind CDN y navbar, templates CRUD y auth estilizados, imágenes en listados/detalle, `MEDIA_URL` en `urls.py`.

**Falta:** revisión final de consistencia visual y rama dedicada si el profe la exige por separado.

**Qué hacer:**
- `vinoteca/templates/vinoteca/base.html`:
  - Tailwind via Play CDN: `<script src="https://cdn.tailwindcss.com"></script>`
  - Navbar con logo/nombre, links a vinos y bodegas, login/logout condicional
  - Bloques `title` y `content`
  - Footer con nombre de la vinoteca (desde context processor)
- Completar y estilizar todos los templates de las partes anteriores
- Template de inicio `home.html` con vinos destacados (desde context processor)
- Verificar visualización de imágenes de vinos y bodegas en templates
- Asegurarse que `MEDIA_URL` esté configurado en `urls.py` para desarrollo:
  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

**Resultado esperado:** sistema completamente navegable con diseño consistente en Tailwind.

---

### Parte 8 — README y entrega final ⏳
**Rama:** `feature/parte-8-readme`
**Depende de:** Todo mergeado en develop y funcionando

**Qué hacer:**
- Correr el proyecto localmente y tomar capturas de:
  - Home / página principal
  - Lista y detalle de vinos
  - Formulario de creación/edición
  - Panel de admin
  - Login y registro
  - Vista con permisos (botones que aparecen/desaparecen)
- Escribir `README.md` con:
  - Descripción del sistema
  - Lista de modelos y sus relaciones
  - Instrucciones para clonar y correr el proyecto (migraciones, superusuario, `.env`)
  - Capturas del proyecto en funcionamiento
- Hacer merge de `feature/parte-8-readme` → `develop` → `main`
- Verificar checklist final (ver abajo)

**Estado actual:** Parte 5 (permisos y grupos) ya está implementada en `develop` (commit `c308402`). Solo queda implementar Parte 8 (README y entrega).

---

## Checklist final antes de entregar

### Base de datos
- [x] Al menos 6 modelos (`Usuario`, `Bodega`, `Varietal`, `Categoria`, `Vino`, `Proveedor`, `Compra`, `ItemCompra`)
- [x] Relaciones entre modelos (FK y M2M)
- [x] Al menos 1 `ImageField` (en `Vino` y en `Bodega`)

### Usuarios
- [x] `CustomUser` con `AbstractUser`
- [x] Registro desde template
- [x] Login y logout desde templates

### Vistas
- [x] Navegación completa por el sistema
- [x] CRUD completo de `Vino` (5 vistas)
- [x] CRUD completo de `Bodega` (5 vistas)
- [x] Control total desde el panel de admin con filtros, ordenamiento y búsqueda

### Permisos
- [x] Al menos 2 grupos de usuarios con permisos diferenciados
- [x] Vistas de create/update/delete protegidas con `@permission_required`
- [x] Vistas de read protegidas con `@login_required`

### Otros
- [x] Al menos 1 context processor propio en uso
- [x] Carga de imágenes funcional (admin y formularios)
- [x] Estilos con Tailwind CSS aplicados consistentemente

### Entrega
- [ ] Repositorio en GitHub en rama `main` (rama `develop` actualizada en remoto)
- [ ] `README.md` con capturas del proyecto funcionando
- [ ] Fecha límite: **miércoles 24 de junio de 2026**

**Estado actual:** ✅ Parte 5 completada (permisos y grupos)
⏳ Parte 8 pendiente (README y entrega final)

---

## Setup inicial del repositorio (una sola vez)

```bash
# Un integrante crea el repo en GitHub y lo inicializa
git init
git add .
git commit -m "chore: setup inicial del proyecto"
git branch -M main
git remote add origin https://github.com/usuario/vinoteca-django.git
git push -u origin main

# Crear rama develop desde main
git checkout -b develop
git push origin develop

# El otro integrante clona y configura
git clone https://github.com/usuario/vinoteca-django.git
cd vinoteca-django
git checkout develop
```