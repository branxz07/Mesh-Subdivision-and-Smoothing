# CODE BY BRANDON MAGAÑA AVALOS

import numpy as np
import trimesh  # Pre-install trimesh before running the code "pip install trimesh"

def readObj(obj):
    """
    Reads an OBJ file and extracts vertices and faces.

    Parameters:
    obj (str): Path to the OBJ file.

    Returns:
    tuple: A tuple containing two numpy arrays, one for vertices and one for faces.
    """
    vertices = []
    faces = []
    with open(obj, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0] == 'v':
                vertices.append(list(map(float, parts[1:4])))
            elif parts[0] == 'f':
                face = [int(p.split('/')[0]) - 1 for p in parts[1:]]
                faces.append(face)
    return np.array(vertices), np.array(faces)


def subdivideFaces(vertices, faces):
    """
    Subdivides the faces of a mesh and ensures no duplicate vertices by checking shared midpoints.

    Parameters:
    vertices (numpy array): Array of vertices.
    faces (numpy array): Array of faces.

    Returns:
    tuple: A tuple containing two numpy arrays, one for new vertices and one for new faces.
    """
    newVertices = vertices.tolist()
    newFaces = []
    # Dictionary to store midpoints to ensure no duplicates
    edgeMidpoints = {}

    for face in faces:
        faceVertices = []
        for i in range(3):
            start, end = face[i], face[(i + 1) % 3]
            edge = tuple(sorted((start, end)))

            # If the edge is not already in the dictionary, create the new vertex.
            if edge not in edgeMidpoints:
                midpoint = (vertices[start] + vertices[end]) / 2
                edgeMidpoints[edge] = len(newVertices)
                newVertices.append(midpoint)

            faceVertices.append(edgeMidpoints[edge])

        v0, v1, v2 = face
        # Midpoints of the edges v0-v1, v1-v2, v2-v0
        m0, m1, m2 = faceVertices  

        # Add the new faces to the existing ones, ensuring no duplicate faces
        newFaces.extend([[v0, m0, m2], [v1, m1, m0], [v2, m2, m1], [m0, m1, m2]])

    return np.array(newVertices), np.array(newFaces)


def apply_laplacian_smoothing(vertices, faces, iterations=4, factor=0.6):
    """
    Applies Laplacian smoothing to the vertices of a mesh.

    Parameters:
    vertices (numpy array): Array of vertices.
    faces (numpy array): Array of faces.
    iterations (int): Number of smoothing iterations. Default is 4.
    factor (float): Smoothing factor. Default is 0.6.

    Returns:
    numpy array: Array of smoothed vertices.
    """
    smoothed_vertices = vertices.copy()
    adjacency_matrix = [[] for _ in range(len(vertices))]

    for face in faces:
        for i in range(3):
            v1, v2 = face[i], face[(i + 1) % 3]
            adjacency_matrix[v1].append(v2)
            adjacency_matrix[v2].append(v1)

    for _ in range(iterations):
        for i, vertex in enumerate(vertices):
            neighbors = set(adjacency_matrix[i])  
            if neighbors:
                avg_neighbor_pos = np.mean(vertices[list(neighbors)], axis=0)
                smoothed_vertices[i] = (1 - factor) * vertex + factor * avg_neighbor_pos

    return smoothed_vertices


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