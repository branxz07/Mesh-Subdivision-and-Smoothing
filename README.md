# Mesh Subdivision and Smoothing

This project provides a Python script for reading, subdividing, and applying Laplacian smoothing to 3D mesh models in OBJ format. The script uses the `trimesh` library for handling 3D meshes and `numpy` for numerical operations.

## Features

- **OBJ File Reading**: Reads vertices and faces from an OBJ file.
- **Face Subdivision**: Subdivides the faces of a mesh while ensuring no duplicate vertices.
- **Laplacian Smoothing**: Applies Laplacian smoothing to the vertices of a mesh to create a smoother surface.
- **Visualize and Download**: Shows the final result after the subdivision and smoothing, and downloads the new OBJ.

## Requirements

- Python 3.x
- `numpy`
- `trimesh`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/branxz07/Mesh-Subdivision-and-Smoothing.git
    cd Mesh-Subdivision-and-Smoothing
    ```

2. Install the required packages:
    ```sh
    pip install numpy trimesh
    ```

## Usage

1. Place your OBJ file in the project directory. For example, `pumpkin_tall_10k.obj`.

2. Update the `objPath` variable in the script to the name of your OBJ file:
    ```python
    objPath = 'pumpkin_tall_10k.obj'
    ```

3. Run the script:
    ```sh
    python mesh_subdivision_and_smoothing.py
    ```

4. The script will generate a new OBJ file with the subdivided and smoothed mesh, named `Sub.obj` by default.

## Example

```python
# Path to the input OBJ file
objPath = 'pumpkin_tall_10k.obj'

# Read the OBJ file
vertices, faces = readObj(objPath)

# Subdivide the faces
subVertex, subFaces = subdivideFaces(vertices, faces)

# Apply Laplacian smoothing
smoothed_vertices = apply_laplacian_smoothing(subVertex, subFaces)

# Create a new mesh with smoothed vertices and subdivided faces
newObj = trimesh.Trimesh(vertices=smoothed_vertices, faces=subFaces)

# Path to the output OBJ file
output_file = 'Sub.obj'

# Export the new mesh to an OBJ file
newObj.export(output_file)

# Display the new mesh
newObj.show()

```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is free to use. You are free to use, modify, and distribute this code without any restrictions.

## Disclaimer

This project is provided "as is". Users of this code are responsible for understanding its functionality and implementing it appropriately in their own projects. While efforts have been made to ensure its reliability, users should exercise due diligence in testing and adapting the code to their specific needs. The authors and contributors are not liable for any outcomes resulting from the use of this code.

## Acknowledgements

* Thanks to [**Dr. Arturo Jafet Rodriguez Muñoz**](https://www.linkedin.com/in/arturojafet/?originalSubdomain=mx) for the initial idea based on the OBJ reader from the Raytracer project.
* Special thanks to Miguel Velez for implementation assistance and OpenAI-GPT-4 for providing an approximation of how to avoid duplicate vertices.
* Thanks to [@YahwthaniMG](https://github.com/YahwthaniMG) for help with coding and implementation of a lambda function adapted to the actual project.
