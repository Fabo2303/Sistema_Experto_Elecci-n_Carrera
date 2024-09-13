def inference_engine(input_data, knowledge_base):
    recommendations_dict = {}

    for rule in knowledge_base:
        conditions = rule['conditions']
        match_count = sum(1 for cond, value in conditions.items() if input_data.get(cond, None) == value)

        if match_count >= 3:
            career = rule['career']
            recommendations_dict[career] = recommendations_dict.get(career, 0) + match_count

    sorted_recommendations = sorted(recommendations_dict.items(), key=lambda x: x[1], reverse=True)

    top_recommendations = [(career, count) for career, count in sorted_recommendations[:3]]

    return top_recommendations
