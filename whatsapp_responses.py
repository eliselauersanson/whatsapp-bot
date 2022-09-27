palavras_feias = ["cu", "cú", "foder", "fode", "fuder", "fude", "ferrar", "catar"]

def response(input_message):
    message = input_message.lower()

    for palavra in palavras_feias:
        if palavra in message:
            return "Vai vc!!"

    if "tarde" in message:
        return "Boa tarde!"

    elif "fome" in message:
        return "Muita fome"
    else:
        return ":)"


