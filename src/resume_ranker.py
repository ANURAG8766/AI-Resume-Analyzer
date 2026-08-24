def rank_resume(score):

    if score >= 90:
        return "🏆 Industry Ready"

    elif score >= 75:
        return "🥇 Advanced"

    elif score >= 60:
        return "🥈 Intermediate"

    else:
        return "🥉 Beginner"