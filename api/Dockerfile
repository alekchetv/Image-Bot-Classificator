FROM python:3.12.4-slim

ADD main.py /api/
ADD model_loader.py /api/
ADD index_to_name.json /api/
ADD model_scripted_resnet50_6_classes.pt /api/
ADD requirements.txt /api/

WORKDIR /api/
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
RUN pip install -r requirements.txt