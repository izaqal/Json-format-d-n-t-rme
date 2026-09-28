import json
dosya = input("Dosya adı girin (uzantısız): ")
def telegramla_egitmek(input_file, output_file):
	with open(input_file, 'r', encoding='utf-8') as f:
		data = json.load(f)
	with open(output_file, 'w', encoding='utf-8') as out:
		for i in range(len(data) - 1):
			input_msg = data[i].get("Mesaj: ", "")
			output_msg = data[i+1].get("Mesaj: ", "")
			if input_msg.strip() and output_msg.strip():
				entry = {
					"instruction": "Sen bu Telegram grubunun bir üyesisin ve grubun geçmiş konuşmalarından elde ettiğin bilgilere ve konuşma tarzına sahipsin. Sana sorulan sorulara, grubun bilgi birikimini kullanarak ve grubun üslubuyla cevap ver.",
					"input": input_msg,
					"output": output_msg
				}
				out.write(json.dumps(entry, ensure_ascii=False) + '\n')
telegramla_egitmek(f"{dosya}.json", f"{dosya}.jsonl")
print(f"İşlem tamam, {dosya}.jsonl dosyası hazır")
