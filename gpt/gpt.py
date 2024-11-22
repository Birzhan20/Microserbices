import nest_asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import g4f

nest_asyncio.apply()

app = FastAPI()


class Txt(BaseModel):
    text: str | int


@app.post("/gpt")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user",
                       "content": f"������ ���������� ����-����� �� 200 �������� �� �������, ��� ���������, � ���������� ������� �����: {text}"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/auto/goods/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ���������� �� ���� �� ������������� ����� ���������� Mytrade.kz �� ������ ����� ������: �{text}�."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/auto/goods/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ����� ���������� Mytrade.kz ���������� �� �������� � ������� ��� � �������, ������� ��� ����� � ������ �{text}�. ������� ��������� �������. ��������� ������ ��������� ������� ����, � ������� ����� ����� �������������� ���������� �� ����� ���������� Mytrade.kz � �������, �������, ������ ����. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/auto/categories/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ��������� ������������� ����� ���������� Mytrade.kz �{text}�. ������ ������ ����� ���� ����� ������, �������, ����� ��� ����� � ������ � ������ ���������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/auto/categories/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� 500 ���� � ����������� ���������� ���������� � �������, �������, ������ ���� � ��������� �{text}� �� ������������� ����� ���������� Mytrade.kz. �������� � ������� ������������ ���������� � ��������� �{text}� �� �������� � ������� ��� �� ����� ����. ��������� ������ � �������� �������������� �� ����� ���������� Mytrade.kz ����� � ������ ���� �� ��������� �{text}� � ������� ������� �� ����������. ��������� ������ ��������� ������� ����, � ������� ������� ���� � �������� �������, �������� ��� �������� ���� �� ������ ��������� �� ����� ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/goods/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ����������, ��������������� �� ������������� ����� ���������� Mytrade.kz �� ������ ����� ������: {text}"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/goods/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ����� ���������� Mytrade.kz ���������� �� �������� � ������� ��� � ������� � ������� �{text}�. ������� ������� ���������� ������ �{text}�. ��������� ������ ��������� ������� ����, � ������� ����� ����� ���� �����, �������������� �� ����� ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/category/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� 500 ���� � ���������� ���������� � ��������� �{text}� �� ������������� ����� ���������� Mytrade.kz. �������� � ������� ������������ ���������� � ��������� �{text}� �� �������� � ������� ��� �� ����� ����. ��������� �������������� �� ����� ���������� Mytrade.kz ������ �� ��������� �{text}� � ������� ������� �� ����������. ��������� ������ ��������� ������� ����, � ������� ������� ���� � �������� ������� ������ �� ������ ��������� �� ������ ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/category/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ��������� ������������� ����� ���������� Mytrade.kz �{text}�. ������ ������ ����� ������ ����� ������ ��� ������� � ������ ���������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/realty/goods/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ���������� � ������������ �� ������������� ����� ���������� Mytrade.kz �� ������ ����� ������: �{text}�"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/realty/goods/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ����� ���������� Mytrade.kz ���������� �� �������� � ������� ��� � �������, ������� ��� ����� � ������ �{text}�. ������� ��������� �������. ��������� ������ ��������� ������� ����, � ������� ����� ����� �������������� ���������� �� ����� ���������� Mytrade.kz � �������, �������, ������ ������� ������������. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/realty/categories/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ��������� ������������� ����� ���������� Mytrade.kz �{text}�. ������ ������ ����� ������������ ����� ������, �������, ����� ��� ����� � ������ � ������ ���������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/realty/categories/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� 500 ���� � ����������� ���������� ���������� � �������, �������, ������ ������������ � ��������� �{text}� �� ������������� ����� ���������� Mytrade.kz. �������� � ������� ���������� ���������� � ��������� �{text}� �� �������� � ������� ��� �� ����� ����. ��������� ������ � �������� �������������� �� ����� ���������� Mytrade.kz ���� ������������� �� ��������� �{text}�. ��������� ������ ��������� ������� ����, � ������� ������� ���� � �������� �������, �������� ��� ����� � ������ ������������ �� ������ ��������� �� ����� ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/services/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f" ������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ���������� ��� ������, ��������������� �� ������������� ����� ���������� Mytrade.kz �� ������ ����� ������: �{text}�. ��� ��������� ������ �� ��������� ID ����������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/services/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ����� ���������� Mytrade.kz ���������� �� �������� � ������� ��� �� ������ �{text}�. ������� ������� ���������� ������ �{text}�. ��������� ������ ��������� ������� ����, � ������� ����� ����� ��� ������, �������������� �� ����� ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/categories/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ��������� ������������� ����� ���������� Mytrade.kz �{text}�. ������ ������ ����� ������ ����� ������ ��� ���������� ������ � ������ ���������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/desk/categories/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� 500 ���� � ���������� ���������� �� ������� � ��������� �{text}� �� ������������� ����� ���������� Mytrade.kz. �������� � ������� ������������ ���������� � ��������� �{text}� �� �������� � ������� ��� �� ����� ����. ��������� �������������� �� ����� ���������� Mytrade.kz ������ �� ��������� �{text}� � ������� ������� �� ����������. ��������� ������ ��������� ������� ����, � ������� ������� ���� � �������� ������� ������ �� ������ ��������� �� ����� ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/goods/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ������, ������������ �� ������������� ������� Mytrade.kz �� ������ ����� ������: {text}"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/goods/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ������� Mytrade ����� �{text}� ����������� ���������� �� ����� ����, ������� ���������. ������� ������� ���������� ������ �{text}�. ��������� ������ ��������� ������� ����, � ������� �������� ������� ���� ����� � ������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/category/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� 500 ���� � ������� ������� �� ��������� �{text}� �� ������������� ������� Mytrade.kz. �������� � ������� ������������ ������� � ��������� �{text}� �� ��������� � �������������� �� ����� ����. ��������� ����������� � ������� Mytrade.kz ������ �� ��������� �{text}� � ������� ������� �� ����������. ��������� ������ ��������� ������� ����, � ������� �������� ������� ������ �� ������ ��������� �� ������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/category/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ��������� �������������� ������� Mytrade.kz �{text}�. ������ ������ ����� ������ ����� ������ � ������ ���������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/vacancy/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� �������� ��������, �������������� �� ������������� ������� Mytrade.kz �� ������ ����� ������: �{text}�."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/vacancy/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ������� ������ ������ Mytrade.kz �������� �{text}� � ��������� ������� ����, ������� ���������. ������� ������� �������� �{text}�. ��������� ������ ��������� ������� ����, � ������� �������� ���� ���������� �� ������ �������� � ������� ������ ������ Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/vacancy/resume/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f" ������� ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ������ ���������� ������, �������������� �� ������������� ������� Mytrade.kz �� ������ ����� ������: �{text}�."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/vacancy/resume/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ������� ������ ������ Mytrade.kz ������ ���������� � ����������� �� ��������� �{text}� � ��������� ������� ����, ������� ���������. ������� ������� ������ �{text}�. ��������� ������ ��������� ������� ����, � ������� ���������� ���� ������ �� ��������� (�������� ���������� �� ��� �� ������������ �������� ���������) � ������� ������ ������ Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/phys/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� �� ������������� ��������� Mytrade.kz �������� ���������� � ����������� �������, �������, ������������, �����������, ����������, ��������, ����������� �� ������� ���������� ��� �� �� ������ ����������. � ����� ����������� �������� �� ����������� �������� ��������� ������� � ����� �������� ������, ������� ��� ��������� � ����� ��������. ������ �����, ��� �� ���������� ������� ��� ����� �������� � ��������� ������������� ���������� � ��������� ������ ���������� ��������� �� ������� ����� �����������. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������: {text}"}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/phys/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                "content": f"������ ���������� ������������� � google ����-����� �� ����� 200 ���� ��� ������ �{text}�. ��� ��������� ������ �� ��������� ID ������������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/jud/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� �������� ��������� Mytrade ��������� ������ � ������ �� ��������� � �������� �� ����� ����, ������� ���������. ������� ������� ����������� ������� � ����� �� �������� �� ������� �{text}�. ��������� ������ ��������� ������� ����, � ������� �������� ������� ������ � ������ � ������� � ����� ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������. "}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/jud/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                "content": f"������ ���������� ������������� � google ����-����� �� ����� 200 ���� ��� ������: �{text}�."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)




if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
