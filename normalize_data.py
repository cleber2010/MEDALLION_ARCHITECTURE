import os
import pandas as pd


class NormalizeData:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def normalize_data(self):
        for file in os.listdir(self.input_dir):
            imput_path = os.path.join(self.input_dir, file)
            name, ext = os.path.splitext(file)
            output_path = os.path.join(self.output_dir, f"{name}.parquet")

            if ext.lower() == ".csv":
                df = pd.read_csv(imput_path)
            elif ext.lower() == ".json":

                try:
                    df = pd.read_json(imput_path)
                except ValueError:
                    df = pd.read_json(imput_path, lines=True)
            else:
                print(f"Unsupported file format: {file}")
                continue

            for col in df.columns:
                if df[col].apply(lambda x: isinstance(x, list)).any():
                    df[col] = df[col].apply(lambda x: str(x) if isinstance(x, list) else x)

            df = df.drop_duplicates().reset_index(drop=True)

            df.to_parquet(output_path, index=False)
            print(f"Normalized {file} and saved to {output_path}")

if __name__ == "__main__":
    normalize_data = NormalizeData(input_dir="01-bronze-raw", output_dir="02-silver-validated")
    normalize_data.normalize_data()