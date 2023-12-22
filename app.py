import os
import pandas as pd
from pathlib import Path
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from enum import Enum
from fastapi import FastAPI, Request, Header, HTTPException, Body
from fastapi.responses import RedirectResponse
from typing import Iterable, Tuple, Optional
from itertools import chain

project_path = Path.cwd()
metadata = bootstrap_project(project_path)
session = KedroSession.create(metadata.package_name, project_path)
context = session.load_context()

app = FastAPI(
    title="FastAPI",
    version="0.1.0",
    description="""
        ChimichangApp API helps you do awesome stuff. 🚀
## Items
You can **read items**.
## Users
You will be able to:
* **Create users** (_not implemented_). * **Read users** (_not implemented_).

    """,
    openapi_tags=[{'name': 'users', 'description': 'Operations with users. The **login** logic is also here.'}, {'name': 'items', 'description': 'Manage items. So _fancy_ they have their own docs.'}]
)

@app.get('/')
async def docs_redirect():
    return RedirectResponse(url='/docs')


MLPredictor = context.catalog.load("MLPredictor")


class MLPredictorcut(str, Enum):
    Ideal = "Ideal"
    Premium = "Premium"
    Good = "Good"
    Very_Good = "Very_Good"
    Fair = "Fair"
    

class MLPredictorcolor(str, Enum):
    E = "E"
    I = "I"
    J = "J"
    H = "H"
    F = "F"
    G = "G"
    D = "D"
    

class MLPredictorclarity(str, Enum):
    I1 = "I1"
    SI2 = "SI2"
    SI1 = "SI1"
    VS2 = "VS2"
    VS1 = "VS1"
    VVS2 = "VVS2"
    VVS1 = "VVS1"
    IF = "IF"
    





@app.get("/my_model", tags=['users'])
def predict_my_model(
carat:float, 
    
    cut:MLPredictorcut, 
    
    color:MLPredictorcolor, 
    
    clarity:MLPredictorclarity, 
    depth:float, 
    table:float, 
    x:float, 
    y:float, 
    z:float
    ):
    args={
    "carat": carat,
    "cut": cut,
    "color": color,
    "clarity": clarity,
    "depth": depth,
    "table": table,
    "x": x,
    "y": y,
    "z": z,
    }
    df = pd.DataFrame({k: [v] for k, v in args.items()})
    result = MLPredictor.predict(df, context)
    
    if result.get('error'):
        raise HTTPException(
            status_code=int(result.get('error').get('status_code')), 
            detail=result.get('error').get('detail')
        )

    return result
def _get_values_as_tuple(values: Iterable[str]) -> Tuple[str, ...]:
    return tuple(chain.from_iterable(value.split(",") for value in values))


@app.post("/kedro")
def kedro(
    request: dict = Body(..., example={
        "pipeline_name": "",
        "tag": [],
        "node_names": [],
        "from_nodes": [],
        "to_nodes": [],
        "from_inputs": [],
        "to_outputs": [],
        "params": {}
    })
):
    pipeline_name = request.get("pipeline_name")
    tag = request.get("tag")
    node_names = request.get("node_names")
    from_nodes = request.get("from_nodes")
    to_nodes = request.get("to_nodes")
    from_inputs = request.get("from_inputs")
    to_outputs = request.get("to_outputs")
    params = request.get("params")

    tag = _get_values_as_tuple(tag) if tag else tag
    node_names = _get_values_as_tuple(node_names) if node_names else node_names
    package_name = str(Path(__file__).resolve().parent.name)
    try:
        with KedroSession.create(package_name, env=None, extra_params=params) as session:
            return session.run(
                    tags=tag,
                    node_names=node_names,
                    from_nodes=from_nodes,
                    to_nodes=to_nodes,
                    from_inputs=from_inputs,
                    to_outputs=to_outputs,
                    pipeline_name=pipeline_name,
                )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.get("/catalog")
def catalog(
    name: str
):
    try:
        file = context.catalog.load(name)
        return file.to_json(force_ascii=False)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))