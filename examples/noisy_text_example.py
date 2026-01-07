from autopx import AutoPX

def run_example():
    texts = [
        "Check this out!!! http://bit.ly/12345",
        "Too many spaces     in between words.",
        "WEIRD capitalization patterns."
    ]
    
    auto = AutoPX()
    _, _ = auto.preprocess(texts)
    
    # Get explanation in Markdown
    md_report = auto.get_report(format="markdown")
    print("Markdown Report:\n", md_report)

if __name__ == "__main__":
    run_example()
