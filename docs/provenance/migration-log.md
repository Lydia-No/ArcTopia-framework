# ArcTopia Migration Log

This file records migrated material brought into ArcTopia from earlier repositories.

## Format

- Source repo:
- Source path:
- Source commit SHA:
- Destination path:
- Action:
- Notes:

---

## Initial migrations

### ArcTopia base files
- Source repo: Lydia-No/ArcTopia
- Source path: backend/package.json
- Source commit SHA: fac5fa9e5c52d2b5431550b2aa682b97249d78b8
- Destination path: backend/package.json
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source repo: Lydia-No/ArcTopia
- Source path: backend/package-lock.json
- Source commit SHA: fac5fa9e5c52d2b5431550b2aa682b97249d78b8
- Destination path: backend/package-lock.json
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source repo: Lydia-No/ArcTopia
- Source path: backend/server.js
- Source commit SHA: fac5fa9e5c52d2b5431550b2aa682b97249d78b8
- Destination path: backend/server.js
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source repo: Lydia-No/ArcTopia
- Source path: backend/src/engine/recognitionEngine.js
- Source commit SHA: fba35e29fe9cddb39c545c2a1af45f2eb76f9b32
- Destination path: backend/src/engine/recognitionEngine.js
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source repo: Lydia-No/ArcTopia and Lydia-No/arctopia-core
- Source path: backend/src/db/index.js
- Source commit SHA: e33fc5bee76d00bcd3f90b4db099eca1d3741852 and 2f92fa7a6d33f78323c7569fca532e7c527cc39f
- Destination path: backend/src/db/index.js
- Action: merged manually
- Notes: replaced hardcoded port with PG* environment-variable configuration

- Source repo: Lydia-No/ArcTopia
- Source path: backend/README.md
- Source commit SHA: fac5fa9e5c52d2b5431550b2aa682b97249d78b8
- Destination path: backend/README.md
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source repo: Lydia-No/ArcTopia
- Source path: frontend/index.html
- Source commit SHA: fac5fa9e5c52d2b5431550b2aa682b97249d78b8
- Destination path: frontend/index.html
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

- Source repo: Lydia-No/ArcTopia
- Source path: db/schema.sql
- Source commit SHA: fac5fa9e5c52d2b5431550b2aa682b97249d78b8
- Destination path: db/schema.sql
- Action: copied
- Notes: adopted from ArcTopia-sync canonical base

### Runtime / field imports
- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/runtime.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/runtime.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/intelligence.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/intelligence.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/autonomous.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/autonomous.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/agent.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/agent.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/hypercube.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/hypercube.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/cognition.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/cognition.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/memory.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/memory.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/hypercube-field-system
- Source path: backend/core/attractor.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821
- Destination path: runtime/field/backend/core/attractor.py
- Action: copied
- Notes: canonical runtime dependency chain

- Source repo: Lydia-No/The-cube
- Source path: packages/field-core/backend/core/math_utils.py
- Source commit SHA: 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Destination path: runtime/field/backend/core/math_utils.py
- Action: copied
- Notes: donor utility import

- Source repo: Lydia-No/The-cube
- Source path: packages/field-core/backend/core/topology.py
- Source commit SHA: 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Destination path: runtime/field/backend/core/topology.py
- Action: copied
- Notes: donor utility import

- Source repo: Lydia-No/The-cube
- Source path: packages/field-core/backend/core/timeline.py
- Source commit SHA: 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Destination path: runtime/field/backend/core/timeline.py
- Action: copied
- Notes: donor utility import

- Source repo: Lydia-No/hypercube-field-system and Lydia-No/The-cube
- Source path: backend/api/server.py and packages/field-core/backend/api/server.py
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821 and 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Destination path: runtime/field/backend/api/server.py
- Action: merged manually
- Notes: kept canonical runtime endpoints and added donor /health endpoint only

- Source repo: Lydia-No/hypercube-field-system and Lydia-No/The-cube
- Source path: requirements.txt and packages/field-core/requirements.txt
- Source commit SHA: 16a6aa5241be9a0f714c17428478521903b33821 and 117a3a84d60e82a3b484d7e20f9e4074d46c7835
- Destination path: runtime/field/requirements.txt
- Action: merged manually
- Notes: reduced to the minimal validated dependency set used by the staged runtime

### realERT imports
- Source repo: Lydia-No/realERT
- Source path: src/realerts/
- Source commit SHA: 61feca1e0748a7fcdb0ce660bfa3a28c96439cf8
- Destination path: apps/realert/src/realerts/
- Action: copied selectively
- Notes: canonical package import for realERT

- Source repo: Lydia-No/realERT
- Source path: src/realerts/simulation/lineage.py and lineage.py
- Source commit SHA: ce48efa2517a6257b12e70afd1e48ffe2265a3f8 and b2c3baccd63b03b23339129278b432a4f85ee484
- Destination path: apps/realert/src/realerts/simulation/lineage.py
- Action: merged manually
- Notes: kept package implementation and imported the flat-file parents() helper only
