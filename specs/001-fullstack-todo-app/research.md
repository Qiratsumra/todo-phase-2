# Research: Full-Stack Todo Web Application

This document summarizes key technical research and decisions made during the planning phase for the Full-Stack Todo Application.

## 1. Database Selection for FastAPI Backend

**Task**: Research the best database for FastAPI applications, considering PostgreSQL, SQLite, and MySQL.

**Decision**: PostgreSQL (specifically via a managed service like Neon).

**Rationale**:
- **Performance & Features**: PostgreSQL offers a rich feature set, including robust support for JSON, full-text search, and a wide array of indexing strategies that are beneficial for future scalability.
- **Async Support**: It has excellent asynchronous support through libraries like `asyncpg`, which integrates perfectly with FastAPI's async nature, providing a non-blocking data access layer.
- **Ecosystem**: The Python ecosystem for PostgreSQL is mature. SQLAlchemy, our chosen ORM, has first-class support for it, and Alembic makes migrations straightforward.
- **SQLite Limitation**: While simple for development, SQLite is not suitable for a production web application that requires concurrent write access.
- **MySQL vs. PostgreSQL**: Both are viable, but PostgreSQL's feature set and strong async story give it the edge for modern Python web backends.
- **Managed Service (Neon)**: Using a managed serverless Postgres like Neon simplifies operations, handles automated backups, scaling, and allows for features like database branching, which is excellent for development and testing.

**Alternatives Considered**:
- **SQLite**: Rejected due to limitations with write concurrency, making it unsuitable for a production web service.
- **MySQL**: A strong contender, but PostgreSQL's advanced features and superior async driver ecosystem made it the preferred choice.

---

## 2. Next.js and FastAPI Integration Patterns

**Task**: Find best practices for integrating a Next.js frontend with a FastAPI backend.

**Decision**: Use a proxy for development and separate services for production, communicating via a REST API.

**Rationale**:
- **Development (Proxy)**: In development, Next.js's built-in proxy feature (`rewrites` in `next.config.js`) will be used to forward API requests from the frontend (e.g., `/api/v1/...`) to the FastAPI backend server running on a different port. This avoids CORS issues and simplifies local setup.
- **Production (Separate Services)**: In production, the Next.js frontend and FastAPI backend will be deployed as separate containerized services. An API Gateway or reverse proxy (like Nginx or Traefik) will route requests from the public domain to the appropriate service (e.g., requests to `/v1/*` go to the FastAPI container, all others go to the Next.js container).
- **API Client**: The frontend will use a dedicated API client (e.g., a wrapper around `axios` or `fetch`) to handle communication with the backend. This client will be responsible for setting the `Authorization` header, handling standardized error responses, and managing token refresh logic.

**Alternatives Considered**:
- **Serving Frontend from FastAPI**: FastAPI can be configured to serve static files, but this negates all the benefits of Next.js's server-side rendering, static site generation, and optimized build process. Rejected as it undermines the choice of Next.js.
- **Serverless Functions**: Deploying the FastAPI backend as serverless functions (e.g., on Vercel) alongside the Next.js frontend is a viable pattern but adds complexity to database connection management and can be less cost-effective for sustained workloads. The Docker-based approach is more flexible and portable.

---

## 3. JWT Token Storage Strategy

**Task**: Research and decide on a secure token storage strategy (HttpOnly cookies vs. localStorage) for a Next.js application.

**Decision**: A hybrid approach: store the refresh token in a secure, HttpOnly cookie and the short-lived access token in application memory (e.g., a React Context or Zustand store).

**Rationale**:
- **Security (CSRF & XSS)**:
    - **Refresh Token (HttpOnly Cookie)**: Storing the long-lived refresh token in an `HttpOnly`, `Secure`, and `SameSite=Strict` cookie provides the best protection against Cross-Site Scripting (XSS) attacks, as JavaScript cannot access it. The `SameSite=Strict` flag provides strong protection against Cross-Site Request Forgery (CSRF).
    - **Access Token (Memory)**: Storing the short-lived access token in memory prevents it from being vulnerable to XSS attacks that target `localStorage`. Since it's short-lived (e.g., 15 minutes), the window of opportunity for theft is small. It is sent with each API request via the `Authorization: Bearer <token>` header.
- **UX**: This approach enables a "silent refresh" flow. When the access token expires, the frontend can make a request to a `/refresh` endpoint. The browser will automatically send the HttpOnly refresh token cookie, and the backend can issue a new access token without requiring the user to log in again.

**Alternatives Considered**:
- **Storing Both Tokens in `localStorage`**: Rejected due to high vulnerability to XSS attacks. If a malicious script runs on the site, it can steal both tokens, leading to full account compromise.
- **Storing Both Tokens in Cookies**: This is a viable option but can be more complex to manage from the frontend, as JavaScript cannot directly access the access token to add it to the `Authorization` header. It would require all API calls to be simple `GET` or `POST` requests where the cookie is sent automatically, which is not always the case with modern APIs, or would rely on the server to handle the token extraction from the cookie. The hybrid approach is more explicit and aligns better with the RESTful `Bearer` token pattern.
