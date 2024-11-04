# disable the InsecureRequestWarning: Unverified HTTPS request is being made to host '127.0.0.1'. Adding certificate verification is strongly advised.
import urllib3
import boto3
import json
urllib3.disable_warnings()

bedrock_client = boto3.client(service_name='bedrock-runtime',
                                region_name = 'us-west-2', # 如果使用美西2的代理,请改成us-west-2
                                endpoint_url='https://xxxx.elb.us-west-2.amazonaws.com',
                                verify = False)# 不验证 SSL

body = {
    "prompt": "\n\nHuman: Hello\n\nAssistant:",
    "max_tokens_to_sample": 300,
    "temperature": 0.5,
    "top_k": 250,
    "top_p": 1,
    "stop_sequences": ["\n\nHuman:"]
}

response = bedrock_client.invoke_model(
    modelId="anthropic.claude-3-5-sonnet-20241022-v2:0",
    body=json.dumps(body)
)

response_body = json.loads(response.get('body').read())
print(response_body.get('completion'))
