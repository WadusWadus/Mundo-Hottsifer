# Dianapp

Wiki de personajes y lore, visible solo con cuenta. Django 5.2 LTS + PostgreSQL.
Repositorio: `git@github.com:WadusWadus/Mundo-Hottsifer.git`

## Qué se quiere construir

Una wiki donde cada personaje tiene su propia página con nombre, imagen,
descripción y lore.

- Para leer hay que entrar con una cuenta; sin sesión todo redirige al
  login. Con sesión solo se ven personajes publicados
- Los autores crean personajes, que nacen como borrador
- El staff y el grupo `moderadores` revisan y publican
- Producto final: listado navegable, página de detalle por personaje,
  personajes enlazados entre sí, tags y favoritos

## Entorno

- macOS, venv en `.venv/` (actívalo antes de cualquier comando)
- PostgreSQL 18 por Homebrew: `brew services start postgresql@18`
- Base de datos y rol locales: `dianapp`
- Dependencias en `requirements.txt` y `requirements-dev.txt`
- Variables en `.env` (plantilla en `.env.example`), nunca hardcodear secretos
- Comandos con `python manage.py ...` desde la raíz

## Decisiones cerradas — no proponer alternativas

- `accounts.User(AbstractUser)` como `AUTH_USER_MODEL`
- Permisos vía `is_staff` y grupo `moderadores`. Sin enum de roles propio
- `ImageField` + Pillow. `MEDIA_ROOT` separado de `STATIC_ROOT`
- Templates namespaceados: `<app>/templates/<app>/...`
- psycopg 3, no psycopg2
- Tailwind por CDN mientras dure el MVP
- Dominio de producción: hotssifer.elgs.me

## Estado actual

Hecho:

- `settings.py` lee SECRET_KEY, DEBUG, ALLOWED_HOSTS y la conexión a
  PostgreSQL desde `.env`
- `accounts.User` vacío, `AUTH_USER_MODEL` definido y migrado
- `characters.Character` migrado: slug, name, description, lore, image,
  status (`draft` / `published`), author (FK, `PROTECT`), created_at,
  updated_at
- `MEDIA_URL` y `MEDIA_ROOT` (`media/`) configurados
- `Character` y `User` registrados en el admin; superusuario local `wadus`
- Vistas de lista (`/`) y detalle (`/personajes/<slug>/`), solo publicados
- `templates/base.html` y templates de `characters` con estructura mínima
- Nombre visible del sitio: "El mundo de Hottsifer" (header y `<title>`);
  el proyecto Django y la base siguen llamándose `dianapp`
- Detalle de personaje con la imagen grande a todo el ancho, sin recorte
  circular; el listado conserva el avatar circular pequeño
- Personaje publicado de prueba cargado (`/personajes/zapato/`)
- `media/` servido en desarrollo (`DEBUG`)
- Cuentas en `/cuenta/`: registro (`registro/`), login (`entrar/`), logout
  por POST (`salir/`) y "Mi cuenta" (`/cuenta/`, requiere login) con los
  personajes propios y su estado. El registro pide solo usuario y
  contraseña e inicia sesión al terminar
- `LOGIN_URL`, `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` definidos;
  `LANGUAGE_CODE = 'es'`
- Header con "Entrar" / "Mi cuenta" según la sesión
- Listado y detalle de personajes exigen login (`LoginRequiredMixin`); sin
  sesión, `/` redirige a `/cuenta/entrar/`
- Login con imagen principal: `static/img/login-hero.svg` (ilustración
  provisional, reemplazable). `STATICFILES_DIRS = [BASE_DIR / 'static']`
- Tests de cuentas en `accounts/tests.py` (`python manage.py test`); el rol
  local `dianapp` tiene `CREATEDB` para poder crear la base de tests

## Fase actual: cuentas de usuario

Registro, login, logout y página de cuenta. Pendiente:

1. Revisar en el navegador, en ancho de celular: listado, detalle y las
   páginas de cuenta
2. Afinar el frontend

Diseño: referencia en `imagen-referencia.jpeg` (fondo menta, tarjetas claras
en dos columnas en celular, avatar circular). Colores y fuentes definidos en
`tailwind.config` dentro de `templates/base.html`.

Fuera de alcance en esta fase: creación de personajes por autores, tags,
favoritos, enlaces entre personajes, panel de moderación, recuperación de
contraseña, email, contadores, deployment.

## Cómo trabajar

- Implementa directo: un paso completo de la fase por vez, verificado
  (`check`, migraciones, prueba en el navegador cuando aplique)
- Resume en pocas líneas las decisiones tomadas; sin tutoriales ni preguntas
  de comprensión
- Si algo que pido es técnicamente incorrecto, dilo en vez de implementarlo
- No agregues features que no estén en la fase actual
- Actualiza "Estado actual" y "Fase actual" al terminar cada paso
- No hagas commit ni push sin que lo pida
