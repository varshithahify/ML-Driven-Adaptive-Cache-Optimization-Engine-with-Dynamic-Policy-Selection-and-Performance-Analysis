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
