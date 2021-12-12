1) SSE-S3 = s3 manages keys
2) SSE-KMS = encryption uses a KMS CMK
3) SSE-C = Customer uploads a key used for server side encryption
4) client side encryption before upload

- enabling encrpytion on a bucket does not encrypt existing objects
- Enforce encryption at the bucket level with a resource based bucket policy