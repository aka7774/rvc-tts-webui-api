import os
import re
import datetime
import time
import subprocess
import json
import gradio_client

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

def rvctts(args: dict):
    args.setdefault('speed', 0)
    args.setdefault('tts_voice', 'ja-JP-NanamiNeural-Female')
    args.setdefault('f0_key_up', 0)
    args.setdefault('f0_method', 'rmvpe')
    args.setdefault('index_rate', 1)
    args.setdefault('protect0', 0.33)

    url = f"http://127.0.0.1:{args['port']}/"
    grc = gradio_client.Client(url)
    res = grc.predict(
        args['model_name'],
        int(args['speed']),
        args['tts_text'],
        args['tts_voice'],
        float(args['f0_key_up']),
        args['f0_method'],
        float(args['index_rate']),
        float(args['protect0']),
        fn_index=0)
    return res

def change_voice(args: dict):
    url = f"http://127.0.0.1:{args['port']}/"
    grc = gradio_client.Client(url)

    res = grc.predict(
        args['model_name'],
        0.33,
        0.33,
        api_name='/infer_change_voice')
    return res

def infer_convert(args: dict):
    url = f"http://127.0.0.1:{args['port']}/"
    grc = gradio_client.Client(url)

    info, path = grc.predict(
        0,
        args['source_wav'],
        0,
        'README.md', # dummy
        'rmvpe',
        '',
        args['model_index'],
        0.75,
        3,
        0,
        0.25,
        0.33,
        api_name='/infer_convert')

    print(info)
    print(path)
    with open(path, 'rb') as f:
        body = f.read()

    return body

@app.post("/rvctts")
async def api_rvctts_post(args: dict) -> Response:
    return Response(content=rvctts(args), media_type="audio/wav")

@app.post("/change_voice")
async def api_change_voice_post(args: dict) -> Response:
    return change_voice(args)

@app.post("/infer_convert")
async def api_infer_convert_post(args: dict) -> Response:
    return Response(content=infer_convert(args), media_type="audio/wav")
