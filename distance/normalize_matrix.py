import pandas as pd
import sys

if len(sys.argv) != 2:
    print("Usage: python test.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    df = pd.read_csv(input_file, index_col=0)
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
    sys.exit(1)


# z_scores = (df - df.mean()) / df.std()

# # Step 4: Apply Min-Max Scaling to Z-scores
# z_min = z_scores.min().min()  # Minimum Z-score
# z_max = z_scores.max().max()  # Maximum Z-score

# # Rescale to [0, 1]
# scaled_df = (z_scores - z_min) / (z_max - z_min)

# scaled_df = scaled_df.round(2)

# output_file = f"{input_file}_normalized.csv"
# scaled_df.to_csv(output_file)

normalized_df = (df - df.min()) / (df.max() - df.min())


output_file = f"{input_file}_normalized.csv"

normalized_df = normalized_df.round(3)

normalized_df.to_csv(output_file)

print(
    f"Normalization complete. The normalized matrix has been saved to '{output_file}'."
)
