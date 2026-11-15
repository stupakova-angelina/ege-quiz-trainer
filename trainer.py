import random

questions = [
    {"question": "Сколько бит в 1 килобайте? (введи число)", "answer": "8192"},
    {"question": "В каком году произошло Крещение Руси?", "answer": "988"},
    {"question": "Чему равна сумма углов треугольника в градусах?", "answer": "180"},
]

print("--- ТРЕНАЖЕР ДЛЯ ПОДГОТОВКИ К ЕГЭ ---")
random.shuffle(questions)

score = 0
mistakes = []

for i, item in enumerate(questions, 1):
    print(f"\nВопрос {i} из {len(questions)}:")
    print(item["question"])

    user_answer = input("Твой ответ: ").strip().lower()

    if user_answer == item["answer"].lower():
        print("Верно!")
        score += 1
    else:
        print(f"Неверно. Правильный ответ: {item['answer']}")
        mistakes.append(item)

print("\n--- ИТОГИ ТРЕНИРОВКИ ---")
print(f"Правильных ответов: {score} из {len(questions)}")

if mistakes:
    print("\nТемы, которые нужно повторить:")
    for m in mistakes:
        print(f"- {m['question']} -> Ответ: {m['answer']}")
else:
    print("Идеальный результат! Ошибок нет.")