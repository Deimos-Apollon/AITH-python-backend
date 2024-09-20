

async def send_text(send, status_code: int, info: str) -> None:
    await send({
        'type': 'http.response.start',
        'status': status_code,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': info.encode("utf-8"),
    })

