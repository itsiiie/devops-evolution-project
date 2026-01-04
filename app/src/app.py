import os
from flask import Flask, jsonify
import psycopg

app = Flask(__name__)

# ---------------------------
# Environment Configuration
# ---------------------------
APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "v1-dev")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "devopsdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


# ---------------------------
# Helper: Database Connection
# ---------------------------
def get_db_connection():
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=3,
    )


# ---------------------------
# Routes
# ---------------------------
@app.route("/health")
def health():
    """
    Health check endpoint.
    Used by load balancers, CI/CD, monitoring.
    """
    return jsonify(
        status="ok",
        environment=APP_ENV
    ), 200


@app.route("/version")
def version():
    """
    Shows deployed application version.
    Helps with debugging deployments and rollbacks.
    """
    return jsonify(
        version=APP_VERSION
    ), 200


@app.route("/items")
def items():
    """
    Database connectivity check.
    Intentionally simple to expose infra issues clearly.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                result = cur.fetchone()

        return jsonify(
            message="Database connection successful",
            result=result[0]
        ), 200

    except Exception as e:
        return jsonify(
            error="Database connection failed",
            details=str(e)
        ), 500


# ---------------------------
# Application Entry Point
# ---------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
