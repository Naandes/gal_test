from extract import extract_data
from load import load_data
import schedule
import time as tm


def start():
    response_list = extract_data()
    print(f"Foram coletados {len(response_list)} filmes")
    load_data(response_list)
    print("Fim da coleta")

start()
schedule.every(2).days.do(start)

while True:
    schedule.run_pending()
    tm.sleep(1)
