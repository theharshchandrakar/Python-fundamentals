import json
import glob

def convert_ipynb_to_py(ipynb_path):
    """Convert a Jupyter notebook to a Python file with proper markdown commenting."""
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    py_content = []
    
    for cell in notebook['cells']:
        cell_type = cell['cell_type']
        source_lines = cell['source']
        
        if cell_type == 'markdown':
            # Convert each line of markdown to a comment
            for line in source_lines:
                if line.strip():  # Only comment non-empty lines
                    py_content.append(f"# {line.rstrip()}")
                else:
                    py_content.append("")  # Keep empty lines as empty
            py_content.append("")  # Add blank line after markdown cell
        elif cell_type == 'code':
            # Keep code as is
            source = ''.join(source_lines)
            if source.strip():
                py_content.append(source.rstrip())
                py_content.append("")  # Add blank line after code cell
    
    # Write to .py file
    py_path = ipynb_path.replace('.ipynb', '.py')
    with open(py_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(py_content))
    
    print(f"Converted {ipynb_path} to {py_path}")

# Convert all .ipynb files
for ipynb_file in glob.glob("*.ipynb"):
    convert_ipynb_to_py(ipynb_file)

print("Conversion complete!")
