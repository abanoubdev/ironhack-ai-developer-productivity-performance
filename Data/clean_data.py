import kagglehub
from kagglehub import KaggleDatasetAdapter

def get_ai_developer_dataset():   
    """
    This function downloads the AI Developer Performance dataset from Kaggle and returns it as a pandas DataFrame.
    """
    file_path = kagglehub.dataset_download("ayeshasiddiqa123/ai-development")
    print("Path to dataset files:", file_path)
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "ayeshasiddiqa123/ai-development",
        "AI_Developer_Performance_Extended_1000.csv")

    df_clean = df.drop_duplicates()
    return df_clean