import asyncio
from services.service import downloadPdf
from dotenv import dotenv_values


domen,doi = dotenv_values('.env').values()

async def getreq(domen=domen,doi=doi):
    r= await downloadPdf(domen,doi)
    print(r)
    return r

with asyncio.Runner() as runner:
    runner.run(getreq())