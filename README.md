## Fluffy Dollop

[![Build Status](https://travis-ci.org/robertwpaul/fluffy-dollop.svg?branch=master)](https://travis-ci.org/robertwpaul/fluffy-dollop)

The fluffiest of dollops

### Testing

```bash
$ make test
```

Runs the tests and passes [pytest-pep8](https://pypi.python.org/pypi/pytest-pep8) and
[pyflakes](https://pypi.python.org/pypi/pyflakes) over the code.

##### Perform a deployment dry run

This will display a preview of what operations will be performed if you run a deploy:

```bash
$ make deploy-dry-run
```

Example output, updating the `echo` function:

```bash
  + function echo
    size: 641 B -> 782 B

  + alias echo
    version: $LATEST
    alias: current
```

### Deploy

Set the following environment variables:

```bash
$ export AWS_ACCESS_KEY_ID=<access key>
$ export AWS_SECRET_ACCESS_KEY=<secret access key>
$ export AWS_REGION=<region, e.g. eu-west-1>
```

The credentials should belong to a user with the permissions detailed on the
[Apex website](http://apex.run/). The policy Apex provides looks like this:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateRole",
        "iam:CreatePolicy",
        "iam:AttachRolePolicy",
        "iam:PassRole",
        "lambda:GetFunction",
        "lambda:ListFunctions",
        "lambda:CreateFunction",
        "lambda:DeleteFunction",
        "lambda:InvokeFunction",
        "lambda:GetFunctionConfiguration",
        "lambda:UpdateFunctionConfiguration",
        "lambda:UpdateFunctionCode",
        "lambda:CreateAlias",
        "lambda:UpdateAlias",
        "lambda:GetAlias",
        "lambda:ListAliases",
        "lambda:ListVersionsByFunction",
        "logs:FilterLogEvents",
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*"
    }
  ]
}
```

Though it seems like a lot to give the Apex user `iam` permissions, so you can 
limit the resources to which those permissions apply to the policy you're creating
and role the lambdas run under:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:GetFunction",
        "lambda:ListFunctions",
        "lambda:CreateFunction",
        "lambda:DeleteFunction",
        "lambda:InvokeFunction",
        "lambda:GetFunctionConfiguration",
        "lambda:UpdateFunctionConfiguration",
        "lambda:UpdateFunctionCode",
        "lambda:CreateAlias",
        "lambda:UpdateAlias",
        "lambda:GetAlias",
        "lambda:ListAliases",
        "lambda:ListVersionsByFunction",
        "logs:FilterLogEvents",
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreatePolicy",
        "iam:PassRole",
        "iam:CreateRole",
        "iam:AttachRolePolicy"
      ],
      "Resource": [
        "arn:aws:iam::1234567890:policy/policy-name",
        "arn:aws:iam::1234567890:role/role-name"
      ]
    }
  ]
}
```

Then run `make deploy-test` and you'll see something like:

```
   • config unchanged          env= function=echo
   • updating function         env= function=echo
   • updated alias test        env= function=echo version=8
   • function updated          env= function=echo name=echo version=8
```

Test your lambda function, and if it passes, promote to production:

```bash
$ make deploy-prod
```

The code hasn't changed, so the only thing that happens is the `prod` alias
is applied to the latest version of the code:

```
   • config unchanged          env= function=echo
   • code unchanged            env= function=echo
   • updated alias prod        env= function=echo version=8
```

### Build locally

Lambdas are built as zip files and deployed to AWS. You can build the zip locally if
you install Apex and run the [build command](http://apex.run/#building-functions) passing the name of the function to build:

```bash
$ apex build echo > /tmp/echo.zip
```

However, to bundle the libraries in we move stuff around and pollute the function
directory, so to prevent that you can build it in the Docker container.

First, build the container

```bash
$ docker build .
Sending build context to Docker daemon  250.4kB
Step 1/8 : FROM python:2.7-alpine
 ---> 53bf0a99b6d0
Step 2/8 : MAINTAINER Robert Paul
 ---> Using cache
 ---> 38410f7a19d5
Step 3/8 : WORKDIR /usr/src/app
 ---> Using cache
 ---> 3be0998faa12
Step 4/8 : RUN apk add --no-cache curl
 ---> Using cache
 ---> 58d6986f9e2e
Step 5/8 : RUN curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh
 ---> Using cache
 ---> 6db48e101e8b
Step 6/8 : COPY requirements.txt /usr/src/app/
 ---> Using cache
 ---> 6aac5b21d0e7
Step 7/8 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Using cache
 ---> 7b12a12dbf0b
Step 8/8 : COPY . /usr/src/app
 ---> aef855d32dfe
Successfully built aef855d32dfe
```

The last line of the output will contain the image name. Run the build command in a
container running that image:

```bash
$ docker run aef855d32dfe apex build echo > /tmp/echo.zip
```

### Links

 - [Apex website](http://apex.run/)
 - [AWS Lambda](https://aws.amazon.com/lambda/details/)
