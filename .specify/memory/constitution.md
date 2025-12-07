<!--
Sync Impact Report:
- Version change: 0.0.0 -> 1.0.0
- Modified principles: All principles have been rewritten.
- Added sections: Technology Stack, Development Workflow.
- Removed sections: None.
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
  - ✅ .claude/commands/sp.constitution.md
- Follow-up TODOs: None.
-->
# Full-Stack Todo Application Constitution

## Core Principles

### I. Code Quality and Maintainability
- Strict typing is mandatory. Use `mypy` for Python backend and TypeScript for Next.js frontend.
- Comprehensive and predictable error handling is required. Implement custom exception classes for business logic and a global error handling middleware in the FastAPI backend.
- All code must be tested. Use `pytest` for the backend and `Jest`/`React Testing Library` for the frontend. Unit tests must cover all business logic, and integration tests must cover all API endpoints.

### II. RESTful API Design
- APIs must adhere to RESTful conventions.
- Use standard HTTP status codes (e.g., 200, 201, 204, 400, 401, 403, 404, 500).
- Responses must use a consistent JSON format, such as `{ "data": ... }` for success or `{ "error": { "message": "..." } }` for failures.
- Use Pydantic for request and response data validation in FastAPI to ensure type safety and clear contracts.

### III. Security First (NON-NEGOTIABLE)
- All authenticated endpoints must be protected. JWT validation must be performed in a shared dependency or middleware.
- User data must be isolated. All database queries must include a condition to scope data to the authenticated user.
- Passwords must be securely hashed using a strong, salted algorithm (e.g., `passlib` with `bcrypt`).
- Prevent injection attacks by using ORM/query builders (SQLAlchemy) and validating/sanitizing all user input.

### IV. Structured Database Management
- Database schemas must be clearly defined, normalized, and documented.
- Database migrations are mandatory and must be managed using `Alembic`. Migrations must be reversible.
- Apply indexes to foreign keys and columns that are frequently used in `WHERE` clauses to optimize query performance.

### V. Modern Frontend Architecture
- Implement a component-based architecture. Components should be small, reusable, and follow a logical structure (e.g., atomic design).
- Use a centralized state management solution (e.g., React Context, Zustand) for global state like user information.
- Ensure the application is accessible by following WCAG 2.1 guidelines.
- All UI must be responsive and functional across modern web browsers and device sizes.

### VI. Comprehensive Documentation
- The primary source of truth for the API is the auto-generated OpenAPI (Swagger/ReDoc) documentation from FastAPI.
- Frontend components should be documented using TSDoc.
- The `README.md` file must contain a project overview, setup instructions, and architecture details.
- Use inline comments only to explain the *why* behind complex or non-obvious code, not the *what*.

### VII. Disciplined Git Workflow
- Follow the Conventional Commits specification for all commit messages (e.g., `feat:`, `fix:`, `docs:`, `chore:`).
- All development must happen on feature branches (e.g., `feature/TICKET-123-add-login`).
- All code must be merged into the `main` branch via Pull Requests (PRs).
- PRs must pass all automated checks (linting, tests) and receive at least one approval from a peer before being merged.

## Technology Stack
- **Frontend**: Next.js 16+ with TypeScript
- **Backend**: Python 3.11+ with FastAPI
- **Database**: Neon PostgreSQL
- **Authentication**: JWT-based

## Development Workflow
- The workflow follows the principles outlined in this constitution.
- All work must be tracked in an issue tracker.
- Code reviews should focus on adherence to the constitution, correctness, and maintainability.

## Governance
- This constitution is the single source of truth for all development practices. It supersedes any previous or informal agreements.
- Any amendments to this constitution require a formal proposal, a review by the team, and an update to this document, including a version bump.
- All code reviews must verify compliance with this constitution. Any deviations must be explicitly justified and approved.

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07