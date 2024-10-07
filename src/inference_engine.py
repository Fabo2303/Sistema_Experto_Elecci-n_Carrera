def inference_engine(input_data, knowledge_base):
    recommendations_dict = {}

    for rule in knowledge_base:
        conditions = rule['conditions']
        match_count = 0
        for cond, value in conditions.items():
            if isinstance(value, list):
                for v in value:
                    if v in input_data.get(cond, '').split(','):
                        match_count += 1
            else:
                if value == input_data.get(cond, ''):
                    match_count += 1

        if match_count >= 3:
            movie_data = rule['movie'].strip('{}').split(',')
            movie_title = movie_data[0].strip()
            movie_link = movie_data[1].strip()
            recommendations_dict[movie_title] = {
                'matches': match_count,
                'link': movie_link
            }

    sorted_recommendations = sorted(recommendations_dict.items(), key=lambda x: x[1]['matches'], reverse=True)

    top_recommendations = [(movie, details['link'], details['matches']) for movie, details in
                           sorted_recommendations[:3]]

    return top_recommendations
