from autopx import AutoPX, TaskType

def run_example():
    texts = [
        "This is amazing! ❤️",
        "Terrible experience, never again. 😡"
    ]
    
    # Explicitly setting task to sentiment
    auto = AutoPX()
    _, _ = auto.preprocess(texts, task=TaskType.SENTIMENT)
    
    print("Sentiment Preprocessing Report (JSON):")
    print(auto.get_report(format="json"))

if __name__ == "__main__":
    run_example()
