from transformers import pipeline

def decide(log_text):
    agent = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

    actions = [
        "RETRY BUILD",
        "NOTIFY DEVELOPER",
        "BLOCK MERGE"
    ]

    result = agent(log_text, candidate_labels=actions)
    return result["labels"][0]


if __name__ == "__main__":
    with open("logs/dependency_check.log", "r") as f:
        log = f.read()

    decision = decide(log)
    print("\nAGENT DECISION:", decision)
