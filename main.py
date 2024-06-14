from fastapi import FastAPI

import tmap

app = FastAPI()


@app.get("/hometime/")
async def hometime(start: str, end: str, app_key: str):
    start_poi = tmap.get_poi_by_keyword(start, app_key)
    end_poi = tmap.get_poi_by_keyword(end, app_key)
    total_time = tmap.get_total_time(start_poi, end_poi, app_key)
    return {"result": total_time}
