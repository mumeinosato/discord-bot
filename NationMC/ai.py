import openai
import json

openai.api_key = "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"

response = openai.Answer.create(
  search_model="ada", 
  model="curie",
  question="三郎は何をもらうと嬉しいですか",
  documents=["太郎はコーヒーが好き", "二郎はお酒が好き", "三郎はココアが好き", "花子はお酒が好き"],
  examples_context="ビビンコは2018年に設立された", 
  examples=[["ビビンコはいつ設立された？", "2018年"]],
  max_tokens=100,
  stop=["\n", "<|endoftext|>"],
)

print(json.dumps(response, ensure_ascii=False, indent=2))