# 2D to 3D image AI conversion

## Installation of DUSt3R: https://github.com/naver/dust3r

1. `cd` to the cloned root folder of this repo

2. Clone DUSt3R. Note: it is cloned to `dust3r` folder which is gitignored

   ```
   git clone --recursive https://github.com/naver/dust3r
   ```

3. Create new conda environment

   ```
   conda create -n dust3r python=3.9
   conda activate dust3r
   ```

4. Install PyTorch as described here [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) or if you have CUDA: `pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126`

5. Install DUSt3R requirements:

   ```
   cd dust3r
   pip install -r requirements.txt
   ```

6. Install the optional requirements: `pip install -r requirements_optional.txt`

7. You can make the dust3r a package within the local environment by copying the content of `make-package` folder to the cloned `dust3r` folder and then install it to the environment by executing `pip install -e .` from the outer dust3r folder.

8. Install Jupyter: `pip install jupyter`

9. Execute the example notebook [`./notebooks/test-DUSt3R.ipynb`](./notebooks/test-DUSt3R.ipynb) to validate that DUSt3R is installed correctly:

   ```
   cd notebooks
   jupyter-lab
   ```

   Open the notebook `test-DUSt3R.ipynb` and execute all cells.

## Run the demo

```
conda activate dust3r
cd dust3r
python demo.py --model_name DUSt3R_ViTLarge_BaseDecoder_512_dpt`
```

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

## Possible things to do

Go to [TODO.md](./TODO.md).

## Experiments plan

Possible experiments plan can be found in [EXPERIMENTS_PLAN.md](./EXPERIMENTS_PLAN.md).
