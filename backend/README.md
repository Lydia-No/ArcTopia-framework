# ArcTopia Backend

This backend provides the live ArcTopia governance engine.

## What it does

It supports:

- resource creation
- lineage links
- obligation tracking
- fulfillment tracking
- event-driven recognition state computation
- propagation from upstream to downstream
- simulation of hypothetical events
- decision suggestions

## Run requirements

- Node.js
- PostgreSQL
- Docker Compose (recommended for local DB)

## Local DB

From repo root:

```bash
docker-compose up -d
