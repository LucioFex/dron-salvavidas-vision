# dron-salvavidas-vision

Detección de ahogamientos con visión artificial para un dron salvavidas autónomo. Corre en una
laptop sin internet y le da órdenes al dron por MAVLink.

> Prototipo experimental en desarrollo. No es un equipo de rescate certificado y no reemplaza a
> un guardavidas. Cualquier prueba con personas se hace con guardavidas presentes y un piloto de
> seguridad que puede tomar el control del dron.

## La idea

En las playas de la Costa Atlántica argentina, una persona que se ahoga casi nunca pide ayuda. Queda
vertical, con la boca al ras del agua, y en menos de un minuto puede hundirse. El guardavidas tiene
que verla, bajar de la torre, correr y nadar.

El sistema mira el mar con una cámara fija. Cuando detecta a alguien con el patrón de ahogamiento,
manda un dron chico que vuela solo hasta la persona y le suelta un flotador autoinflable. El
guardavidas sale igual al rescate desde el primer segundo, con su tabla o su torpedo. El dron solo
llega antes y mantiene a la persona a flote hasta que él llega.

## Qué hace este repo

Es el "cerebro" del sistema, en Python:

| Módulo | Qué hace |
|---|---|
| `ojo` | Lee el video de la cámara fija (en el prototipo, un iPhone usado como webcam) |
| `deteccion` | Encuentra a las personas que están en el agua |
| `seguimiento` | Sigue a cada persona en el tiempo y calcula la probabilidad de que se esté ahogando |
| `ubicacion` | Pasa la posición en la imagen a una coordenada GPS, con la cámara calibrada |
| `estados` | Decide qué hacer: despegar, esperar la botonera, soltar el flotador o volver |
| `piloto` | Le manda los comandos al dron (ArduPilot) por MAVLink |
| `botonera` | Habla por cable con la botonera del guardavidas |

## Cómo decide

1. Si la probabilidad de ahogamiento pasa un umbral, el dron despega solo y la botonera de la torre
   empieza a sonar.
2. El dron vuela hasta la persona y se queda encima con luz y sirena, que le marcan al guardavidas
   dónde está.
3. En la botonera hay dos botones. "Incidente real" suelta el flotador en el momento y "Falso
   positivo" manda al dron de vuelta a la base.
4. Si nadie toca nada y la probabilidad sigue alta, el dron suelta el flotador al terminar una
   cuenta regresiva. Lo más probable es que el guardavidas ya haya salido corriendo.

Hay un modo 100% automático que suelta sin esperar a nadie. Es experimental y puede tirarle el
flotador a alguien que estaba bien.

Todo corre local, sin internet. La decisión de soltar la toma una máquina de estados con reglas
fijas, y ningún modelo de lenguaje interviene en ella.

## Estado

En diseño. Todavía no hay código funcional. La estructura de módulos ya está armada.

## Repos del proyecto

- [dron-salvavidas-vision](https://github.com/LucioFex/dron-salvavidas-vision): detección y lógica de decisión (este repo)
- [dron-salvavidas-firmware](https://github.com/LucioFex/dron-salvavidas-firmware): botonera ESP32 y configuración de ArduPilot
- [dron-salvavidas-hardware](https://github.com/LucioFex/dron-salvavidas-hardware): modelos 3D y lista de materiales

## Desarrollo

```bash
python -m venv .venv
source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

## Licencia

[Apache-2.0](LICENSE). Copyright 2026 Luciano Esteban y Elías Espinosa.

## Autores

- Luciano Esteban ([@LucioFex](https://github.com/LucioFex))
- Elías Espinosa
