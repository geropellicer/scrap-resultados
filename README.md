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
- Alternativamente, para traer solo los votos al FITU, PTS y MST: `scrap_municipio_fitu(<PROV>, <MUN>, mesa_inicial=<MESA_INI (opcional)>, mesa_final=<MESA_FINAL (opcional)>)`

## Por provincia:
- Con bpython activo: `from app.main import scrap_provincia`
- `scrap_provincia(<PROV>, mun_inicial=<MUN_INICIAL (opcional)>, mesa_inicial=<MESA_INICIAL (opcional)>)`
- Alternativamente, para traer solo los votos al FITU, PTS y MST: `scrap_provincia(<PROV>, mun_inicial=<MUN_INICIAL (opcional)>, mesa_inicial=<MESA_INICIAL (opcional)>, fitu=True)`

### Importante
- Si se elige la opción de traer solo lo del FITU, antes de arrancar, asegurarse que en `app/settings.py` estan los codigos de la provincia que nos interesa en `codigos_fitu_partido`, `codigos_lista_pts` y `codigos_lista_mst`.
- Tener en cuenta que los formatos entre cuando decidimos traer todos los datos o cuando decidimos traer solo lo del FITU cambia. En el primer caso genera una fila por cada lista de cada partido y por los demas datos generales de la mesa (votos en blanco, totales, nulos, etc). En el segundo caso genera una columna de voto fitu, una columna de voto mst y una de voto pts e inserta solo una fila por mesa.
- Si se cambia algo del codigo, hay que salir de bpython, volver a entrar, volver a importar y volver a correr.
- En el caso de provincia igual va a generar un resultado por municipio, pero es tipo backup. Al final generara toda la provincia.

