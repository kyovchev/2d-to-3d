import open3d as o3d


point_cloud = o3d.io.read_point_cloud("pointcloud_779.ply")
o3d.visualization.draw_geometries([point_cloud], window_name="Point Cloud Viewer")