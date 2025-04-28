import pandas as pd
from db import get_connection
from embed import get_embedding

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        question = row["question"]
        answer = row["answer"]
        full_text = question + " " + answer
        embedding = get_embedding(full_text)

        cur.execute(
            "INSERT INTO medquad (question, answer, embedding) VALUES (%s, %s, %s)",
            (question, answer, embedding)
        )

    conn.commit()
    conn.close()
    print("✅ Loaded MedQuAD dataset into pgvector")

if __name__ == "__main__":
    load_data("medquad_sample.csv")
