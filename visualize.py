import os
import json
import math
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx
# pip install networkx matplotlib

# Color mapping for different file types
COLOR_MAP = {
    '.py': '#3776AB',  # Python blue
    '.md': '#f5f5f5',  # Light gray for markdown
    '.txt': '#d3d3d3', # Light gray for text
    '.yml': '#cb171e', # Red for YAML
    '.gitignore': '#000000',  # Black for git files
    '': '#7f7f7f'  # Default gray
}

def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except:
        return 0

def get_file_color(filename):
    _, ext = os.path.splitext(filename)
    return COLOR_MAP.get(ext, COLOR_MAP[''])

def analyze_dcclib(repo_path):
    data = {"name": "dcclib", "children": []}
    
    def process_directory(path, node):
        try:
            items = os.listdir(path)
        except:
            return
            
        for item in items:
            if item.startswith('.git') or item == '__pycache__':
                continue
                
            full_path = os.path.join(path, item)
            child = {"name": item}
            
            if os.path.isfile(full_path):
                size = get_file_size(full_path)
                child["size"] = size
                child["type"] = "file"
                child["extension"] = os.path.splitext(item)[1]
                if size > 0:  # Only add non-empty files
                    node["children"].append(child)
            elif os.path.isdir(full_path):
                child["children"] = []
                child["type"] = "directory" 
                node["children"].append(child)
                process_directory(full_path, child)
                
    process_directory(repo_path, data)
    return data

def generate_dcclib_visualization(data, output_file):
    plt.style.use('dark_background')
    
    G = nx.Graph()
    node_colors = []
    
    def add_nodes(node, parent=None, depth=0, path=None):
        if path is None:
            path = [node["name"]]
        else:
            path = path + [node["name"]]

        node_id = "/".join(path)
        size = math.sqrt(node.get("size", 3000))  # Adjusted base size
        G.add_node(node_id,
                  size=size,
                  label=node["name"],
                  depth=depth)

        # Set color based on file type
        if "type" in node and node["type"] == "file":
            color = get_file_color(node["name"])
        else:
            color = '#2F4F4F'  # Darker color for directories
        node_colors.append(color)

        if parent:
            G.add_edge(parent, node_id)

        if "children" in node:
            for child in node["children"]:
                add_nodes(child, node_id, depth + 1, path)
    
    add_nodes(data)
    
    # Layout
    pos = nx.spring_layout(G, k=1, iterations=50)
    
    # Create visualization
    plt.figure(figsize=(20,20))
    plt.title("DCCLib Repository Structure", pad=20, size=16)
    
    # Draw nodes
    node_sizes = [G.nodes[node]["size"] * 100 for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, 
                          node_size=node_sizes,
                          node_color=node_colors,
                          alpha=0.7)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, 
                          edge_color='gray',
                          alpha=0.2,
                          width=0.5)
    
    # Add labels
    labels = {node: G.nodes[node]["label"] for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, 
                          labels,
                          font_size=8,
                          font_color='white')
    
    # Add legend
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                label=ext,
                                markerfacecolor=color, 
                                markersize=10)
                      for ext, color in COLOR_MAP.items()]
    plt.legend(handles=legend_elements, 
              loc='center left',
              bbox_to_anchor=(1, 0.5))
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, 
                bbox_inches='tight',
                dpi=300,
                facecolor='white')
    plt.close()

if __name__ == "__main__":
    # Replace with your local path to dcclib repository
    REPO_PATH = "./dcclib"  
    OUTPUT_FILE = "dcclib_visualization.png"
    
    data = analyze_dcclib(REPO_PATH)
    generate_dcclib_visualization(data, OUTPUT_FILE)