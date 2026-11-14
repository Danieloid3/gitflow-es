---
name: gitflow-es
description: Sigue el Gitflow del equipo en GitHub al crear ramas, commits, PR, promociones entre dev, qa y main o hotfix. Exige PR y una aprobación externa para toda entrada a ramas permanentes; redacta en español. Úsala también al iniciar cambios de código que deban seguir este flujo. No configura protecciones ni sustituye una revisión técnica.
---

# Gitflow en español

## Alcance y preparación

Aplica estas instrucciones al trabajo solicitado; cargar la skill no autoriza publicar, fusionar ni desplegar. No pidas de nuevo permisos ya otorgados. Crear un PR no autoriza fusionarlo. Una promoción requiere que la petición incluya el destino; no encadenes promociones por iniciativa propia.

Antes de modificar: lee las instrucciones del repositorio, comprueba `git status`, remotos, rama actual y ramas remotas actualizadas. Identifica las equivalencias de `dev`, `qa` y `main` por documentación y referencias existentes, respetando mayúsculas. No supongas que la rama predeterminada representa producción. Si faltan ramas o hay varias equivalencias plausibles, consulta antes de crearlas o elegirlas. Si una regla local contradice este flujo, expón el conflicto antes de la operación afectada.

Preserva los cambios ajenos: no hagas reset destructivo, stash automático ni commits de archivos fuera del encargo. Si ya estás en una rama permanente con cambios propios sin commit, pásalos a una rama de trabajo sin perderlos; si no puedes separar cambios con seguridad, detén solo esa operación y explica lo necesario.

Usa Git y una integración de GitHub disponible, o `gh` autenticado. Si falta acceso, prepara ramas, mensajes o el texto del PR hasta donde sea posible, e informa exactamente qué no ejecutaste. Nunca inventes aprobaciones, pruebas ni enlaces.

## Rutas permitidas

| Trabajo | Rama de origen | PR hacia | Aprobaciones externas |
|---|---|---|---:|
| Cambio habitual | `<tipo>/<descripcion>` desde `dev` | `dev` | 1 |
| Promoción a pruebas | `dev` | `qa` | 1 |
| Promoción a producción | `qa` | `main` | 1 |
| Urgencia en producción | `hotfix/<descripcion>` desde `main` | `main` | 1 |
| Propagar urgencia | `fix/<descripcion>` desde cada destino | `dev` y `qa`, por separado | 1 por PR |

No hagas push directo, force push ni elimines ninguna de las tres ramas permanentes. No eludas el flujo aunque GitHub lo permita o se solicite un atajo: prepara el PR correspondiente. No cambies reglas de GitHub, revisores ni Actions como consecuencia de usar esta skill.

Publica solo ramas de trabajo cuando esté autorizado. Antes de abrir un PR, busca uno abierto con el mismo origen y destino: actualízalo si corresponde. Si ya fue fusionado o cerrado, comprueba los cambios pendientes antes de crear otro. No promociones si no hay diferencias reales.

Las promociones incluyen todos los cambios pendientes del origen. Explica su alcance antes de publicar si incluye trabajo adicional al pedido. No selecciones funcionalidades mediante cherry-pick para una promoción ordinaria.

## Ramas, commits y PR

Lee [convenciones.md](references/convenciones.md) para nombres y mensajes. Forma commits coherentes solo con los cambios del encargo y ejecuta las comprobaciones pertinentes del proyecto. No instales validadores ni hooks por usar esta skill.

Redacta el título y cuerpo del PR en español usando [plantilla-pr.md](references/plantilla-pr.md). Describe necesidad, comportamiento resultante, cambios, motivo, evidencia de pruebas y pendientes. Incluye impacto, riesgos, migraciones y capturas cuando apliquen. La amplitud debe permitir comprender el cambio sin leer el chat; evita relleno y secciones vacías. En promociones agrupa funcionalidades y correcciones incluidas, enlazando los PR cuando estén disponibles.

## Condición obligatoria antes de cualquier merge

Solo fusiona si está autorizado y se cumplen **todas** estas condiciones en GitHub, incluso sin protecciones:

1. Origen y destino corresponden a una ruta permitida; el PR está abierto y listo, no en borrador.
2. Existe al menos una aprobación humana válida de alguien distinto del autor del PR y de quien realizó el último cambio revisable. Una revisión escrita por este agente, un bot, una revisión pendiente o descartada no cuenta.
3. La aprobación corresponde al HEAD actual. Si llegan commits después, solicita nueva aprobación; si no puedes verificar la correspondencia, no fusiones. No basta con comprobar que existe algún evento histórico `APPROVED`: examina el estado vigente de cada revisor, los cambios solicitados y las conversaciones pendientes.
4. No quedan solicitudes de cambios ni conversaciones sin resolver. Las comprobaciones exigidas por el repositorio terminan satisfactoriamente. La ausencia de CI no obliga a crearlo: registra las validaciones ejecutadas y sus límites.
5. No hay conflictos. El método de merge commit está permitido. Si solo se permite squash o rebase, informa la incompatibilidad; no modifiques la configuración ni cambies el método silenciosamente.

Vuelve a consultar el estado inmediatamente antes de fusionar. Vincula la operación al SHA de origen verificado (por ejemplo, `gh pr merge --merge --match-head-commit <sha>`) y no uses `--admin`, auto-merge ni mecanismos de bypass. Si el estado cambia o falla una condición, deja el PR pendiente con la causa concreta. No borres `dev`, `qa` ni `main` tras un merge.

Resuelve conflictos en una rama de trabajo y por PR. Nunca resuelvas una promoción haciendo un merge local y push a su destino. Si necesitas una rama auxiliar para reparar el origen, haz primero un PR de reparación hacia ese origen con una aprobación y después revalida la promoción.

## Hotfix y propagación

Lee [hotfix.md](references/hotfix.md) para urgencias. Un hotfix no omite aprobación ni PR. Después de integrarlo en producción, propaga únicamente la corrección mediante PR independientes hacia `dev` y `qa`. No mezcles todo `main` en estos destinos ni des por terminada la propagación al abrir los PR: informa si están pendientes de aprobación o merge.

## Entrega

Informa rama y destino, commits o PR creados, validaciones reales, aprobación y estado de merge. Distingue acciones completadas de propuestas o pendientes. Sin acceso a GitHub no afirmes haber comprobado revisores ni publicado nada. Esta skill guía al agente; no impide operaciones de otros colaboradores ni realiza una revisión técnica especializada.
