from autopx import AutoPX, ModelType

def run_example():
    texts = [
        "I love this tool! 😄",
        "یہ ایک بہترین لائبریری ہے",
        "Bohat achi quality hai is ki"
    ]
    
    auto = AutoPX(model_type=ModelType.ML)
    vectors, report = auto.preprocess(texts)
    
    print("Vectors type:", type(vectors))
    try:
        print("Vectors shape:", vectors.shape)
    except AttributeError:
        print("Vectors length:", len(vectors))
    
    print("\nProcessing Report (JSON):\n", report)

if __name__ == "__main__":
    run_example()
