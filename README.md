# Cyber Attack Classification Using Supervised Machine Learning

This project focuses on developing a machine learning-based system to classify network traffic cyber-attacks. By leveraging supervised algorithms such as Random Forest and Naïve Bayes, the system aims to accurately predict and categorize various cyber threats.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

With the increasing complexity and frequency of cyber-attacks, traditional security measures often fall short in timely detection and classification. This project addresses this challenge by implementing supervised machine learning techniques to analyze network traffic and identify potential threats in real-time.

## Features

- **Data Preprocessing:** Cleansing and preparing data for analysis.
- **Feature Extraction:** Identifying relevant attributes from network traffic data.
- **Model Training:** Utilizing algorithms like Random Forest and Naïve Bayes for classification.
- **Real-Time Deployment:** Implementing a Django-based web interface for monitoring and detection.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** Scikit-learn, Pandas, NumPy
- **Framework:** Django
- **Visualization:** Matplotlib, Seaborn

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ItsDarker/Cyber-Attack-Classification-Using-Supervised-ML.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd Cyber-Attack-Classification-Using-Supervised-ML
   ```
3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```
4. **Activate the Virtual Environment:**
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Unix or MacOS**:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
## Usage

### Data Preprocessing:
Use the `M1.ipynb` notebook to clean and preprocess the dataset.

### Feature Extraction:
Execute the `M2.ipynb` notebook to extract relevant features.

### Model Training:
Train models using the following notebooks:
- `M3 - GNB.ipynb` for Gaussian Naïve Bayes.
- `M4 - ADB.ipynb` for AdaBoost.
- `M5 - RFC.ipynb` for Random Forest.

### Model Deployment:
Deploy the trained model using Django as outlined in the `PROJECT` directory.

## Modules

1. **Data Preprocessing:**
   - Handling missing values and duplicates.
   - Variable identification and analysis.

2. **Feature Extraction:**
   - Data visualization and pattern recognition.

3. **Model Training:**
   - Implementation of supervised learning algorithms.

4. **Deployment:**
   - Integration with Django for real-time monitoring.

## Results

The Random Forest Classifier achieved the highest accuracy among the evaluated models. The deployed system effectively identifies various cyber-attacks, enhancing cybersecurity measures.

## Future Work

- **Cloud Deployment:** Explore deploying the system on cloud platforms for scalability.
- **IoT Integration:** Optimize the system for Internet of Things environments.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgements

Special thanks to the team members and contributors who made this project possible.

