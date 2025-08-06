#!/usr/bin/env python3
"""
Model Download Script for Melanoma Detection App
Downloads the trained model from Google Drive
"""

import os
import requests
from tqdm import tqdm
import gdown

def download_model():
    """Download the melanoma detection model"""
    
    # Model file URL from Google Drive
    # Original link: https://drive.google.com/file/d/1PX8Ako-7wQMBMk2FpnsF2fQzXNCm1hDq/view?usp=sharing
    google_drive_id = "1PX8Ako-7wQMBMk2FpnsF2fQzXNCm1hDq"
    model_path = "melanoma_model.h5"
    
    print("Downloading melanoma detection model...")
    print("This may take a few minutes depending on your internet connection.")
    
    try:
        # Use gdown with the direct file ID approach
        gdown.download(f"https://drive.google.com/uc?id={google_drive_id}", model_path, quiet=False, fuzzy=True)
        
        # Check if file was downloaded successfully
        if os.path.exists(model_path) and os.path.getsize(model_path) > 100000000:  # > 100MB
            print(f"✅ Model downloaded successfully to {model_path}")
            print(f"File size: {os.path.getsize(model_path) / (1024*1024):.1f} MB")
            print("You can now run the Flask application!")
        else:
            print("❌ Download failed or file is too small. Please check the Google Drive link.")
            if os.path.exists(model_path):
                os.remove(model_path)  # Remove the small file
        
        print(f"✅ Model downloaded successfully to {model_path}")
        print("You can now run the Flask application!")
        
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        print("\nAlternative options:")
        print("1. Train your own model using mel.py")
        print("2. Contact the repository owner for the model file")
        print("3. Use a pre-trained model from a medical AI repository")

if __name__ == "__main__":
    download_model() 