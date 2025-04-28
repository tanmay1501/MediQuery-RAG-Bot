import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="medquad",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS medquad (
            id SERIAL PRIMARY KEY,
            question TEXT,
            answer TEXT,
            embedding VECTOR(384)  -- all-MiniLM-L6-v2
        )
    """)
    conn.commit()
    conn.close()
