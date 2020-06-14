# Localization and Classification

This work object localization and classification of nanocrystal active sites in transmission electron microscopy images. Our first simple goal is to automate particle size and facet analysis, which can be done slowly by humans already. This was achieved by fine-tuning a SSD-Inception_v2 model, and we demontrate high mAP values.

<p align="center">
  <img width="600" height="314" src="NanoparticleDetectionComparison.jpg">
</p>

### Directory Setup

```
├── workingspace
│   ├── training_demo
│       ├── images
│           ├── train
│           ├── test
│       ├── pre-trained-model (SSD_Inception_v2)
│       ├── trained-inference-graph
│           ├── output_interence_graph.pb
│       ├── annotations (stores all .xml files)
│       ├── training (stores model checkpoints)
│           ├── ssd_inception_v2_coco.config (config file)
├── object_detection_scripts (generating .csv's and .record's)
│   ├── xml_to_csv.py
│   ├── generate_tfrecord.py
├── models
│   ├── research
│       ├── object_detection
│           ├── train
```
### Prerequisites
* Python (version >= 3.5)
* Tensorflow (version 1.14)

### Documentation

* Detection.ipynb - Comprehensive notebook including .csv and .record generation, GPU-training, and testing
* xml_to_csv.py - Python script to convert folder of .xml files to a .csv file
* generate_tfrecord.py - Python script to convert .csv file to .record file
* train.py - Python script to train model
* export_inference_graph.py - Export graph after model is finished training
