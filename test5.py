import requests

get_id = "Screenshot_2023-05-30_181943.png"
hook = "https://discord.com/api/webhooks/1388724725794078892/oHMo46lgqtouiOQDmso5iGQkoXvGWTe4YU6T5CJEHfAhWxTM1vdDizoDw7KIZusOrGxw"

with open(get_id, 'rb') as f:
    requests.post(hook, files={"file": f})
