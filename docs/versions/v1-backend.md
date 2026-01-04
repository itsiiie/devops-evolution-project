# Version 1 – Backend Service

## Overview

A minimal Flask backend built specifically to support DevOps workflows.

## Endpoints

- `/health` – Used for CI checks, monitoring, and load balancers
- `/version` – Confirms deployed version
- `/items` – Database connectivity verification

## Configuration

All configuration is provided via environment variables.

## DevOps Principles Applied

- No hardcoded configuration
- Clear failure visibility
- Same code runs in local, CI, Docker, and EC2
