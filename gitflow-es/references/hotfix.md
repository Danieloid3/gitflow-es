# Correcciones urgentes

1. Actualiza las referencias remotas y crea `hotfix/<descripcion>` desde el `main` real. No incluyas funcionalidades ajenas a la incidencia.
2. Valida la corrección y abre PR hacia producción con el incidente, comportamiento resultante y pruebas en español.
3. Espera una aprobación humana válida para el HEAD actual y el resto de condiciones de `SKILL.md`. Solo fusiona si la petición lo autoriza.
4. Tras el merge, identifica los commits que contienen únicamente la corrección. Para cada destino, comprueba si la corrección ya está presente por historial y contenido; no te limites a comparar SHA porque un cherry-pick cambia el identificador.
5. Para cada destino que la necesite, crea desde su última referencia remota una rama como `fix/propagar-acceso-a-dev` o `fix/propagar-acceso-a-qa`. Traslada solo los commits de corrección, por ejemplo mediante `git cherry-pick -x <sha>` de commits ordinarios, preservando su procedencia. No traslades a ciegas el commit de merge completo; si la corrección incluye merges, inspecciona el diff y adapta el parche mínimo.
6. Resuelve y valida cualquier adaptación en esa rama. Si no puedes resolver un conflicto con confianza, deja el estado explicado sin alterar el destino.
7. Abre o actualiza los dos PR y enlázalos con el original. Ambos requieren una aprobación externa vigente y autorización de merge. Si un destino ya contenía la corrección, documenta la evidencia y no abras un PR vacío.

Informa por separado producción, dev y qa: pendiente, PR abierto, fusionado o ya presente. La urgencia no permite push directo ni bypass. No fusiones automáticamente otras funcionalidades como parte de la propagación.
