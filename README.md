# Training Steps

## Prerequisites

Ensure that you have the following installed:

1. **PaddlePaddle**: The core deep learning framework used in PaddleOCR. Follow the installation instructions on the [PaddlePaddle website](https://www.paddlepaddle.org.cn/install/quick) for your system.
   
2. **PaddleOCR**: You can install it directly via pip:
   ```bash
   pip install paddlepaddle paddleocr
   ```

3. **Python**: Python 3.7 or later.

4. **Dependencies**:
   Install all the required Python dependencies with the following command:
   ```bash
   pip install -r requirements.txt
   ```

---

## Steps to Train Detection and Recognition Models

### 1. Clone the Repository
Clone the PaddleOCR repository to your local machine:
```bash
git clone https://github.com/PaddlePaddle/PaddleOCR.git
cd PaddleOCR
```

### 2. Create a Virtual Environment
To avoid dependency issues, it is recommended to create a virtual environment:


### 3. Prepare Your Dataset
Ensure your dataset follows the format specified here: [PaddleOCR Dataset Format](https://paddlepaddle.github.io/PaddleOCR/main/en/datasets/ocr_datasets.html)

You can also use the dataset provided in [this Google Drive link](https://drive.google.com/drive/folders/1ANYjE6saMmWwSJBYo7p23_A0yhIHimfL?usp=drive_link).

### 4. Download Pretrained Models
Download and extract the pretrained models from Google or copy them into the `PaddleOCR` directory from the provided Google Drive link.

### 5. Create Output Directory
Manually create the output directory where the model will be saved. PaddleOCR does not create the directory automatically, and this is necessary for saving the trained model.

### 6. Train Detection Model
Update the `.yml` file for the detection model in the PaddleOCR directory located at `configs/det/det_db.yml`.  
Then, run the following command to start training the detection model:
```bash
python tools/train.py -c configs/det/det_db.yml
```

### 7. Train Recognition Model
Update the `.yml` file for the recognition model in the PaddleOCR directory located at `configs/rec/rec_icdar15.yml`.  
Then, run the following command to start training the recognition model:
```bash
python tools/train.py -c configs/rec/rec_icdar15.yml
```

---

## Additional Notes

- If your dataset is in the [ICDAR format](https://rrc.cvc.uab.es/?ch=4&com=downloads), you can convert it using the provided Python scripts as instructed from this [site](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/model_train/training.html) for both recognition and detection models. Otherwise, data egenrated from the python notebook is already generated in the desired format, no need for any change other than the file save loaction.
- Recommended Versions of a few libraries:
  - paddleocr 2.5
  - paddlepaddle-gpu 2.5.0
  - CUDA 11.4 or above (I used 11.8)
- You an find all the pre trained models [here](https://paddleclas-en.readthedocs.io/en/latest/models/models_intro_en.html).

---
