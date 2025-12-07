---
id: 0001
title: Specify Full-Stack Todo Application
stage: spec
date: 2025-12-07
surface: agent
model: gemini-1.5-pro
feature: 001-fullstack-todo-app
branch: 001-fullstack-todo-app
user: qiratsumra
command: /sp.specify
labels: [spec, full-stack, requirements]
links:
  spec: specs/001-fullstack-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-fullstack-todo-app/spec.md
  - specs/001-fullstack-todo-app/checklists/requirements.md
tests:
  - null
---

## Prompt

/sp.specify Write clear, testable requirements for Phase II: Full-Stack Todo Web Application Source: Console app: @todo-app Requirements to specify: Functional Requirements: 1. User authentication (signup/signin with Better Auth) Acceptance criteria: • User can register with email+password • Login returns JWT • Invalid credentials return 401 • Passwords never stored in plain text. 2. Task CRUD operations Acceptance criteria: • Create/read/update/delete tasks • Users see only their tasks • Successful operations return proper status codes 200/201/204. 3. Task completion toggle Acceptance criteria: • Tasks have boolean completed state • PATCH toggles status • UI reflects state instantly. 4. User-specific task isolation Acceptance criteria: • Cross-user access blocked • Unauthorized access returns 403/404 • DB queries filter by owner_id. 5. Responsive UI Mobile+Desktop Acceptance criteria: • Works at 360px–1280px+ • Touch friendly • Lighthouse responsive score ≥90. Technical Requirements: 1. RESTful API (GET/POST/PUT/PATCH/DELETE) Acceptance criteria: • 6 endpoints for tasks implemented • JSON responses + spec documented. 2. JWT Auth Acceptance criteria: • All task routes require Bearer token • Invalid/expired tokens return 401 • JWT encodes user_id. 3. Neon PostgreSQL Storage Acceptance criteria: • Tasks persist • DB credential-based access • Backup/restore verified. 4. SQLModel ORM Acceptance criteria: • Models for User and Task • CRUD via ORM • Validation returns structured JSON. 5. Next.js App Router Acceptance criteria: • Server+Client components used appropriately • JWT included in fetch requests • Build passes cleanly. Non-Functional Requirements: 1. API latency <200ms Acceptance criteria: • 95th percentile under target with 500 tasks per user. 2. Frontend loads <3s on 3G Acceptance criteria: • Lighthouse performance ≥85 • Code splitting used. 3. Auth required for all endpoints Acceptance criteria: • No token →401 • Middleware enforced. 4. Password hashing bcrypt Acceptance criteria: • bcrypt cost≥10 • No raw storage. 5. CORS configured Acceptance criteria: • Only frontend domain allowed • Preflight works • Others blocked.

## Response snapshot

I have created the feature specification for the "Full-Stack Todo Web Application".

- **Branch**: `001-fullstack-todo-app`
- **Specification**: `specs/001-fullstack-todo-app/spec.md`
- **Checklist**: `specs/001-fullstack-todo-app/checklists/requirements.md`

The specification is complete and has passed all quality checks. It is now ready for the next phase: planning (`/sp.plan`).

## Outcome

- ✅ Impact: A detailed and testable specification has been created, providing a clear foundation for the development of the full-stack application.
- 🧪 Tests: No tests were run as this was a documentation task.
- 📁 Files: 2 files were created.
- 🔁 Next prompts: `/sp.plan`
- 🧠 Reflection: The process was smooth. The `create-new-feature.sh` script worked as expected. The PHR script still has issues on Windows.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-phr.sh` script continues to have a malformed output on Windows.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Fix the `create-phr.sh` script to handle paths correctly on Windows.