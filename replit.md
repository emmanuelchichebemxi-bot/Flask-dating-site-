# Python Project

This project includes a standalone Python package with a small command-line example.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string
- `cd python-project && python -m python_project` — run the Python CLI
- `cd python-project && python -m pytest` — run the Python tests

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)
- Python: Python 3.11+, setuptools, pytest

## Where things live

- `python-project/` — standalone Python package and CLI
- `python-project/pyproject.toml` — Python package metadata and entry point
- `python-project/src/python_project/main.py` — CLI implementation
- `python-project/tests/` — Python tests

## Architecture decisions

- The Python package uses a `src` layout so installed and source imports behave consistently.
- The Python package is kept separate from the existing pnpm workspace services.

## Product

The Python starter currently provides a greeting CLI that can be extended with application-specific behavior.

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

_Populate as you build — sharp edges, "always run X before Y" rules._

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
