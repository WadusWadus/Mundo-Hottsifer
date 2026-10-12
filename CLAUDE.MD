# Dianapp

Wiki de personajes y lore. Django 5.2 LTS + PostgreSQL. Proyecto de aprendizaje:
el objetivo es que yo entienda el código, no que esté terminado rápido.

## Entorno

- MACOS, venv en `.venv/` (actívalo antes de cualquier comando)
- Dependencias en `requirements.txt` y `requirements-dev.txt`
- Variables en `.env` (plantilla en `.env.example`), nunca hardcodear secretos
- Comandos con `python manage.py ...` desde la raíz

## Decisiones cerradas — no proponer alternativas

- `accounts.User(AbstractUser)` con `AUTH_USER_MODEL` definido antes de la
  primera migración, aunque hoy no agregue campos
- Permisos vía `is_staff` y grupo `moderadores`. Sin enum de roles propio
- `ImageField` + Pillow. `MEDIA_ROOT` separado de `STATIC_ROOT`
- Templates namespaceados: `<app>/templates/<app>/...`
- psycopg 3, no psycopg2
- Tailwind por CDN mientras dure el MVP
- Dominio de producción: hotssifer.elgs.me

## Estado actual

Estructura base creada (proyecto `dianapp`, apps `accounts` y `characters`),
dependencias instaladas, git inicializado. Falta todo lo demás.

## Fase actual: rebanada vertical mínima

Que un personaje publicado se vea en el navegador. En orden:

1. `settings.py` leyendo SECRET_KEY, DEBUG, ALLOWED_HOSTS y conexión a
   PostgreSQL desde `.env`
2. Modelo `User` vacío + `AUTH_USER_MODEL` + primera migración
3. Modelo `Character`: slug, name, description, lore, image, status
   (`TextChoices`), author (FK), created_at, updated_at
4. Vista de lista y de detalle, con templates y `base.html`
5. Registro en `admin.py` para cargar datos de prueba

Fuera de alcance: tags, favoritos, enlaces entre personajes, panel de
moderación, registro de usuarios, contadores, deployment.

## Cómo quiero trabajar

- Un paso a la vez, deteniéndote a esperar mi confirmación
- Explica qué decisión estás tomando y por qué antes de escribir código
- Si algo que pido es técnicamente incorrecto, dímelo en vez de implementarlo
- No agregues features que no estén en la fase actual
