import loompy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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

# Create a mapping of current labels to new labels
label_mapping = {
    # Add your label mapping here
}

# Map cell type labels
mapped_cell_labels = [label_mapping[label] if label in label_mapping else label for label in cell_labels]

# Create a Pandas DataFrame for your data
data = pd.DataFrame({'Cell Type': mapped_cell_labels, 'BEAF-32 Expression': beaf_32_expression})

# Create a facet grid using Seaborn catplot
plt.figure(figsize=(14, 6))
g = sns.catplot(data=data, x='Cell Type', y='BEAF-32 Expression', kind="violin", palette="viridis")
g.set_axis_labels("Cell Type", "BEAF-32 Expression")
g.set_xticklabels(rotation=45, horizontalalignment="right")
g._legend.remove()  # Remove the legend
plt.title("Gene Expression of BEAF-32 Among Cell Types (Violin Plot)")
plt.tight_layout()
plt.show()

# Close the .loom file
ds.close()

