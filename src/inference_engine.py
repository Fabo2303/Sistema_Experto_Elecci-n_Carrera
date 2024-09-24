def inference_engine(input_data, knowledge_base):
    recommendations_dict = {}

    for rule in knowledge_base:
        conditions = rule['conditions']
        match_count = 0

        # si es un arreglo debe comparar uno por uno
        for cond, value in conditions.items():
            # genero ['animacion', 'comedia', 'drama']
            # si value es un conjunto entonces debemos comparar uno por uno con input_data
            if isinstance(value, list):
                for v in value:
                    print(input_data.get(cond, '').split(','))
                    if v in input_data.get(cond, '').split(','):
                        match_count += 1
                        break
            else:
                if value == input_data.get(cond, ''):
                    match_count += 1

        # Si hay 3 o más coincidencias, agregar la carrera (en este caso, la película) a las recomendaciones
        if match_count >= 3:
            movie_data = rule['career'].strip('{}').split(',')
            movie_title = movie_data[0].strip()
            movie_link = movie_data[1].strip()
            recommendations_dict[movie_title] = {
                'matches': match_count,
                'link': movie_link
            }

    # Ordenar recomendaciones por coincidencias
    sorted_recommendations = sorted(recommendations_dict.items(), key=lambda x: x[1]['matches'], reverse=True)

    # Obtener las tres mejores recomendaciones
    top_recommendations = [(movie, details['link'], details['matches']) for movie, details in
                           sorted_recommendations[:3]]

    return top_recommendations
