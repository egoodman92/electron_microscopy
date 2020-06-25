# Material Classification

This work studies the classification and interpretation of ten different materials based on their nanoscale images. The goal is to distinguish between various oxide nanomaterials, composed of different elements or even the same element but different morphology.

<p align="center">
  <img width="500" height="540" src="ClassActivationMap.jpg">
</p>

### Directory Setup

```
├── train
│   ├── Al2O3
│   ├── ...
│   └── TiO2
├── validation
│   ├── Al2O3
│   ├── ...
│   └── TiO2
├── ten_class_weights (stored via callbacks)
├── 10supports_ClassActivationMapsCAMs.ipynb
├── SupportClassification_FineTuning_10Supports_Callbacks.ipynb
```

### Image Preprocessing
Model training and fine-tuning done on dataset of electron microscopy images collected over 5 years and 12 students. For each material class (i.e. CeO2) a folder containing subfolders of each synthesized material is organized. All .dm3 files are pooled together and are converted simultaneously to .jpgs prevent unique conversion artifacts (i.e. different scalebar or contrast settings). Full images are screened 1-by-1 to make sure there are no similar images (which would be a problem if image appeared in both training and test data). Then, folder of .jpgs are split into quadrants using image_subcrops.py, and the original full-size images are discarded. From this dataset, every third image is selected and placed into a folder for test images (every third image was chosen to remove artificats from only choosing a specific quadrant). Finally, the validation data is quickly screened to remove poor images (i.e. empty field, only lacey C, or too high magnification.

### Prerequisites

* Python (version >= 3.5)
* Tensorflow (version 2.2.0)

### Documentation

* 10_supportsClassActivationMapsCAMs.ipynb - Python notebook for interpretation of material classification
* SupportClassification_FineTuning_10Supports_Callbacks.ipynb - Python notebook for fine-tuning various models using augmentation etc.


