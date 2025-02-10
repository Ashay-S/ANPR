# Training Steps

Steps required to train the **Detection** and **Recognition** models using PaddleOCR.

## Steps to Train Detection and Recognition Models

### 1. Clone the Repository
Clone the PaddleOCR repository to your local machine:
```bash
git clone https://github.com/PaddlePaddle/PaddleOCR.git
cd PaddleOCR
```

### 2. Create a Virtual Environment
To avoid dependency issues, it is recommended to create a virtual environment:
```bash
python -m venv paddleocr_env
paddleocr_env\Scripts\activate     # Windows
```

### 3. Install Dependencies
Install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Prepare Your Dataset
Ensure your dataset follows the format specified here:  
[PaddleOCR Dataset Format](https://paddlepaddle.github.io/PaddleOCR/main/en/datasets/ocr_datasets.html)

You can also use the dataset provided in [this](https://drive.google.com/drive/folders/1ANYjE6saMmWwSJBYo7p23_A0yhIHimfL?usp=drive_link) link.

### 5. Download Pretrained Models
Download and extract the pretrained models from Google or copy them into the `PaddleOCR` directory from the provided Google Drive link.

### 6. Create Output Directory
Manually create the output directory where the model will be saved. PaddleOCR does not create the directory automatically, and this is necessary for saving the trained model.

### 7. Train Detection Model
Update the `.yml` file for the detection model in the PaddleOCR directory located at `configs/det/det_db.yml`.  
Then, run the following command to start training the detection model:
```bash
python tools/train.py -c configs/det/det_db.yml
```

### 8. Train Recognition Model
Update the `.yml` file for the recognition model in the PaddleOCR directory located at `configs/rec/rec_icdar15.yml`.  
Then, run the following command to start training the recognition model:
```bash
python tools/train.py -c configs/rec/rec_icdar15.yml
```

## Additional Notes

- If your dataset is in the **ICDAR 2015 format**, you can convert it using the provided Python scripts from this [site](https://rrc.cvc.uab.es/?ch=4&com=downloads).

---
