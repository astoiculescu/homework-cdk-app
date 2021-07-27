
''
cdk init sample-app --language python
''

#activate virtual env
.venv\Scripts\activate.bat

pip install -r requirements.txt

editare app.py

cdk synth 

#deploy
cdk deploy homework-cdk-stack

#verificat in consola ca s-a creat stackul si s3 bucket

#cleanup 
cdk destroy