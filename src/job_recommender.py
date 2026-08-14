def recommend_roles(skills):

    roles = []

    if "python" in skills and "machine learning" in skills:
        roles.append("Machine Learning Engineer")

    if "python" in skills and "sql" in skills:
        roles.append("Data Analyst")

    if "deep learning" in skills:
        roles.append("AI Engineer")

    if "power bi" in skills:
        roles.append("Business Intelligence Analyst")

    if not roles:
        roles.append("Software Developer")

    return roles