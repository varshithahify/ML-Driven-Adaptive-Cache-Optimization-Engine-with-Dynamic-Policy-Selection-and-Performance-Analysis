# ==========================================
# AI CACHE OPTIMIZATION ENGINE
# MAIN PROGRAM
# ==========================================

from ml.dataset_generator import generate_dataset


print("========================================")
print(" AI CACHE OPTIMIZATION ENGINE")
print(" PHASE 6 - DATASET GENERATION")
print("========================================")

generate_dataset(
    samples=300,
    cache_size=5
)

print()
print("========================================")
print(" PHASE 6 COMPLETED")
print("========================================")