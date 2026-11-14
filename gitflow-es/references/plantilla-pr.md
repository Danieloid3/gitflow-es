# Plantilla para redactar PR

Completa con hechos del diff y pruebas reales. Adapta o elimina apartados opcionales; nunca dejes instrucciones o marcadores sin completar. Si no hubo pruebas, explica por qué y qué falta. No pegues secretos ni datos personales en evidencias.

```markdown
## Necesidad y resultado
Explicar el problema, a quién afecta y cómo se comporta ahora el sistema.

## Cambios realizados
Describir los cambios principales y el motivo de las decisiones relevantes.
Para promociones, agrupar las funcionalidades y correcciones incluidas y enlazar sus PR.

## Validación
Indicar comprobaciones ejecutadas y resultados observados.
Separar pruebas pendientes, limitaciones y pasos de comprobación manual.

## Impacto y puesta en marcha
Cuando aplique: compatibilidad, riesgos, migraciones, configuración y recuperación.

## Referencias y evidencias
Cuando aplique: issues, PR relacionados y capturas de los cambios visuales.
```

En un hotfix explica además el incidente, el alcance de la corrección y el estado de propagación hacia `dev` y `qa`. Actualiza los enlaces y estados cuando los PR existan.
