# Image-Matrix-Processing
Ye project images ko NumPy arrays (matrices) mein convert karta hai aur phir un par mathematical operations apply kar ke brightness aur contrast adjust karta hai
🖼️ Image Processing via Matrix Manipulation
A sophisticated Python tool that treats images as Numerical Matrices (NumPy Arrays) to perform low-level image enhancement. This project is a core part of my Numerical Computing portfolio.

🚀 Overview
Standard image editing tools use high-level APIs, but this project dives into the Mathematics of Pixels. By converting images into NumPy arrays, we can manipulate brightness and contrast through direct matrix arithmetic.

🛠️ Key Features
Image-to-Matrix Conversion: Seamlessly transform .png/.jpg files into multi-dimensional arrays.

Brightness Optimization: Implemented through scalar addition/subtraction across the pixel matrix.

Contrast Enhancement: Achieved via matrix multiplication to scale pixel intensities.

Real-time Processing: Fast execution using optimized NumPy broadcasting.

📁 Project Structure
image_matrix.py: The engine behind the processing logic.

ss.png: Original input source.

bright_ss.png: Output demonstrating increased luminosity.

contrast_ss.png: Output demonstrating refined pixel variance.

💻 Tech Stack
Language: Python 3.x

Libraries: NumPy, OpenCV (cv2)
