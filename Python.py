import requests

file_path = "sound.py"
webhook = "https://discord.com/api/webhooks/1388724725794078892/oHMo46lgqtouiOQDmso5iGQkoXvGWTe4YU6T5CJEHfAhWxTM1vdDizoDw7KIZusOrGxw"

with open(file_path, 'rb') as f:
    requests.post(webhook, files={"file": f})
