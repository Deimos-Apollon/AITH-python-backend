from math_functions import factorial, fibonacci, mean
from utils import send_text

from typing import Any, Callable, Awaitable


async def get_factorial(send: Callable[[dict[str, Any]], Awaitable[None]],
                        path_components: list[str], parameters: dict[str, str]):
    if 'n' not in parameters:
        await send_text(send, 400, "Can't read `n` from url")
        return
    n = parameters['n'][0]
    try:
        n = int(n)
    except ValueError as e:    
        await send_text(send, 400, "Error reading `n` from url")
        return 

    try:
        res = factorial(n)
        await send_text(send, 200, str(res))
    except ValueError as e:    
        await send_text(send, 400, repr(e))


async def get_fibonacci(send: Callable[[dict[str, Any]], Awaitable[None]],
                        path_components: list[str], parameters: dict[str, str]):
    if 'n' not in parameters:
        await send_text(send, 400, "Can't read `n` from url")
        return
    n = parameters['n'][0]
    try:
        n = int(n)
    except ValueError as e:    
        await send_text(send, 400, "Error reading `n` from url")
        return

    try:
        res = fibonacci(n)
        await send_text(send, 200, str(res))
    except ValueError as e:    
        await send_text(send, 400, repr(e))


async def get_mean(send: Callable[[dict[str, Any]], Awaitable[None]],
                   path_components: list[str], parameters: dict[str, str]):
    if 'data' not in parameters:
        await send_text(send, 400, "Can't read `data` from url")
        return
    data = parameters['data'][0]
    try:
        data = [float(x) for x in data.split(',')]
    except ValueError as e:    
        await send_text(send, 400, "Error reading `data` from url")
        return

    try:
        res = mean(data)
        await send_text(send, 200, str(res))
    except ValueError as e:    
        await send_text(send, 400, repr(e))