import kagglehub
from kagglehub import KaggleDatasetAdapter

def get_ai_developer_dataset():   
    file_path = kagglehub.dataset_download("ayeshasiddiqa123/ai-development")
    print("Path to dataset files:", file_path)
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "ayeshasiddiqa123/ai-development",
        "AI_Developer_Performance_Extended_1000.csv")
    df_clean = df.dropna()
    df_clean = df_clean.drop_duplicates()
    return df_clean