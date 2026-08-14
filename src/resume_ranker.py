def rank_resume(score):

    if score >= 85:
        return "A+ (Excellent)"

    elif score >= 70:
        return "A (Very Good)"

    elif score >= 55:
        return "B (Good)"

    elif score >= 40:
        return "C (Needs Improvement)"

    else:
        return "D (Poor)"