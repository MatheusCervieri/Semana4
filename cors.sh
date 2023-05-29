awslocal apigateway put-rest-api- --rest-api-id awl3u8nm59 --region us-east-1 --cors-configuration '{
    "CORSRules": [
        {
            "AllowedOrigins": ["*"],
            "AllowedMethods": ["GET", "POST", "PUT", "DELETE"],
            "AllowedHeaders": ["*"],
            "MaxAgeSeconds": 3000
        }
    ]
}'