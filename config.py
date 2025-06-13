"""Configuration for scoring and diagnostic thresholds.
Learning designers can tweak these values without modifying core code.
"""

# Similarity score required to accept the learner's diagnosis
DIAGNOSIS_THRESHOLD = 0.7

# Weight applied to questions exploring Ideas, Concerns and Expectations (ICE)
ICE_WEIGHT = 1.5

# Weight applied to symptom-based questions
SYMPTOM_WEIGHT = 1.0
