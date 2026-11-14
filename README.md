# Gitflow en español para Claude Code y Codex

Una skill compartida para trabajar con GitHub: ramas con prefijos convencionales, commits y PR explicados en español, promociones entre entornos y correcciones urgentes.

**Todo PR hacia `dev`, `qa` o `main` necesita una aprobación de otra persona.** No se permite push directo, force push ni eliminar estas ramas. La skill guía al agente incluso si el repositorio no tiene protecciones; no puede impedir que una persona u otra herramienta incumpla el flujo. No configura reglas de GitHub ni sustituye la revisión técnica.

## Flujo del equipo

| Trabajo | Origen → destino | Aprobaciones |
|---|---|---:|
| Funcionalidad, corrección u otro cambio | Rama de trabajo desde `dev` → `dev` | 1 |
| Promoción a pruebas | `dev` → `qa` | 1 |
| Promoción a producción | `qa` → `main` | 1 |
| Urgencia | `hotfix/...` desde `main` → `main` | 1 |
| Propagación de urgencia | Rama independiente desde cada destino → `dev` y `qa` | 1 por PR |

Las promociones incorporan todos los cambios pendientes del origen. Los merges conservan el historial mediante merge commit. La propagación de hotfix incorpora únicamente la corrección. Se respetan nombres existentes como `DEV`, `QA` y `Main` cuando su equivalencia esté clara; si faltan ramas, se consulta antes de crearlas.

## Requisitos

