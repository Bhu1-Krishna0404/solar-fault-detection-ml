# solar-fault-detection-ml
Machine Learning-based fault detection system for identifying anomalies like partial shading and dirt in photovoltaic (PV) systems using electrical and environmental data.
# 🌞 Machine Learning-Based Fault Detection in Photovoltaic Systems

## 📌 Project Overview

Efficient and reliable operation of photovoltaic (PV) systems is vital for maximizing the potential of solar energy. This project presents a **machine learning-based fault detection system** for classifying and identifying faults—such as **partial shading** and **dirt accumulation**—in PV systems using only **electrical and environmental data**.

The aim is to provide a **cost-effective and automated fault detection solution** to improve the reliability and performance of PV systems.

---

## 🧠 Machine Learning Models Used

The following **supervised ML algorithms** were implemented and compared:

- 📈 Logistic Regression  
- 🌳 Decision Tree  
- 🌲 Random Forest  
- 📐 Support Vector Machine (SVM)  
- 🧠 Artificial Neural Network (ANN)

---

## 🧾 Dataset Description

The dataset includes the following **input features**:

- 📊 Voltage (V)
- ⚡ Current (I)
- 🌡️ Ambient Temperature (°C)
- ☀️ Solar Irradiance (W/m²)

**Target Labels** (Operating Conditions):
- ✅ Normal Operation  
- 🌥️ Partial Shading  
- 🧼 Dirt Accumulation  

---

## 🧹 Data Preprocessing Steps

- 🔄 **Normalization** of numerical features  
- 🔖 **Label Encoding** for class labels  
- ✂️ **Train-Test Split** (typically 80:20 or 70:30)

---

## 📊 Evaluation Metrics

Each model was evaluated using:

- ✅ Accuracy  
- 🎯 Precision  
- 🔁 Recall  
- 📏 F1-Score  
- 🧮 Confusion Matrix  

---

## 🧪 Experimental Results

- All models performed well when tested on data from the **same PV system** used for training.
- **ANN achieved the highest accuracy**, with **precision > 98%**.
- However, performance **degraded** when tested on data from a **different PV system**, emphasizing the **importance of system-specific training**.

---

## 🔍 Key Findings

- **ANN outperformed** other classifiers in accuracy and robustness.
- System-specific training is **critical** for optimal fault detection.
- Machine Learning provides a **scalable and low-cost** solution for PV system monitoring.

---

## ✅ Requirements
 Python 3.8+

pandas

numpy

scikit-learn

matplotlib

seaborn

tensorflow / keras (for ANN)

## 📌 Future Enhancements
Add real-time fault detection capability.

Explore transfer learning or domain adaptation to handle data from different PV systems.

Integrate into an IoT monitoring platform.

## 📬 Contact
If you have any questions or suggestions, feel free to reach out!



## 📄 License
This project is licensed under the MIT License.

---

Would you like me to generate a sample `requirements.txt` file or code template for any specific model (e.g., ANN or Random Forest)?

