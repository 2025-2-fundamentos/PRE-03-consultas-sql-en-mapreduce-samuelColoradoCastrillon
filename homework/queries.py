"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

import os
import pandas as pd

#
# ORQUESTADOR:
#
def run():
    """Orquestador"""
    df = pd.read_csv("files/input/tips.csv")  # 👈 ajusta el nombre si es diferente

    for i in range(1, 6):
        os.makedirs(f"files/query_{i}", exist_ok=True)

    q1 = df.groupby("day")["total_bill"].mean().reset_index()
    q1.to_csv("files/query_1/part-00000", index=False)
    open("files/query_1/_SUCCESS", "w").close()

    q2 = df.groupby("sex")["tip"].mean().reset_index()
    q2.to_csv("files/query_2/part-00000", index=False)
    open("files/query_2/_SUCCESS", "w").close()

    q3 = df.groupby("smoker").size().reset_index(name="count")
    q3.to_csv("files/query_3/part-00000", index=False)
    open("files/query_3/_SUCCESS", "w").close()

    q4 = df.groupby("day")["size"].sum().reset_index()
    q4.to_csv("files/query_4/part-00000", index=False)
    open("files/query_4/_SUCCESS", "w").close()

    q5 = df.groupby("size")["tip"].mean().reset_index()
    q5.to_csv("files/query_5/part-00000", index=False)
    open("files/query_5/_SUCCESS", "w").close()

if __name__ == "__main__":
    run()