import open3d as o3d
import numpy as np


#  Зареждане на KITTI-360 LIDAR данни.
gt_cloud = np.fromfile('0000000779.bin', dtype=np.float32).reshape(-1, 4)[:, :3]  # XYZ само

#  Зареждане на реконструирани точки от DUST3R.
pcd = o3d.io.read_point_cloud('pointcloud_779.ply')
recon_cloud = np.asarray(pcd.points)

#  Подравняване на реконструирания облак.
source_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(recon_cloud))
source_pcd.rotate(source_pcd.get_rotation_matrix_from_xyz((np.pi / 2, np.pi / 2 + 0.2, np.pi)), center=(0, 0, 0))
source_pcd.scale(39, center=(0, 0, 0))
source_pcd.translate((0, 0, -0.5))
recon_cloud = np.asarray(source_pcd.points)

#  Визуалиация на двата облака.
gt_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(gt_cloud))
recon_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(recon_cloud))
gt_pcd.paint_uniform_color([1, 0, 0])  # Червено - Ground Truth KITTI-360
recon_pcd.paint_uniform_color([0, 0, 1])  # Синьо - Подравнен реконструиран облак от DUST3R
o3d.visualization.draw_geometries([gt_pcd, recon_pcd])
