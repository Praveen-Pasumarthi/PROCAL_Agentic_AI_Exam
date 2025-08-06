import pandas as pd
import os

def generate_personalized_emails(input_csv_path, output_csv_path):
    if not os.path.exists(input_csv_path):
        print(f"❌ File not found: {input_csv_path}")
        return

    # Load the processed lead data
    df = pd.read_csv(input_csv_path)
    required_columns = ['Prospect ID', 'Lead Number', 'segment', 'lead_score']

    # Validate required columns
    for col in required_columns:
        if col not in df.columns:
            print(f"❌ Required column '{col}' not found in input data!")
            return

    # Generate personalized emails
    personalized_messages = []
    for _, row in df.iterrows():
        name_placeholder = f"Lead #{row['Lead Number']}"
        segment = row['segment']
        score = row['lead_score']

        # Rule-based message logic
        if score > 75:
            message = f"Hi {name_placeholder}, thanks for being such an engaged user! We noticed your interest from the {segment} channel. Here’s a special offer for you!"
        elif score > 40:
            message = f"Hi {name_placeholder}, we appreciate your activity. Since you came from {segment}, we’d love to recommend our top programs."
        else:
            message = f"Hi {name_placeholder}, we noticed you visited us via {segment}. Check out our programs to learn more!"

        personalized_messages.append({
            "Prospect ID": row['Prospect ID'],
            "Lead Number": row['Lead Number'],
            "Personalized Message": message
        })

    # Create output DataFrame
    output_df = pd.DataFrame(personalized_messages)
    output_df.to_csv(output_csv_path, index=False)
    print(f"✅ Personalized emails saved to: {output_csv_path}")
    print(output_df.head())


if __name__ == "__main__":
    generate_personalized_emails(
        input_csv_path="data/Processed_Lead_Scoring.csv",
        output_csv_path="data/Personalized_Emails.csv"
    )