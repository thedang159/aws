import boto3

ec2 = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')
image_id = 'ami-08c84d37db8aafe00'
instance_type = 't2.micro'
sgId = 'sg-05cd64705369535c8'

## create instance
# response = ec2.run_instances(
#     ImageId=image_id,
#     InstanceType=instance_type,
#     MinCount=1,
#     MaxCount=1,
#     SecurityGroupIds=[
#         sgId
#     ],
#     TagSpecifications=[
#         {
#             'ResourceType':'instance',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'demo_b1'
#                 },
#             ]
#         },
#     ],
# )
# print("Id:", response['Instances'][0]['InstanceId'])

id = 'i-073e87b42e52b4026'


## check state instance
# response = ec2.describe_instance_status(
#     # Filters=[
#     #     {
#     #         'Name': 'string',
#     #         'Values': [
#     #             'string',
#     #         ]
#     #     },
#     # ],
#     InstanceIds=[
#         id,
#     ],
# )

## Start instance
# response = ec2.start_instances(
#     InstanceIds=[
#         id,
#     ],
# )

## Stop instance
# response = ec2.stop_instances(
#     InstanceIds=[
#         id,
#     ],
# )

## terminate instance
response = ec2.terminate_instances(
    InstanceIds=[
        id,
    ],
)

print(response)