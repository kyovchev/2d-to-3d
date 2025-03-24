import trimesh
import numpy as np


scene = trimesh.load("scene_779.glb")
point_cloud = []
for geom in scene.geometry.values():
    if isinstance(geom, trimesh.Trimesh):  # check if mesh
        point_cloud.append(geom.vertices)  # vertices only (w/o faces)
points = np.vstack(point_cloud)
point_cloud_trimesh = trimesh.PointCloud(points)
point_cloud_trimesh.export("pointcloud_779.ply")
