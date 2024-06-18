import requests
import sqlite3
import time

from orchestrator.orchestrator import IOrchestrator
from orchestrator.types import Task

api_url: str = "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1"

db_path: str = './cache/cache.db'


def check_hash_in_db(hash_value: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    _ = cursor.execute("SELECT * FROM files WHERE hash=?", (hash_value,))
    result: tuple[int, str, str] | None = cursor.fetchone()
    conn.close()
    return result is not None

#download files and return path to them
def mock_file_request(hash_value: str):
    return "test_files/" + hash_value

def save_hash_to_db(hash_value: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    _ = cursor.execute("INSERT INTO files (hash) VALUES (?)", (hash_value,))
    conn.commit()
    conn.close()

def save_filepath_to_db(file_path: str, file_hash: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    _ = cursor.execute("UPDATE files SET filepath=? WHERE hash=?", (file_path, file_hash))
    conn.commit()
    conn.close()

def print_database_contents():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    _ = cursor.execute("SELECT * FROM files")
    rows: list[tuple[int, str, str]] = cursor.fetchall()
    print("db content:")
    for row  in rows:
        print(row)
    conn.close()

def get_file_from_hash(file_hash: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    _ = cursor.execute("SELECT * FROM files WHERE hash=?", (file_hash,))
    row: tuple[int, str, str] = cursor.fetchone()
    conn.close()
    return row


def czy_plikies(orchestrator: IOrchestrator):
    while True:
        response = requests.get(api_url)
        if response.status_code == 200:
            data: list[int] = response.json()
            file_hash = str(data[0])
            if file_hash:
                if check_hash_in_db(file_hash):
                    print(f"Hash {file_hash} znajduje się w bazie danych.")
                else:
                    print(f"Hash {file_hash} nie znajduje się w bazie danych.")
                    save_hash_to_db(file_hash)
                    file_path = mock_file_request(file_hash)
                    save_filepath_to_db(file_path, file_hash)
                    print_database_contents()
                    task  = get_file_from_hash(file_hash)
                    orchestrator.add_task({"id": str(task[0]), "filepath": task[1]})
            else:
                print("Otrzymano niekompletną odpowiedź.")
        time.sleep(5)


def handle_completion(task: Task):
    print("completed: " + str(task))