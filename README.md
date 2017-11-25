## Fluffy Dollop

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

Then run `make deploy` and you'll see something like:

```bash
   • config unchanged          env= function=echo
   • updating function         env= function=echo
   • updated alias current     env= function=echo version=4
   • function updated          env= function=echo name=echo version=4
```

### Links

 - [Apex website](http://apex.run/)
 - [AWS Lambda](https://aws.amazon.com/lambda/details/)