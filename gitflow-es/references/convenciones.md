# Convenciones

## Ramas

Formato: `<tipo>/<descripcion-en-espanol>`. Usa minúsculas, guiones, sin espacios ni tildes. Conserva identificadores de issues solo si existen; no inventes números. No renombres ramas permanentes existentes.

| Tipo | Uso | Ejemplo |
|---|---|---|
| feat | Funcionalidad | `feat/pagos-parciales` |
| fix | Corrección | `fix/calculo-del-total` |
| docs | Documentación | `docs/guia-de-instalacion` |
| refactor | Reorganización sin cambio funcional | `refactor/validacion-de-pedidos` |
| test | Pruebas | `test/descuentos-acumulados` |
| chore | Mantenimiento | `chore/actualizar-dependencias` |
| ci | Integración continua | `ci/verificar-compilacion` |
| build | Compilación y empaquetado | `build/ajustar-empaquetado` |
| perf | Rendimiento | `perf/optimizar-consulta` |
| revert | Reversión | `revert/pagos-parciales` |
| hotfix | Urgencia desde producción | `hotfix/error-al-iniciar-sesion` |

## Commits

Sigue [Conventional Commits 1.0.0](https://www.conventionalcommits.org/es/v1.0.0/): `<tipo>(<ambito-opcional>): <descripcion>`. Tipos iguales a los anteriores salvo `hotfix`: una urgencia usa normalmente `fix` en el commit.

Escribe el ámbito y la explicación en español, salvo nombres técnicos reales. Usa una primera línea breve que exprese una acción concreta, por ejemplo:

```text
feat(pagos): agregar pagos parciales
fix(pedidos): corregir el cálculo del descuento
docs: explicar la instalación para el equipo
```

Separa el cuerpo con una línea vacía cuando haga falta explicar el motivo o las consecuencias. Para incompatibilidades usa `!` y explica el cambio y la adaptación en español bajo el marcador estándar:

```text
feat(api)!: exigir el identificador del cliente

BREAKING CHANGE: las solicitudes deben incluir cliente_id; adaptar las integraciones existentes.
```

No reescribas commits compartidos o ajenos para adaptar mensajes. El agente controla los mensajes que crea; los mensajes automáticos de GitHub pueden depender de la plataforma.

## Títulos de PR

Usa la misma convención para cambios habituales. Para promociones: `chore(promocion): promover dev a qa` o `chore(promocion): promover qa a main`, sustituyendo los nombres por los reales. Para una urgencia: `fix(sesion): corregir el acceso en producción`.
