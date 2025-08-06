import pandas as pd
import os

def create_lead_identification_agent(csv_file_path, output_file_path):
    """
    Loads data, scores leads based on TotalVisits, and segments them.
    Saves processed data to the output path.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path)
        df.columns = df.columns.str.strip()

        print("Column names found after loading CSV:")
        print(df.columns.tolist())  # For-debugging

        # Lead Scoring Logic
        if 'TotalVisits' in df.columns:
            max_visits = df['TotalVisits'].max()
            if max_visits > 0:
                df['lead_score'] = (df['TotalVisits'] / max_visits) * 100
            else:
                print("⚠️ Warning: 'TotalVisits' column has no valid data.")
                df['lead_score'] = 0
        else:
            print("❌ Error: 'TotalVisits' column not found for lead scoring.")
            return pd.DataFrame()

        # Lead Segmentation Logic
        if 'Lead Origin' in df.columns:
            df['segment'] = df['Lead Origin']
        else:
            df['segment'] = 'Unknown'

        # Save processed data
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        df.to_csv(output_file_path, index=False)
        print(f"✅ Processed leads saved to: {output_file_path}")

        return df

    except Exception as e:
        print("❌ Exception occurred:", e)
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    input_path = "data/Lead Scoring.csv"
    output_path = "data/Processed_Lead_Scoring.csv"
    result_df = create_lead_identification_agent(input_path, output_path)
    print(result_df.head())