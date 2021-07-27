Pentru rezolvare am folosit urmatoarele comenzi:

Initializare
```
cdk init sample-app --language python
```

Activare virtual env
```
.venv\Scripts\activate.bat
```

```
pip install -r requirements.txt
```

Am editat fisierul app.py, generat de comanda cdk init, folosind un template din https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/cdk/app.py 

```
from aws_cdk import (
    aws_s3 as s3,
    core,
)

class S3Stack(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        bucket = s3.Bucket(
            self, "homework-cdk-bucket",
            versioned=True)

app = core.App()
S3Stack(app, "homework-cdk-stack")
app.synth()

```
Am rulat comanda synthesize pentru crearea template-ului CloudFormation 
```
cdk synth 
```

Deploy
```
cdk deploy homework-cdk-stack
```

Am verificat in consola ca s-a creat stackul si s3 bucket si in consola
```
aws cloudformation list-stacks
```

Cleanup pt a fi sigur ca nu raman resurse create
```
cdk destroy
```