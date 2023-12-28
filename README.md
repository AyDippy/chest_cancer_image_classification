# Chest Cancer Image Classification

![Chest Cancer Image](https://images.unsplash.com/photo-1579544757872-ce8f6af30e0f?q=80&w=2037&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

This repository contains the code, resources, and a pre-trained model for a chest cancer image classification project. The goal of this project is to classify chest CT scan images into four different classes: Adenocarcinoma, Large cell carcinoma, Squamous cell carcinoma, and Normal cell.

## Dataset

The dataset used for this project is available on Kaggle. You can find it [here](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images). It consists of three main folders:

- `train`: Contains training images organized into four classes.
- `test`: Contains test images.
- `validation`: Contains validation images.

## Preprocessing

Image preprocessing is an essential step in preparing the data for model training. In this project, we used the following preprocessing steps:

- Image resizing to 224x224 pixels.
- Batch normalization.
- Data augmentation using ImageDataGenerator with a batch size of 32.

## Model

Transfer learning was employed in this project, utilizing the ResNet50 architecture as the base model. The model architecture includes:

- ResNet50 base model.
- Batch normalization layers.
- Flatten layer.
- Dense layers with dropout for predictions based on the four classes.

## Training

The model was trained for 50 epochs with a callback function for learning rate reduction. The achieved accuracy on the validation set is approximately 85%.

## Pre-trained Model

The pre-trained model for chest cancer classification is available in the repository as `chest_cancer_detector.h5`.

## Streamlit App

You can interact with the deployed Streamlit app for this project [here](https://chestcancerimageclassification-wyvfqfnsmcnmmpzn9dwpta.streamlit.app/).

## Requirements

The required Python libraries and packages are listed in the `requirements.txt` file. You can install them using the following command:

**pip install -r requirements.txt**


## Author

- **Dipeolu Ayomide**

## License

This project does not have a specified license. Please check with the project author for usage rights and permissions.

## Acknowledgments

- Kaggle for providing the dataset.
- The Streamlit community for app deployment resources.
- The creators of ResNet50 for the pre-trained model.



