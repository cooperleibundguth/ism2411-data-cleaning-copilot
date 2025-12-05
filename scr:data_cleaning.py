import pandas as pd



def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df 



def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df 



def handle_missing_values(df):
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    if "quantity" in df.columns:
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    df = df.dropna(subset=["price", "quantity"])
    return df



def remove_invalid_rows(df):
    df = df[df["price"] >= 0]
    df = df[df["quantity"] >= 0]
    return df



def strip_text_columns(df):
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()
    return df



if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = strip_text_columns(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
