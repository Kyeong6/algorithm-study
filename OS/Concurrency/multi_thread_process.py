import os
import csv
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait

# 변수 설정
CSV_NAME = "test.csv"
CONTENTS: list = []
TOTAL_COUNTS = 1_000_000
MAX_WORKERS = 1 # 해당 값을 변경해가며 작업 단위 늘릴 수 있음

# 테스트 진행을 위한 csv 생성 함수
def create_test_csv(name):
    fp = open(name, "w")
    w = csv.writer(fp)
    for _ in range(0, TOTAL_COUNTS):
        w.writerow([1,2,3,4])

# multi-thread를 테스트하기 위한 기본 설정 함수
def test_multi_threads():
    fp = open(CSV_NAME)
    r = csv.reader(fp)

    # list comprehension으로 메모리에 적재
    contents = [i for i in r]
    for content in contents:
        content == [1,2,3,4]


# multi-processing을 테스트하기 위한 기본 설정 함수
def test_multi_processes():
    fp = open(CSV_NAME)
    r = csv.reader(fp)

    # list comprehension으로 메모리에 적재
    contents = [i for i in r]
    for content in contents:
        content == [1,2,3,4]


# multi-threads 수행
def multi_threads():
    start_time = time.time()

    threads = []
    pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    for _ in range(MAX_WORKERS):
        threads.append(pool.submit(test_multi_threads))
    wait(threads)

    print(f"MULTI THREADS TIME: {time.time() - start_time:.3f}s")
        

# multi-processing 수행
def multi_processes():
    start_time = time.time()

    processess = []
    pool = ProcessPoolExecutor(max_workers=MAX_WORKERS)
    for _ in range(MAX_WORKERS):
        processess.append(pool.submit(test_multi_processes))
    wait(processess)

    print(f"MULTI PROCESSES TIME: {time.time() - start_time:.3f}s")


# main 실행
if __name__ == "__main__":
    if not os.path.exists(CSV_NAME):
        create_test_csv(CSV_NAME)

    # multi-threads 실행
    multi_threads()

    # multi-processing 실행
    multi_processes()
