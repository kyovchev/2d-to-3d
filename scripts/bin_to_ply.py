import numpy as np
import open3d as o3d


point_cloud = np.fromfile("0000000854.bin", dtype=np.float32).reshape(-1, 4)[:, :3]  # x, y, z
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud)
o3d.io.write_point_cloud("kitti360_converted.ply", pcd)
