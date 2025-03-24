# 2D to 3D image AI conversion

## Installation of DUST3R: https://github.com/naver/dust3r

Clone DUSt3R

```
git clone --recursive https://github.com/naver/dust3r
cd dust3r
```

Create conda environment with python=3.11

```
conda activate <environment-name>
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia # use the correct version of cuda for your system
pip install -r requirements.txt
```

Optional: `pip install -r requirements_optional.txt`

## Run the demo

`python demo.py --model_name DUSt3R_ViTLarge_BaseDecoder_512_dpt`

## KITTI-360

Download from https://www.cvlibs.net/datasets/kitti-360/download.php:
https://s3.eu-central-1.amazonaws.com/avg-projects/KITTI-360/6489aabd632d115c4280b978b2dcf72cb0142ad9/data_3d_semantics.zip
https://s3.eu-central-1.amazonaws.com/avg-projects/KITTI-360/data_2d_raw/2013_05_28_drive_0003_sync_image_00.zip
https://s3.eu-central-1.amazonaws.com/avg-projects/KITTI-360/data_2d_raw/2013_05_28_drive_0003_sync_image_01.zip
https://s3.eu-central-1.amazonaws.com/avg-projects/KITTI-360/data_3d_raw/2013_05_28_drive_0003_sync_velodyne.zip

## Experiments

### Install additional libs

```
pip install open3d
pip install pykitti
```

### Download

https://download.europe.naverlabs.com/ComputerVision/DUSt3R/DUSt3R_ViTLarge_BaseDecoder_512_dpt.pth to checkpoints

### Scripts

- `bin_to_ply.py` - converts KITTI-360 scan file to pointcloud ply
- `glb_to_ply.py` - converts GLB scene downloaded from the demo with only Transparent cameras checked
- `viz_ply.py` - visualizes point cloud file
- `test_779.py` - compares DUSt3R output for frame 0000000779 from 2013_05_28_drive_0003_sync with KITTI-360 scan ground truth
- `test_854.py` - compares DUSt3R output for frame 0000000854 from 2013_05_28_drive_0003_sync with KITTI-360 scan ground truth
