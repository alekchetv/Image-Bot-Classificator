import torch
import json
from torchvision import transforms
import numpy as np


def load_model(model_path: str):
    model = torch.jit.load(model_path).to(torch.device("cpu"))
    model.eval()
    return model


def model_predict(model, image) -> str:
    image_transformer = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.5]*3, [0.5]*3)
    ])

    with open('index_to_name.json', 'r') as json_file:
        label = json.load(json_file)
        image_tensor = image_transformer(image).unsqueeze(axis=0)
        model_output = model(image_tensor).detach().numpy().squeeze()
        print(np.exp(model_output) / np.sum(np.exp(model_output)))
        predict = np.argmax(np.exp(model_output) /
                            np.sum(np.exp(model_output)))
        return label[str(predict)]
