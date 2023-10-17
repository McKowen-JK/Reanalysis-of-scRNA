import loompy
import numpy as np

# Load the .loom file
ds = loompy.connect("GSM4363298_7053cells_highquality_ovary.loom")

# Define the gene name for BEAF-32
gene_name_beaf32 = "BEAF-32"

# Find the index of BEAF-32 within the 'Genes' row attribute
gene_index_beaf32 = np.where(ds.ra['Gene'] == gene_name_beaf32)[0][0]

# Access the expression data for BEAF-32
beaf32_expression = ds[gene_index_beaf32, :]

# Calculate Pearson correlation coefficients for all genes
correlation_coefficients = []
for gene_index in range(ds.shape[0]):
    if gene_index != gene_index_beaf32:  # Exclude BEAF-32 itself
        gene_expression = ds[gene_index, :]
        correlation = np.corrcoef(beaf32_expression, gene_expression)[0, 1]
        correlation_coefficients.append((gene_index, correlation))

# Sort genes by correlation coefficient
correlation_coefficients.sort(key=lambda x: abs(x[1]), reverse=True)

# Set threshold
threshold = 0.5

# Extract genes with correlations above the threshold
significant_genes = [ds.ra['Gene'][gene_index] for gene_index, correlation in correlation_coefficients if abs(correlation) >= threshold]

# Print or save the list of significant genes
print("Genes with significant correlation to BEAF-32:")
for gene in significant_genes:
    print(gene)
