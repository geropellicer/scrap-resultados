# Instalación

## Prerequisitos
- Tener instalado pipenv o en su defecto usar el env por defecto de Python

## Instalación
- Clonar el repo
- `cd scrap-resultados`
- `pipenv install`
- `pipenv shell`

# Uso

- Con la shell activa (último paso de instalación): `bpython`

## Por municipio:
- Con bpython activo: `from app.main import scrap_municipio`
- `scrap_municipio(<PROV>, <MUN>, mesa_inicial=<MESA_INI (opcional)>, mesa_final=<MESA_FINAL (opcional)>)`

## Por provincia:
- Con bpython activo: `from app.main import scrap_provincia`
- `scrap_provincia(<PROV>)`

### Importante
- Antes de arrancar, asegurarse que en `app/settings.py` estan los codigos de la provincia que nos interesa en `codigos_fitu_partido`, `codigos_lista_pts` y `codigos_lista_mst`.
- Si se cambia algo del codigo, hay que salir de bpython, volver a entrar, volver a importar y volver a correr.
- En el caso de provincia igual va a generar un resultado por municipio, pero es tipo backup. Al final generara toda la provincia.

