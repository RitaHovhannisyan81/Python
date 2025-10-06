def mill_game():
    print("Սկսում ենք խաղը։ Յուրաքանչյուր ճիշտ հարցի համար կստանաս 10 Bon\n")
    bon = 0 

    questions = [
        {
            "question": "Որն է Հայաստանի մայրաքաղաքը?",
            "options": ["Գյումրի", "Իջևան", "Երևան"],
            "answer": "Երևան"
        },
        {
            "question": "Որն է աշխարհի ամենամեծ օվկիանոսը?",
            "options": ["Հնդկական", "Ատլանտյան", "Խաղաղ"],
            "answer": "Խաղաղ"
        },
        {
            "question": "Python լեզվի ստեղծողը ո՞վ է։",
            "options": ["Գիդո վան Ռոսում", "Լարի Փեյջ", "Բիլ Գեյթս", "Մարկ Ցուկերբերգ"],
            "answer": "Գիդո վան Ռոսում"
        }
    ]

    for i, q in enumerate(questions):
        print(f"\nՀԱՐՑ {i+1}: {q['question']}")
        for j, option in enumerate(q["options"], start=1):
            print(f"{j}) {option}")

        # օգտվողը կարող է գրել թե՛ պատասխանի տեքստը, թե՛ համարը
        answer = input("Ձեր պատասխանը (թիվ կամ բառ): ").strip()

        correct_answer = q["answer"].strip()

        # ստուգենք թե արդյոք թիվ է մուտքագրված
        if answer.isdigit():
            index = int(answer) - 1
            if 0 <= index < len(q["options"]):
                chosen = q["options"][index].strip()
            else:
                print("Սխալ պատասխան, փորձիր նորից։")
                continue
        else:
            chosen = answer

        if chosen.lower() == correct_answer.lower():
            print("Ճիշտ է!")
            bon += 10
            print(f"Դուք շահեցիք 10 Bon! Ընդամենը՝ {bon} Bon")
        else:
            print(f" Սխալ պատասխան։ Ճիշտ պատասխանը՝ {correct_answer}")
            print(f"Դուք ունեք {bon} Bon")
            break
    else:
        print("\n Շնորհավորում եմ՝ դուք հաղթեցիք խաղը!!!!")

mill_game()