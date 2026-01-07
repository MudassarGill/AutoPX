from autopx import AutoPX

# Short, sentiment-focused texts
texts = [
    "I am so happy today! 😄",
    "This product is terrible... 😡",
    "Aap ka kaam bohat acha hai! 👍",
    "Main bohat udaas hoon 😔"
]

# Initialize AutoPX with automatic task inference
autopx_pipeline = AutoPX(task=None, model_type="ml")

# Preprocess texts
vectors, report = autopx_pipeline.preprocess(texts)

# Print vectors for verification
try:
    print("Vectors shape:", vectors.shape)
except AttributeError:
    print("Vectors length:", len(vectors))

# Generate a JSON report for structured inspection
json_report = autopx_pipeline.get_report(format="json")
print("\nJSON Report:\n", json_report)
