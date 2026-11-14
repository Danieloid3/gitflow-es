# Registro de validación

## Comprobaciones reproducibles

La versión inicial pasó el validador `quick_validate.py` de skill-creator y `git diff --check`, además de las pruebas temporales siguientes.

Ejecutar `python tests/validate.py` desde la raíz del repositorio. Requiere Python 3 y Git, no usa red y elimina su repositorio temporal al terminar.

- Comprueba la entrada del paquete y los enlaces locales de la documentación.
- Ensaya una funcionalidad y las promociones dev → qa → main con commits de merge y conservación de ancestros.
- Ensaya un hotfix y su traslado selectivo a dev y qa, comprobando que no arrastre otro cambio exclusivo de producción.

Estas pruebas comprueban la topología y los archivos; las fusiones locales del entorno temporal no prueban aprobaciones ni el comportamiento de un modelo.

## Revisión de escenarios de las instrucciones

Revisión documental realizada sobre la versión inicial, sin operaciones en proyectos del equipo:

| Escenario | Resultado prescrito |
|---|---|
| PR hacia dev, qa o main sin aprobación | Dejar pendiente, incluso sin protección del servidor. |
| Aprobación propia, de bot, descartada o anterior al HEAD | No fusionar; obtener aprobación humana vigente. |
| Se solicita push directo o bypass | Preparar PR por la ruta permitida. |
| PR abierto del mismo origen y destino | Reutilizarlo tras comprobar el contenido. |
| Cambios ajenos o conflicto | Preservarlos; resolver en rama de trabajo o explicar el impedimento. |
| No hay autenticación o permisos | Preparar lo posible y declarar lo no ejecutado. |
| Hotfix ya presente en un destino | Comprobar historial y contenido; evitar PR vacío. |
| Merge autorizado pero cambió el SHA | No fusionar un HEAD diferente del revisado. |

## Límites y prueba de aceptación del equipo

Se comprobaron las versiones locales de Claude Code y Codex y la estructura portable del paquete. No se instalaron copias globales, no se ejecutaron sesiones de inferencia de ninguno de los dos agentes y no se obtuvo una aprobación de otra persona para probar un merge real. Por tanto, el descubrimiento en sesiones nuevas y la obediencia a estos escenarios requieren aceptación interactiva; no se presentan como pruebas superadas.

Después de instalar, invocar la skill explícitamente en cada agente y pedir una explicación sin cambios. Después, en un repositorio de prueba del equipo, abrir un PR hacia dev sin aprobación: el agente debe dejarlo pendiente. Repetir con una aprobación real, autorizar el merge y verificar el SHA. Publicar otro commit después de una aprobación debe exigir una nueva. Probar las promociones y la propagación antes de adoptar la skill en proyectos activos.

La publicación inicial de este repositorio distribuye el paquete. No implica que el equipo haya aprobado un cambio de producto ni que se hayan configurado protecciones de GitHub.
