def calculate_ticket_cost(num_tickets):
    total_cost = 0
    discount = 0
    
    for _ in range(num_tickets):
        age = int(input("Введите возраст посетителя: "))
        
        if age < 18:
            # Посетитель до 18 лет проходит бесплатно
            continue
        elif age < 25:
            total_cost += 990
        else:
            total_cost += 1390
    
    if num_tickets > 3:
        discount = 0.1 * total_cost
    
    total_cost -= discount
    
    return total_cost

num_tickets = int(input("Введите количество билетов: "))
total_cost = calculate_ticket_cost(num_tickets)

print("Общая стоимость билетов:", total_cost, "руб.")