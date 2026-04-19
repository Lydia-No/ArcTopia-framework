# ArcTopia Migration Log

This file records migrated material brought into ArcTopia-framework from earlier repositories.

## Repository migration metadata

- Migration date: 2026-04-19
- Destination repo: Lydia-No/ArcTopia-framework
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Notes: destination commit above is the final-repo baseline that received the migrated material before this provenance log was expanded to include timeline metadata.

## Format

- Source working tree:
- Source remote:
- Source path:
- Source commit SHA:
- Source commit date:
- Destination repo:
- Destination path:
- Destination commit SHA:
- Destination commit date:
- Migration date:
- Action:
- Notes:

---

## Initial migrations

### ArcTopia base files
- Source working tree: ~/symbolic-system-core/ArcTopia-sync
- Source remote: Lydia-No/ArcTopia
- Source path: backend/package.json, backend/package-lock.json, backend/server.js, backend/README.md, frontend/index.html, db/schema.sql
- Source commit SHA: fac5fa9e5c52d2b5431550b2aa682b97249d78b8
- Source commit date: 2026-03-23T22:03:34+01:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: backend/, frontend/index.html, db/schema.sql
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source working tree: ~/symbolic-system-core/ArcTopia-sync
- Source remote: Lydia-No/ArcTopia
- Source path: backend/src/engine/recognitionEngine.js
- Source commit SHA: fba35e29fe9cddb39c545c2a1af45f2eb76f9b32
- Source commit date: 2026-03-23T02:50:46+01:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: backend/src/engine/recognitionEngine.js
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source working tree: ~/symbolic-system-core/ArcTopia-sync and ~/symbolic-system-core/arctopia-core
- Source remote: Lydia-No/ArcTopia and local donor archive
- Source path: backend/src/db/index.js
- Source commit SHA: e33fc5bee76d00bcd3f90b4db099eca1d3741852 and 2f92fa7a6d33f78323c7569fca532e7c527cc39f
- Source commit date: 2026-03-23T04:12:17+01:00 and 2026-03-23T02:34:39+01:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: backend/src/db/index.js
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: merged manually
- Notes: replaced hardcoded port with PG* environment-variable configuration

### Runtime / field imports
- Source working tree: ~/field-core/field-core
- Source remote: local working tree for canonical runtime base
- Source path: backend/core/runtime.py, backend/core/intelligence.py, backend/core/autonomous.py, backend/core/agent.py, backend/core/hypercube.py, backend/core/cognition.py, backend/core/memory.py, backend/core/attractor.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Source commit date: 2026-04-01T18:52:34+02:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: runtime/field/backend/core/
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: copied
- Notes: canonical runtime dependency chain staged to satisfy the validated field API smoke path

- Source working tree: ~/the-cube
- Source remote: Lydia-No/The-cube
- Source path: packages/field-core/backend/core/math_utils.py, packages/field-core/backend/core/topology.py, packages/field-core/backend/core/timeline.py
- Source commit SHA: 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Source commit date: 2026-04-17T22:06:58+02:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: runtime/field/backend/core/
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: copied
- Notes: donor utility imports retained as a narrow runtime support layer

- Source working tree: ~/field-core/field-core and ~/the-cube
- Source remote: local canonical runtime base and Lydia-No/The-cube
- Source path: backend/api/server.py and packages/field-core/backend/api/server.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821 and 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Source commit date: 2026-04-01T18:52:34+02:00 and 2026-04-17T22:06:58+02:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: runtime/field/backend/api/server.py
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: merged manually
- Notes: kept canonical runtime endpoints and added donor /health endpoint only

- Source working tree: ~/field-core/field-core and ~/the-cube
- Source remote: local canonical runtime base and Lydia-No/The-cube
- Source path: requirements.txt and packages/field-core/requirements.txt
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821 and 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Source commit date: 2026-04-01T18:52:34+02:00 and 2026-04-17T22:06:58+02:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: runtime/field/requirements.txt
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: merged manually
- Notes: reduced to the minimal validated dependency set used by the staged runtime

### realERT imports
- Source working tree: ~/symbolic-workspace/realERT
- Source remote: Lydia-No/realERT
- Source path: src/realerts/
- Source commit SHA: 61feca1e0748a7fcdb0ce660bfa3a28c96439cf8
- Source commit date: 2026-03-23T22:03:39+01:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: apps/realert/src/realerts/
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: copied selectively
- Notes: canonical package import for realERT

- Source working tree: ~/symbolic-workspace/realERT
- Source remote: Lydia-No/realERT
- Source path: src/realerts/simulation/lineage.py and lineage.py
- Source commit SHA: ce48efa2517a6257b12e70afd1e48ffe2265a3f8 and b2c3baccd63b03b23339129278b432a4f85ee484
- Source commit date: 2026-03-14T12:29:37+01:00 and 2026-03-14T13:20:12+01:00
- Destination repo: Lydia-No/ArcTopia-framework
- Destination path: apps/realert/src/realerts/simulation/lineage.py
- Destination commit SHA: d6502fc7d9c07a7917823cb06989b911733565ef
- Destination commit date: 2026-04-19T03:30:29+02:00
- Migration date: 2026-04-19
- Action: merged manually
- Notes: kept package implementation and imported the flat-file parents() helper only
