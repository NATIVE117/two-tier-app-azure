# Two-Tier Web App on Azure

## Overview
This project demonstrates a two-tier web application deployed on Azure, consisting of a React frontend and a FastAPI backend.

The goal was to build, containerize, deploy, and debug a real-world cloud application while documenting every failure and fix along the way.

## Architecture
- Frontend: React (Vite)
- Backend: FastAPI (Python)
- Containerization: Docker
- Backend Hosting: Azure App Service (Web App for Containers)
- Frontend Hosting: Azure Storage Static Website

## Key Features
- REST API backend with `/message` endpoint
- Static frontend consuming backend API
- Dockerized backend deployment
- Production-ready frontend build

## Lessons Learned
- Cloud ≠ local environments
- Docker networking matters
- RBAC can block deployments by design
- Static hosting simplifies frontend delivery
- Logs and curl are essential debugging tools

## Verification
```bash
curl https://<backend-app-name>.azurewebsites.net/message
curl https://<frontend-url>
