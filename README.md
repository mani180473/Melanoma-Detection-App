# Melanoma Detection Web Application

A Flask-based web application that uses deep learning to classify skin lesions as benign or malignant melanoma.

## 🚀 Features

- **Web Interface**: User-friendly web application for uploading skin lesion images
- **AI Classification**: Deep learning model based on ResNet50 architecture
- **Real-time Results**: Instant prediction with confidence scores
- **Image Processing**: Automatic image resizing and preprocessing

## 📁 Project Structure

```
melanoma-detection/
├── app.py                 # Main Flask application
├── mel.py                 # Model training script
├── melanoma_model.h5      # Trained model (not included in repo)
├── templates/
│   └── index.html        # Web interface
├── static/
│   └── uploads/          # Uploaded images storage
├── venv/                 # Virtual environment (not included)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/melanoma-detection-app.git
   cd melanoma-detection-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install flask tensorflow scikit-learn matplotlib numpy pillow
   ```

5. **Download the model**
   ```bash
   python download_model.py
   ```
   - The model file (679MB) will be downloaded automatically
   - Alternatively, train your own model using `mel.py`

## 🚀 Running the Application

1. **Activate virtual environment**
   ```bash
   venv\Scripts\activate  # Windows
   ```

2. **Run the Flask app**
   ```bash
   python app.py
   ```

3. **Open your browser**
   - Go to: `http://127.0.0.1:5000` or `http://localhost:5000`

## 🧠 Model Training

To train your own model:

1. **Prepare your dataset**
   - Organize images in folders: `train/benign/`, `train/malignant/`, `test/benign/`, `test/malignant/`
   - Update paths in `mel.py`

2. **Run training script**
   ```bash
   python mel.py
   ```

3. **Model will be saved as `melanoma_model.h5`**

## 📊 Model Architecture

- **Base Model**: ResNet50 (pre-trained on ImageNet)
- **Custom Layers**: 
  - Flatten layer
  - Dropout (0.5)
  - Dense layer (512 units, ReLU)
  - Output layer (2 units, softmax)
- **Optimizer**: Adam (learning rate: 1e-4)
- **Loss**: Categorical crossentropy

## 🎯 Usage

1. **Upload Image**: Click "Choose File" and select a skin lesion image
2. **Analyze**: Click "Predict" to run the AI analysis
3. **View Results**: See the prediction (benign/malignant) with confidence score

## ⚠️ Important Notes

- **Medical Disclaimer**: This tool is for educational/research purposes only
- **Not Medical Advice**: Always consult healthcare professionals for medical decisions
- **Model Limitations**: Performance depends on training data quality and quantity

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with Flask and TensorFlow
- Uses ResNet50 architecture
- Inspired by medical AI applications

---

**Note**: The trained model file (`melanoma_model.h5`) will be automatically downloaded when you run `python download_model.py`. The model is hosted on Google Drive for easy access. 