# ReserveGO Clone

A production-ready backend clone of a restaurant reservation system built using FastAPI and PostgreSQL.

This project was built to practice backend engineering, database integration, Linux deployment and production infrastructure rather than frontend development.

---

# Features

- Create waitlist entries
- Retrieve active waitlist
- PostgreSQL persistence
- Structured logging
- REST API
- Production deployment

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- psycopg
- Uvicorn
- Ubuntu VPS
- systemd
- Nginx
- DuckDNS
- Let's Encrypt

---

# Architecture

```
Client
   │
   ▼
FastAPI (body.py)
   │
   ▼
Business Logic (organs.py)
   │
   ▼
Database Layer (database.py)
   │
   ▼
PostgreSQL
```

---

# API Endpoints

### Create Waitlist Entry

```
POST /waitlist
```

Creates a new customer waitlist entry.

---

### Get Waitlist

```
GET /waitlist
```

Returns all active waitlist entries.

---

# Project Structure

```
body.py
        API Layer

organs.py
        Business Logic

database.py
        PostgreSQL Operations
```

---

# Skills Demonstrated

- Backend API Development
- Database Design
- PostgreSQL Integration
- Linux Server Deployment
- Production Debugging
- Reverse Proxy Configuration
- Service Management using systemd
- HTTPS Configuration
- REST API Design

---

# Deployment

Production deployment includes:

- Ubuntu VPS
- PostgreSQL
- systemd Service
- Nginx Reverse Proxy
- HTTPS using Let's Encrypt

---

# Future Improvements

- Docker
- CI/CD
- Authentication
- Reservation management
- Monitoring

---

Built as part of my backend engineering portfolio.
