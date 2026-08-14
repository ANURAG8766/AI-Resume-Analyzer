def generate_questions(skills):

    questions = []

    if "python" in skills:
        questions.extend([
            "What is the difference between List and Tuple?",
            "What is a Python decorator?",
            "Explain OOP concepts in Python."
        ])

    if "sql" in skills:
        questions.extend([
            "Difference between WHERE and HAVING?",
            "What are JOINs in SQL?",
            "What is a Primary Key?"
        ])

    if "machine learning" in skills:
        questions.extend([
            "What is overfitting?",
            "Difference between Classification and Regression?",
            "What is Cross Validation?"
        ])

    if "deep learning" in skills:
        questions.extend([
            "What is CNN?",
            "What is RNN?",
            "Difference between TensorFlow and PyTorch?"
        ])

    return questions