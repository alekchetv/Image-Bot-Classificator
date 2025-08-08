from fastapi import FastAPI, UploadFile, File
import uvicorn
from model_loader import load_model
from PIL import Image
import io
from model_loader import load_model, model_predict

app = FastAPI(
    title="Model_API"
)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    model = load_model("model_scripted_resnet50_6_classes.pt")
    predict = model_predict(model, image)
    return {"Status": "Ok", "prediction": predict}

if __name__ == "__main__":
    uvicorn.run(app)
