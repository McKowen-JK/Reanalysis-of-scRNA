import loompy
import umap
import matplotlib.pyplot as plt
import numpy as np

# Load the .loom file and preprocess the data
ds = loompy.connect("GSM4363298_7053cells_highquality_ovary.loom")

# Access UMAP cell embeddings and cell types
umap_embeddings = ds.ca["umap_cell_embeddings"]
cell_types = ds.ca["CellType"]

# Create a mapping of current labels to new labels
label_mapping = {
    '1. Early Germline Cells': ' Early Germline Cells',
    '2. Late Germline Cells': ' Late Germline Cells',
    '3. Somatic Cells in Germarium Region 1': ' Somatic Cells in Germarium Region 1',
    '4. Polar Follicle Cells': ' Polar Follicle Cells',
    '5. Interfollicle (Stalk) Cells': ' Interfollicle (Stalk) Cells',
    '6. Pre-Mitotic Follicle Cells': ' Pre-Mitotic Follicle Cells',
    '7. Mitotic Follicle Cells': ' Mitotic Follicle Cells',
    '8. Post-Mitotic Follicle Cells 1': ' Post-Mitotic Follicle Cells 1',
    '9. Post-Mitotic Follicle Cells 2': ' Post-Mitotic Follicle Cells 2',
    '10. Post-Mitotic Main Body Follicle Cells 1': ' Post-Mitotic Main Body Follicle Cells 1',
    '11. Post-Mitotic Main Body Follicle Cells 2': ' Post-Mitotic Main Body Follicle Cells 2',
    '12. Post-Mitotic Main Body Follicle Cells 3': ' Post-Mitotic Main Body Follicle Cells 3',
    '13. Post-Mitotic Main Body Follicle Cells 4': ' Post-Mitotic Main Body Follicle Cells 4',
    '14. Post-Mitotic Main Body Follicle Cells 5': ' Post-Mitotic Main Body Follicle Cells 5',
    '15. Post-Mitotic Main Body Follicle Cells 6': ' Post-Mitotic Main Body Follicle Cells 6',
    '16. Post-Mitotic Main Body Follicle Cells 7': ' Post-Mitotic Main Body Follicle Cells 7',
    '17. Post-Mitotic Main Body Follicle Cells 8': ' Post-Mitotic Main Body Follicle Cells 8',
    '18. Post-Mitotic Main Body Follicle Cells 9': ' Post-Mitotic Main Body Follicle Cells 9',
    '18.5. Post-Mitotic Main Body Follicle Cells 10': ' Post-Mitotic Main Body Follicle Cells 10',
    '19. Anterior Follicle Cells 1': ' Anterior Follicle Cells 1',
    '20. Anterior Follicle Cells 2': ' Anterior Follicle Cells 2',
    '21. Anterior Follicle Cells 3': ' Anterior Follicle Cells 3',
    '22. Anterior Follicle Cells 4': ' Anterior Follicle Cells 4',
    '23. Anterior Follicle Cells 5': ' Anterior Follicle Cells 5',
    '24. Main Body-derived Corpus luteum Cells': ' Main Body-derived Corpus luteum Cells',
    'Anterior-CL': 'Anterior-CL',
    '25. Anterior-derived Terminal Corpus luteum Cells': ' Anterior-derived Terminal Corpus luteum Cells',
    '26. Posterior-derived Terminal Corpus luteum Cells': ' Posterior-derived Terminal Corpus luteum Cells',
    '27. Muscle Sheath Cells': ' Muscle Sheath Cells',
    '28. Oviduct Cells': ' Oviduct Cells',
    '29. Adipocytes': ' Adipocytes',
    '30. Hemocytes': ' Hemocytes',
}

# Apply the label mapping to cell types
mapped_cell_types = [label_mapping.get(cell_type, cell_type) for cell_type in cell_types]

# Create a dictionary to map cell types to colors
unique_cell_types = np.unique(mapped_cell_types)
color_map = plt.get_cmap("gist_ncar")
cell_type_colors = {cell_type: color_map(i / len(unique_cell_types)) for i, cell_type in enumerate(unique_cell_types)}

# Create the UMAP plot with mapped colors and renamed cell types
plt.figure(figsize=(10, 8))
for cell_type in unique_cell_types:
    mask = np.array(mapped_cell_types) == cell_type
    plt.scatter(umap_embeddings[mask, 0], umap_embeddings[mask, 1], label=cell_type, c=[cell_type_colors[cell_type]], s=10)

plt.title("UMAP Visualization")
plt.xlabel("UMAP 1")
plt.ylabel("UMAP 2")

# Save the UMAP plot without the legend
plt.savefig("umap_plot_x.png")

# Create a legend with custom labels
legend_handles = []
for label in unique_cell_types:
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cell_type_colors[label], markersize=10, label=label))

# Create a separate legend plot and save it
legend_plot = plt.figure(figsize=(6, 3))
plt.axis('off')
plt.legend(handles=legend_handles, loc='center', title="Cell Types")
legend_plot.savefig("legend_x.png", bbox_inches='tight')

# Show the UMAP plot (optional)
# plt.show()

# Close the .loom file
ds.close()
