Act as a senior software architect and static code analyst. Your task is to produce a deep, exhaustive map of this repository. I need full visibility into structure, capabilities, dependencies, data flow, conventions, and implicit logic. Do not summarize; drill into file/module-level responsibilities and cross-references.

Follow this exact workflow and output format:

1. 📁 REPOSITORY STRUCTURE
   - Generate an annotated directory tree. Tag each dir/file with: role (e.g., `#entry`, `#config`, `#test`, `#lib`, `#infra`), framework, and responsibility.
   - Note build tools, package managers, linters, formatters, and CI/CD files.

2. 🚪 ENTRY POINTS & EXECUTION FLOW
   - List all entry points: main functions, route definitions, CLI commands, worker scripts, Docker/entrypoint scripts, serverless triggers, etc.
   - Trace high-level call paths from each entry point (1-3 hops deep).

3. 🧩 MODULE/COMPONENT MAPPING
   For each logical module:
   - Purpose & boundary
   - Public API (exports, routes, interfaces, public classes/functions)
   - Internal dependencies & imports
   - Key files & their exact responsibilities
   - How it integrates with other modules

4. 💧 DATA & STATE FLOW
   - Models, schemas, DTOs, types, and where they're defined/used
   - Databases, caches, queues, file storage, and config-driven state
   - Data transformation pipelines (serializers, validators, mappers)

5. 🔗 DEPENDENCIES & INTEGRATIONS
   - External: libraries, frameworks, APIs, SDKs, env-dependent services
   - Internal: cross-module references, shared utilities, barrel exports
   - Note version pins, peer deps, or conditional imports if visible

6. ⚙️ CONFIGURATION & ENVIRONMENT
   - Env vars, config files, feature flags, secrets strategy
   - Multi-environment setup (dev/stage/prod), deployment targets, infra-as-code refs

7. 🧪 TESTING, QUALITY & CONVENTIONS
   - Test structure, coverage hints, mocking strategies, fixture patterns
   - Linting/formatting rules, error handling, logging, authentication/authorization patterns
   - Naming conventions, architecture style (MVC, hex, event-driven, etc.), and implicit rules

8. 🔍 GAP ANALYSIS & VERIFICATION
   - Flag: undocumented logic, ambiguous imports, circular dependencies, missing tests, potential dead code
   - Tag confidence per section: `[CONFIRMED]`, `[INFERRED]`, `[NEEDS_VERIFICATION]`

OUTPUT RULES:
- Use markdown with clear headings, tables for cross-references, and exact file paths.
- If the repo exceeds context limits, process in logical chunks (e.g., by top-level dir) and end each response with: `CONTINUE? [Y/N]`
- Never guess. If a reference is unclear, state how it should be verified.
- Begin with Section 1 & 2. I will follow up with targeted deep-dive prompts.

## [MODULE_NAME]
- **Purpose**: ...
- **Public API**: 
  - `src/module/api.ts` → exports: `functionA()`, `class B`
  - `src/module/routes.js` → endpoints: `/v1/items`
- **Internal Deps**: 
  - `import { helper } from '../utils/transform'` [CONFIRMED]
  - `import { db } from '../../infra/db'` [NEEDS_VERIFICATION]
- **Key Files**:
  - `src/module/core.ts` → handles X, Y, Z. Entry point for workers.
- **Data Flow**: Receives → validates → transforms → writes to [DB/Table]
- **Testing**: `__tests__/core.test.ts` covers happy path. Edge cases mocked via `jest.mock`.
- **Confidence**: 85% [INFERRED cross-module deps]