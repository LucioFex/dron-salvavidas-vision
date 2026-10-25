import importlib

MODULOS = ["ojo", "deteccion", "seguimiento", "ubicacion", "estados", "piloto", "botonera"]


def test_los_modulos_se_importan():
    for nombre in MODULOS:
        importlib.import_module(f"dron_salvavidas_vision.{nombre}")
