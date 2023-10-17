import loompy
import umap
import matplotlib.pyplot as plt
import numpy as np

# Load the .loom file and preprocess the data
ds = loompy.connect("GSM4363298_7053cells_highquality_ovary.loom")

# Access UMAP cell embeddings
umap_embeddings = ds.ca["umap_cell_embeddings"]

# Define the gene name
gene_name = "BEAF-32"

# Find the index of the gene within the 'Genes' row attribute
gene_index = np.where(ds.ra['Gene'] == gene_name)[0][0]

# Access the expression data for 'BEAF-32' and transpose it
gene_expression = ds[gene_index, :]

# Create the UMAP plot and overlay 'BEAF-32' expression
plt.figure(figsize=(10, 8))
sc = plt.scatter(umap_embeddings[:, 0], umap_embeddings[:, 1], c=gene_expression, cmap='Reds', s=10)

plt.title("UMAP Visualization with 'BEAF-32' Expression")
plt.xlabel("UMAP 1")
plt.ylabel("UMAP 2")

# Add a colorbar to the plot
cbar = plt.colorbar(sc, label="BEAF-32 Expression")

# Save the UMAP plot
plt.savefig("umap_plot_beaf.png")

# Show the UMAP plot (optional)
# plt.show()

# Close the .loom file
ds.close()
