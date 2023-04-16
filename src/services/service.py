import httpx
import re

DOMEN='https://sci-hub.ru'
DOI='https://doi.org/10.1007/s10462-020-09848-z'

async def downloadPdf(domen,doi):
    src = r'src="(\/downloads.*\.pdf).*"'

    try:

        async with httpx.AsyncClient() as client :

            result = await client.get(f"{domen}/{doi}")
            
            pathOfDownload = re.findall(src,str(result.content),flags=re.MULTILINE)
            return pathOfDownload[0]
    except Exception as e:
        print(f'caught {type(e)}: e')