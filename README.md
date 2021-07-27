
```
cdk init sample-app --language python
```

#activate virtual env
```
.venv\Scripts\activate.bat
```

```
pip install -r requirements.txt
```

Am editat fisierul generat app.py
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

cdk synth 

#deploy
cdk deploy homework-cdk-stack

#verificat in consola ca s-a creat stackul si s3 bucket

#cleanup 
cdk destroy