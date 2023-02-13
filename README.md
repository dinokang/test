# ChatGPT in PYTHON

## OPENAI 회원가입 및 API key 발급 받기

[https://platform.openai.com/overview](https://platform.openai.com/overview) 사이트 방문 후 회원가입 후 로그인

[https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) 로그인 후 Create new secret key

![Screenshot from 2023-02-09 14-11-26.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edb466dc-3789-49e6-a155-06401dd7c8c0/Screenshot_from_2023-02-09_14-11-26.png)

sudo apt install python3.10-venv

python3.10 -m venv openai

pip install --upgrade pip

pip3 install openai

나의 오류 - **No module named 'aiohttp' - 해결 방법 pip3 install aiohttp**

pip3 install --upgrade openai

```python
code 작성
# Define OpenAI API key
openai.api_key = "YOUR API KEY"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input('Question :') 

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print("Answer : " + response)
```

```python
실행결과
Question :what is banana
Answer : 

Banana is a common fruit that is widely grown in tropical regions. It is an elongated yellow fruit that has a sweet taste and is often eaten raw or used in baking. Bananas are a good source of fiber, vitamins, and minerals.
```

참고 :  [https://platform.openai.com/docs/api-reference/introduction](https://platform.openai.com/docs/api-reference/introduction)
