def knowledge_base_loader():
    knowledge_base = []

    with open('data/knowledge_base.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split(' : ')  # split the line in rule and conclusion
                conditions_str = parts[0].strip()  # rule_#: conditions
                conclusion = parts[1].strip()

                conditions = {}
                for condition in conditions_str.split(','):
                    key, value = condition.split('=')
                    conditions[key.strip()] = value.strip()

                career = conclusion.split('=')[1].strip()
                knowledge_base.append({
                    'conditions': conditions,
                    'career': career
                })

    return knowledge_base
