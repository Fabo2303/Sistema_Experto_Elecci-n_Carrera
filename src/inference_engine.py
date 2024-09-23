def inference_engine(input_data, knowledge_base):
    recommendations_dict = {}

    for rule in knowledge_base:
        conditions = rule['conditions']
        match_count = 0

        # Verificar coincidencias en cada condición
        for cond, value in conditions.items():
            if cond == 'genero':
                # Comprobar si alguno de los géneros del input_data está en los géneros del rule
                input_generos = set(input_data.get('genero', '').split(','))
                rule_generos = set(value.strip('{}').split(','))
                if input_generos.intersection(rule_generos):
                    match_count += 1
            elif cond == 'anio' or cond == 'duracion' or cond == 'motivo':
                # Comparar valores directamente
                if input_data.get(cond, None) == value:
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
