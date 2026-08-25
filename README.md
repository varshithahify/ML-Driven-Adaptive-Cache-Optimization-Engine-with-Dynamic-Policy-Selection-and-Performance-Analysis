**ML-Driven Adaptive Cache Optimization Engine with Dynamic Policy Selection and Performance Analysis**

An ML-based system that analyzes memory-access workloads and predicts a suitable cache replacement policy to improve simulated cache performance.

## 🎯 Problem Statement

Traditional cache systems generally use a fixed cache replacement policy such as LRU, FIFO, or LFU.
However, different memory-access workloads have different characteristics. A policy that performs well for one workload may perform poorly for another.
This project addresses this problem by analyzing workload characteristics and using Machine Learning to predict a suitable cache replacement policy dynamically.

## 🎯 Objective

The main objectives of this project are:
- Simulate different cache replacement policies.
- Generate different memory-access workloads.
- Extract meaningful workload characteristics.
- Generate a dataset for Machine Learning.
- Train and compare ML classification models.
- Predict a suitable cache replacement policy for a new workload.
- Evaluate the selected policy using hit rate, miss rate, energy, and latency.

  ## ⚙️ How It Works

```text
Memory Access Workload
          ↓
   Feature Extraction
          ↓
      ML Dataset
          ↓
   Model Training
          ↓
 Decision Tree / Random Forest
          ↓
  Predicted Cache Policy
          ↓
    Cache Simulation
          ↓
 Performance Evaluation
          ↓
Hit Rate | Miss Rate | Energy | Latency
```
---
## 🧠 Cache Replacement Policies

The project implements:

| Policy | Description |
|--------|-------------|
| LRU | Removes the least recently used cache entry |
| FIFO | Removes the oldest cache entry |
| LFU | Removes the least frequently used cache entry |
| LRU-OPT | Optimized LRU implementation |

## 🔄 Workload Types
The simulator supports different memory-access patterns:
- **Sequential** — accesses memory locations in a sequential pattern.
- **Repetitive** — repeatedly accesses a small set of memory locations.
- **Random** — accesses memory locations randomly.
- **Mixed** — combines different access patterns.

## 🧮 Feature Engineering

The system extracts four workload features:

| Feature | Description |
|---------|-------------|
| Unique Count | Number of distinct memory locations |
| Repetition Ratio | Degree of repeated memory accesses |
| Sequentiality | Degree of sequential access behavior |
| Frequency Variance | Variation in access frequency among memory locations |

## 🤖 Machine Learning

Cache policy selection is treated as a multi-class classification problem.

### Input Features

- Unique Count
- Repetition Ratio
- Sequentiality
- Frequency Variance

### Target

```text
LRU
FIFO
LFU
LRU_OPT
```

---
## 📈 Model Results
| Model | Accuracy |
|-------|----------|
| Decision Tree | 45.00% |
| Random Forest | 46.67% |

Random Forest currently performs better on the generated dataset and is therefore selected as the prediction model.
The current accuracy is based on a synthetic dataset of 300 samples. Increasing workload diversity, dataset size, feature quality, and model tuning are planned improvements.

## 🔮 Example AI Prediction
For a newly generated workload:
```text
Unique Count       : 34
Repetition Ratio   : 0.66
Sequentiality      : 0.03
Frequency Variance : 12.78

Predicted Best Cache Policy : LFU
```

---
## 🏗️ System Architecture

                  ┌──────────────────┐
                  │ Workload Generator│
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │ Feature Extraction│
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │ ML Model         │
                  │ Decision Tree    │
                  │ Random Forest    │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │ Policy Prediction│
                  └────────┬─────────┘
                           ↓
              ┌──────────────────────────┐
              │ Cache Policy Simulation  │
              │ LRU | FIFO | LFU | LRU-OPT│
              └────────────┬─────────────┘
                           ↓
                  ┌──────────────────┐
                  │ Performance      │
                  │ Evaluation       │
                  └──────────────────┘



---

### 14. Project structure

Use your **actual structure**:

```markdown
## 📁 Project Structure

```text
ML-Driven-Adaptive-Cache-Optimization-Engine/
│
├── core/
│   └── policies.py
│
├── datasets/
│   └── dataset.csv
│
├── graphs/
│   ├── generate_graphs.py
│   ├── hit_rate.png
│   ├── miss_rate.png
│   ├── energy.png
│   └── latency.png
│
├── ml/
│   ├── dataset_generator.py
│   ├── evaluate_model.py
│   ├── features.py
│   ├── predictor.py
│   ├── train_decision_tree.py
│   └── train_random_forest.py
│
├── models/
│   └── cache_model.pkl
│
├── simulator/
│   ├── runner.py
│   └── workloads.py
│
├── main.py
├── test_features.py
└── README.md
```

## 🛠️ Tech Stack
**Language**
- Python

**Machine Learning**
- Scikit-learn
- Decision Tree
- Random Forest

**Data Processing**
- Pandas

**Model Serialization**
- Joblib

**Visualization**
- Matplotlib

**Development**
- VS Code
- Git
- GitHub

## ▶️ How to Run
1. Clone the repository
git clone https://github.com/varshithahify/ML-Driven-Adaptive-Cache-Optimization-Engine.git
cd ML-Driven-Adaptive-Cache-Optimization-Engine                  
2. Install dependencies
pip install pandas scikit-learn joblib matplotlib
3. Generate the dataset
python -m ml.dataset_generator
4. Train the ML models
Train the Decision Tree and Random Forest models and save the best-performing model as:
models/cache_model.pkl
5. Run the project
python main.py
6. Generate performance graphs
python -m graphs.generate_graphs

---
## 🚀 Development Phases
| Phase | Implementation |
|------|----------------|
| Phase 1 | Project Setup |
| Phase 2 | Basic Cache Policies |
| Phase 3 | Optimized LRU |
| Phase 4 | Workload Simulation |
| Phase 5 | Feature Extraction |
| Phase 6 | Dataset Generation |
| Phase 7 | ML Model Training |
| Phase 8 | Model Evaluation |
| Phase 9 | AI Policy Prediction |
| Phase 10 | AI Policy Integration |
| Phase 11 | Performance Visualization |

## ⚠️ Limitations
- The current dataset is synthetically generated.
- The current dataset contains 300 samples.
- Energy and latency are simulated cost metrics.
- Model accuracy depends on the generated workload distribution.
- The current system is a software simulation and does not directly control a physical CPU cache.

## 🔮 Future Improvements
- Increase dataset size and workload diversity.
- Add temporal locality and spatial locality features.
- Add cache size as an ML feature.
- Perform hyperparameter tuning.
- Use cross-validation for more reliable model evaluation.
- Evaluate additional ML algorithms.
- Support online workload monitoring.
- Integrate with realistic cache traces or hardware-level simulators.
- Explore dynamic cache-size optimization.

