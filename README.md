# 

``` 
 
To prepare the application for deployment, use the `sam package` command. 
 
```bash 

sam package  --output-template-file packaged.yaml  --s3-bucket vashi-lambda-code
sam deploy --template-file packaged.yaml --stack-name LambdaCodeLayer --capabilities CAPABILITY_IAM

``` 
 
