# Pose annotator
A simple GUI for clicking on keypoints for training pose estimation models. Currently only supports one set of 
points per frame. Please consider contributing for multiple instances per frame!

## Installation
Run: 
* `git clone https://github.com/athp18/pose_annotator/`
* `cd pose_annotator`
* `pip install --upgrade pip setuptools`
* `pip install -e .`

## Usage
Customize [default_config.yaml](pose_annotator/gui/default_config.yaml) then launch using
 `pose_annotator user_cfg=path/to/custom/config.yaml` 
 
#### Hotkeys 
* `Ctrl+S` save
* `Right` next frame
* `Left` previous frame
* `Down` next keypoint
* `Space` next keypoint
* `Up` previous keypoint
* `Delete` delete keypoint

 

## Known issues
* Adding or deleting images from a directory with existing annotations
	* annotations are matched to image files by rank-order of the filename
* `ModuleNotFoundError: No module named 'skbuild'`
  * please `pip install --upgrade pip`
