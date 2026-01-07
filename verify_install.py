from autopx.core.autopx import AutoPX

print("Import successful.")

texts = [
    "This is a simple test.", 
    "AutoPX seems to be working! \U0001F600",
    "Hum testing kar rahe hain."
]

print("Initializing AutoPX...")
auto = AutoPX()

print("Running fit_transform...")
vectors = auto.fit_transform(texts)
print(f"Vectors generated (Type: {type(vectors)})")

print("Generating report...")
print(auto.report("markdown"))
print("Verification complete.")
