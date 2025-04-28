from db import get_connection
from embed import get_embedding
from psycopg2.extensions import AsIs

def retrieve_answer(query, top_k=3):
    conn = get_connection()
    cur = conn.cursor()
    query_vec = get_embedding(query)

    # Convert list to comma-separated string
    query_vector_str = ','.join(map(str, query_vec))

    cur.execute(
        """
        SELECT question, answer, embedding <-> vector[%s] AS score
        FROM medquad
        ORDER BY score
        LIMIT %s;
        """,
        (AsIs(query_vector_str), top_k)
    )

    result = cur.fetchall()
    conn.close()
    return result
