# Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3


# Create ACM client
acm = boto3.client('acm')

# Remove tag(s) from the specified certificate.
response = acm.remove_tags_from_certificate(
    CertificateArn='arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012',
    Tags=[
        {
            'Key': 'TagKey1',
            'Value': 'TagValue1'
        },
        {
            'Key': 'TagKey2',
            'Value': 'TagValue2'
        },
    ]
)

print(response)

