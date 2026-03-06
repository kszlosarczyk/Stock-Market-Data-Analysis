import os
from datetime import datetime

import pandas as pd

from config import OUTPUT_DIR


def save_outputs(df: pd.DataFrame) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    df_to_save = df.copy()

    df_to_save["Date"] = df_to_save["Date"].dt.strftime("%Y-%m-%d")

    latest = (
        df.sort_values("Date")
        .groupby("BBG")
        .tail(1)
        .reset_index(drop=True)
    )

    df_to_save.to_csv(
        f"{OUTPUT_DIR}/stock_history_{today}.csv",
        index=False,
        encoding="utf-8-sig",
    )

    with pd.ExcelWriter(
        f"{OUTPUT_DIR}/stock_report_{today}.xlsx",
        engine="xlsxwriter",
    ) as writer:
        df_to_save.to_excel(writer, sheet_name="History", index=False)
        latest.to_excel(writer, sheet_name="Latest", index=False)
