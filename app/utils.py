from .settings import BASE_URL


def get_codigo_mesa(num_mesa: int, prov_id: int, mun_id: int):
    prov_code = get_prov_code(prov_id)
    mun_code = get_mun_code(mun_id)
    mesa_code = get_mesa_code(num_mesa)
    return prov_code + mun_code + mesa_code


def get_url_final(codigo_mesa: str, categoria=3):
    return "{}/{}/{}".format(BASE_URL, codigo_mesa, categoria)


def get_prov_code(prov_id: int):
    if len(str(prov_id)) < 2:
        return "0{}".format(prov_id)
    else:
        return str(prov_id)


def get_mun_code(mun_id: int):
    length = len(str(mun_id))
    anteposition = ""
    for i in range(length, 3):
        anteposition += "0"
    return anteposition + str(mun_id)


def get_mesa_code(num_mesa: int):
    length = len(str(num_mesa))
    anteposition = ""
    for i in range(length, 5):
        anteposition += "0"
    return anteposition + str(num_mesa) + "X"


def find_in_array(array, key, value):
    return [pdict for pdict in array if pdict[key] == value][0]
