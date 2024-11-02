import re
import requests

base_url = "https://orangesecurity-challengescripting1.chals.io/robots.txt"

with requests.Session() as sess:
    while True:
        page = sess.get(base_url)
        page_content = page.text
        print("Contenu de la page :", page_content)

        recup_operateur = re.search(r"What is the answer to this\s*:\s*(\d+)\s*x\s*(\d+)", page_content)

        if recup_operateur:
            operand1, operand2 = int(recup_operateur.group(1)), int(recup_operateur.group(2))
            calculs = operand1 * operand2
            print(f"Calcul de : {operand1} x {operand2} = {calculs}")

            page = sess.get(base_url, params={'solution': calculs})
            page_content = page.text

            if "You are not one of us..." not in page_content and "What is the answer to this" not in page_content:
                print("Résultat:", page_content)
                break
        else:
            print("Contenu de la page:", page_content)
            break