- Claude Code o Codex con soporte de skills locales y acceso al repositorio de trabajo.
- Git para trabajar con ramas y commits.
- Para operar en GitHub: una integración con permisos suficientes o [GitHub CLI](https://cli.github.com/) autenticado mediante `gh auth login`. Verifica la cuenta con `gh auth status`.
- Otra persona con acceso suficiente al repositorio para revisar y aprobar los PR.

Sin acceso a GitHub, el agente puede preparar cambios y textos, pero no verificar aprobaciones ni afirmar que publicó un PR. La skill no instala dependencias ni concede permisos.

## Instalación

Clona este repositorio en una carpeta de herramientas. En los ejemplos se usa una carpeta `gitflow-es` recién clonada; ejecuta las copias desde su raíz, donde están este README y la subcarpeta `gitflow-es/`.

```shell
git clone https://github.com/Danieloid3/gitflow-es.git
cd gitflow-es
```

Instala **la subcarpeta que contiene `SKILL.md`**, no el repositorio completo. Elige instalación global o por proyecto para evitar duplicados. Si ya existe una skill con este nombre, revisa y conserva tus cambios antes de reemplazarla.

### Global en Windows (PowerShell)

```powershell
# Codex
New-Item -ItemType Directory -Force -Path "$HOME/.agents/skills" | Out-Null
Copy-Item -LiteralPath ./gitflow-es -Destination "$HOME/.agents/skills/gitflow-es" -Recurse

# Claude Code
New-Item -ItemType Directory -Force -Path "$HOME/.claude/skills" | Out-Null
Copy-Item -LiteralPath ./gitflow-es -Destination "$HOME/.claude/skills/gitflow-es" -Recurse
```

### Global en macOS o Linux

```bash
mkdir -p ~/.agents/skills ~/.claude/skills
cp -R ./gitflow-es ~/.agents/skills/gitflow-es
cp -R ./gitflow-es ~/.claude/skills/gitflow-es
```

Los comandos anteriores suponen que la carpeta de destino `gitflow-es` todavía no existe. No los repitas sobre una instalación existente: podrían crear una carpeta anidada.

### Por repositorio, para todo el equipo

Desde la raíz del proyecto que usará la skill, copia la carpeta del paquete a estas ubicaciones:

| Agente | Ubicación del archivo de entrada |
|---|---|
| Codex | `.agents/skills/gitflow-es/SKILL.md` |
| Claude Code | `.claude/skills/gitflow-es/SKILL.md` |

Copia también `references/` en cada instalación. Puedes incluir ambas ubicaciones en el mismo proyecto; conserva idéntico su contenido. Incorpora la instalación mediante una rama `docs/instalar-gitflow` y un PR con una aprobación. Si el proyecto aún no tiene las ramas del flujo, acuerda primero su inicialización con el equipo; esta skill no crea ni renombra ramas permanentes por su cuenta.

La instalación global afecta a tus proyectos locales; la instalación por repositorio se comparte cuando el equipo obtiene esos archivos. No instala automáticamente la skill en otros equipos.

### Comprobar la instalación

- **Codex:** menciona `$gitflow-es` en el selector de skills o en la petición.
- **Claude Code:** invoca `/gitflow-es`.
- En ambos, solicita: «Explica el flujo de esta skill, sin modificar archivos ni publicar nada». Debe indicar una aprobación para dev, qa y main, la ruta de hotfix y la prohibición de push directo.
- Si no aparece, comprueba que no haya carpetas duplicadas, que `SKILL.md` conserve su nombre y que estén las referencias. Reinicia la sesión si hace falta.

La descripción permite activación automática cuando el agente la considera relevante. Para asegurar su uso en un encargo concreto, invócala explícitamente. Las instrucciones cargadas no son una protección del servidor.

## Uso diario

En Codex comienza la petición con `$gitflow-es`; en Claude Code usa `/gitflow-es` seguido de la petición. Ejemplos del texto del encargo:

| Necesidad | Petición |
|---|---|
| Iniciar una funcionalidad | «Implementa pagos parciales siguiendo el flujo. Prepara los cambios locales; todavía no publiques». |
| Corregir un error | «Corrige el cálculo del total. Crea una rama desde dev y valida el cambio». |
| Publicar el trabajo | «Haz los commits de este encargo, publica la rama y abre el PR hacia dev con una explicación completa. No lo fusiones». |
| Promover a QA | «Abre el PR de dev a qa y resume todas las funcionalidades y correcciones incluidas». |
| Promover a producción | «Abre el PR de qa a main con impacto y validaciones». |
| Fusionar un PR revisado | «Fusiona el PR #123 si tiene una aprobación humana vigente para el HEAD actual y cumple las demás condiciones de la skill». |
| Atender una urgencia | «Corrige el acceso en producción desde main y abre un PR de hotfix. Después del merge, prepara los PR de propagación a dev y qa». |

Publicar un PR no implica permiso para fusionarlo. El agente puede continuar acciones ya autorizadas sin pedir confirmación repetida, pero no inicia promociones a otros destinos por su cuenta. Si una aprobación falta, deja el PR pendiente e informa qué necesita.

### Cómo obtener la aprobación

Comparte el enlace del PR con un compañero con permisos de revisión. Esa persona abre **Files changed → Review changes → Approve** en GitHub. La aprobación debe ser de alguien distinto del autor y de quien hizo el último cambio revisable. No cuenta un comentario «aprobado», un bot ni una evaluación generada por el agente.

Si se publican nuevos commits, pide una nueva aprobación para el HEAD actualizado aunque GitHub conserve la anterior. Antes del merge, el agente comprueba también conflictos, solicitudes de cambios, conversaciones pendientes y comprobaciones exigidas por el proyecto. Sin otra persona disponible, el PR permanece abierto; no hay excepción para dev ni para urgencias.

### Convenciones y PR

- Rama: `feat/pagos-parciales` o `fix/calculo-del-total`.
- Commit: `feat(pagos): agregar pagos parciales`.
- PR: explica el problema, resultado, cambios, pruebas reales y pendientes, además de impacto y evidencias cuando apliquen.

Consulta [todas las convenciones](gitflow-es/references/convenciones.md), la [plantilla de PR](gitflow-es/references/plantilla-pr.md) y el [procedimiento de hotfix](gitflow-es/references/hotfix.md). Son referencias para el agente; no se copian automáticamente a `.github`.

## Actualización y desinstalación

1. En tu clon de esta herramienta, ejecuta `git pull --ff-only` y revisa los cambios.
2. Si personalizaste la copia instalada, guarda esas modificaciones por separado. Renombra la carpeta instalada `gitflow-es` y muévela fuera de cualquier directorio de skills como respaldo.
3. Copia la carpeta nueva siguiendo la instalación inicial y verifica su carga. Actualiza ambas copias si usas ambos agentes.
4. Para desinstalar, elimina únicamente la carpeta `gitflow-es` de la ubicación elegida y reinicia la sesión. En instalaciones por repositorio, entrega la eliminación mediante PR.

Mover el respaldo fuera de los directorios de skills evita que el agente descubra dos versiones con el mismo nombre. No se incluyen instaladores que borren carpetas ni modifiquen la configuración personal.

## Problemas habituales

| Situación | Qué hacer |
|---|---|
| No hay autenticación o permisos | Autenticar la cuenta correcta o pedir acceso; el agente entrega lo preparado y señala lo pendiente. |
| GitHub permite merge sin revisión | Mantener el PR pendiente: la política del agente exige igualmente una aprobación humana. |
| Solo se permite squash o rebase | Resolver la incompatibilidad con el responsable del proyecto; el agente no modifica la configuración. |
| Hay cambios locales ajenos | Separarlos de forma segura o usar un entorno aislado; no descartarlos ni incluirlos en el commit. |
| Hay conflictos o cambió el HEAD | Resolver en una rama de trabajo, validar y obtener nueva aprobación. |
| Ya existe un PR | Reutilizar el PR abierto del mismo origen y destino, comprobando su contenido. |

## Compatibilidad y validación

El paquete usa `name`, `description`, Markdown y referencias relativas compartidas por ambos agentes; no requiere MCP ni extensiones exclusivas. La misma carpeta se distribuye a las dos ubicaciones. Consulta el [registro de validación](VALIDACION.md) para distinguir comprobaciones ejecutadas de las que requieren sesiones interactivas y un revisor real.

Fuentes: [skills de Codex](https://learn.chatgpt.com/docs/build-skills), [skills de Claude Code](https://code.claude.com/docs/en/skills), [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/) y [protecciones de GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
