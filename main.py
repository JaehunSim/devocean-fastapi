from fastapi import FastAPI

import tmap

app = FastAPI()


@app.get("/hometime/")
async def hometime(start: str, end: str):
    start_poi = tmap.get_poi_by_keyword(start)
    end_poi = tmap.get_poi_by_keyword(end)
    total_time = tmap.get_total_time(start_poi, end_poi)
    return {"result": total_time}
