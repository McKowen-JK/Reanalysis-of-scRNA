import loompy
import matplotlib.pyplot as plt
import numpy as np

# Load the .loom file
ds = loompy.connect("GSM4363298_7053cells_highquality_ovary.loom")

# Access gene attributes
gene_attributes = ds.ra

# Access the "Gene" attribute
genes = gene_attributes["Gene"]

# Define the gene of interest
gene_name = "BEAF-32"

# Find the index of the gene within the 'Genes' row attribute
gene_index = np.where(ds.ra['Gene'] == gene_name)[0][0]

# Access the expression data for 'BEAF-32' and transpose it
beaf_32_expression = ds[gene_index, :]

# Access cell type labels
cell_labels = ds.ca["CellType"]


# Count the number of unique cell types
unique_cell_types = np.unique(cell_labels)
num_cell_types = len(unique_cell_types)

# Calculate the mean expression of BEAF-32 for each cell type
mean_expression = [np.mean(beaf_32_expression[cell_labels == cell_type]) for cell_type in unique_cell_types]

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.barh(unique_cell_types, mean_expression, color='skyblue')
plt.xlabel('Mean Expression of BEAF-32')
plt.ylabel('Cell Type')
plt.title('Gene Expression of BEAF-32 Among Cell Types')
plt.tight_layout()
plt.show()

# Close the .loom file
ds.close()

