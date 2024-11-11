# Customize Bedrock endpoint

### Deploy

1. Sign in to AWS Management Console, switch to the region to deploy the CloudFormation Stack to.
2. Click the following button to launch the CloudFormation Stack in that region. Choose one of the following:
   - **NLB + Bedrock interface endpoint**

      [![Launch Stack](assets/launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/template?stackName=BedrockProxyAPI&templateURL=https://sample-client-for-bedrock-clouformation.s3.us-west-2.amazonaws.com/CustomizeBedrockRunetimeEndpoint.yaml)

### Architecture
<img width="829" alt="image" src="https://github.com/user-attachments/assets/2fe3bf54-c370-4bca-9a1e-b63bbff0f3b6">

<br></br>
**Example SDK Usage**

```python
# disable the InsecureRequestWarning: Unverified HTTPS request is being made to host '127.0.0.1'. Adding certificate verification is strongly advised.
import urllib3
import boto3
import json
urllib3.disable_warnings()

bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name = 'us-west-2', # 如果使用美西2的代理,请改成us-west-2
    endpoint_url='https://xxxx.elb.us-west-2.amazonaws.com',
    verify = False
    aws_access_key_id="",
    aws_secret_access_key=""
    )# 不验证 SSL

body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": "hello"}],
            }
        ],
    }

response = bedrock_client.invoke_model(
    modelId="anthropic.claude-3-5-sonnet-20241022-v2:0",
    body=json.dumps(body)
)

# Process and print the response
result = json.loads(response.get("body").read())
input_tokens = result["usage"]["input_tokens"]
output_tokens = result["usage"]["output_tokens"]
output_list = result.get("content", [])

print("Invocation details:")
print(f"- The input length is {input_tokens} tokens.")
print(f"- The output length is {output_tokens} tokens.")

print(f"- The model returned {len(output_list)} response(s):")
for output in output_list:
    print(output["text"])
```
