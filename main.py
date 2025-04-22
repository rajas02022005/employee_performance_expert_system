def evaluate_performance(attendance, task_completion, punctuality, peer_review):
    if attendance > 90 and task_completion > 85 and punctuality > 7 and peer_review > 7:
        return "Excellent"
    elif attendance > 80 and task_completion > 75 and punctuality > 6 and peer_review > 6:
        return "Good"
    elif attendance > 70 and task_completion > 65 and punctuality > 5 and peer_review > 5:
        return "Average"
    else:
        return "Needs Improvement"

def main():
    print("=== Employee Performance Evaluation Expert System ===\n")

    # Get user inputs
    try:
        attendance = float(input("Enter attendance percentage (0-100): "))
        task_completion = float(input("Enter task completion percentage (0-100): "))
        punctuality = float(input("Enter punctuality score (0-10): "))
        peer_review = float(input("Enter peer review score (0-10): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Evaluate
    result = evaluate_performance(attendance, task_completion, punctuality, peer_review)

    # Output
    print(f"\nPerformance Rating: {result}")

if __name__ == "__main__":
    main()
